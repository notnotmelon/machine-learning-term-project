import math
from PIL import Image
from random import random

calculatedWeights = [-9.67e-02, -5.05e-03, 2.77e-02, -5.03e-02, -2.56e-01, 5.46e-04, 1.49e-03, -4.19e-05]
month = 2 # February
cause = 0 # unknown

def calculateHeat(latitude, longitude):
    input = [1, cause, latitude, longitude, month, longitude**2, latitude**2, longitude*latitude]
    heat = 0
    for i in range(0, len(input)):
        heat += input[i] * calculatedWeights[i]
    return math.sqrt(math.e**max(0, heat-17)*3)

center_latitude = 86.778259
center_longitude = -110.417931
percision = 0.05 # each step is a pixel

image = Image.new('RGB', (1000, 1000), 'black')

r,g,b=255,99,71

for x in range(0, 1000):
    for y in range(0, 1000):
        latitude = center_latitude + (y - 500) * percision
        longitude = center_longitude + (x - 500) * percision
        heat = calculateHeat(latitude, longitude)
        if random() < 0.001:
            print(f'heat: {heat}, latitude: {latitude}, longitude: {longitude}')
        image.putpixel((x, y), (
            int(min(255, heat*r/255)),
            int(min(255, heat*g/255)),
            int(min(255, heat*b/255)))
        )


image.show()