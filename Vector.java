public class Vector {
    private double[] values;
    public Vector(double[] values) {
        this.values = values;
    }

    public double get(int index) {
        return values[index];
    }

    public void set(int index, double value) {
        values[index] = value;
    }

    public int size() {
        return values.length;
    }

    public double dot(Vector other) {
        if (values.length != other.size()) {
            throw new IllegalArgumentException("Invalid vector dimensions");
        }

        double result = 0;
        for (int i = 0; i < values.length; i++) {
            result += values[i] * other.get(i);
        }
        return result;
    }

    public Vector add(Vector other) {
        double[] result = new double[values.length];
        for (int i = 0; i < values.length; i++) {
            result[i] = values[i] + other.get(i);
        }
        return new Vector(result);
    }

    public Vector subtract(Vector other) {
        double[] result = new double[values.length];
        for (int i = 0; i < values.length; i++) {
            result[i] = values[i] - other.get(i);
        }
        return new Vector(result);
    }

    public Vector multiply(double scalar) {
        double[] result = new double[values.length];
        for (int i = 0; i < values.length; i++) {
            result[i] = values[i] * scalar;
        }
        return new Vector(result);
    }

    public Vector normalize() {
        double sum = 0;
        for (int i = 0; i < values.length; i++) {
            sum += values[i] * values[i];
        }
        double magnitude = Math.sqrt(sum);
        return multiply(1.0 / magnitude);
    }

    @Override
    public String toString() {
        StringBuilder sb = new StringBuilder();
        sb.append("[");
        for (int i = 0; i < values.length; i++) {
            sb.append(String.format("%.2e", values[i]));
            if (i < values.length - 1) {
                sb.append(", ");
            }
        }
        sb.append("]");
        return sb.toString();
    }
}