import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

public class Main {
    public static Scanner s = new Scanner(System.in);
    public static String csvPath = "filtered_data.csv";
    public static double[] calculatedWeights = {-9.67e-02, -5.05e-03, 2.77e-02, -5.03e-02, -2.56e-01, 5.46e-04, 1.49e-03, -4.19e-05};

    public static Pair<Matrix, Vector> loadCSV(String path) {
        try (BufferedReader br = new BufferedReader(new FileReader(path))) {
            br.readLine(); // Skip the header

            String line = "";
            List<double[]> matrix = new ArrayList<>();
            List<Double> vector = new ArrayList<>();

            while ((line = br.readLine()) != null) {
                String[] values = line.split(",");
                double[] matrixRow = new double[values.length];
                matrixRow[0] = 1.0; // Bias term
                double target = Double.parseDouble(values[0]);
                vector.add(target);

                for (int i = 1; i < values.length; i++) {
                    matrixRow[i] = Double.parseDouble(values[i]);
                }
                matrix.add(matrixRow);
            }
            Matrix trainingData = new Matrix(matrix.toArray(new double[0][0]));
            Vector targets = new Vector(vector.stream().mapToDouble(Double::doubleValue).toArray());
            return new Pair<Matrix, Vector>(trainingData, targets);
        } catch (IOException e) {
            e.printStackTrace();
            return null;
        }
    }

    public static void main(String[] args) {
        print("Good morning!");
        print("Welcome to the Fire Prediction System.");
        print("This algorithm predicts the expected # of acres burned in a wildfire based on several parameters.");
        print("Disclaimer: It is only trained for locations in California.");
        print("\n");
        print("Would you like to run predictions or train the model? (p/t)");

        while (true) {
            String choice = s.nextLine();
            if (choice.equals("p")) {
                runPredictions();
                return;
            } else if (choice.equals("t")) {
                runTraining();
                return;
            } else {
                print("Invalid choice");
            }
        }
    }

    public static void runTraining() {
        Pair<Matrix, Vector> data = loadCSV(csvPath);
        Matrix trainingData = data.getFirst();
        Vector targets = data.getSecond();

        double learningRate;
        print("Enter the learning rate: ");
        learningRate = s.nextDouble();
        while (learningRate > 0.00003) {
            print("Learning rate is too high. Please enter a value less than or equal to 0.00003: ");
            learningRate = s.nextDouble();
        }

        int epochs = 10000;
        print("Enter the number of epochs: ");
        epochs = s.nextInt();

        LinearRegression lr = new LinearRegression(trainingData, targets, learningRate, epochs);
        lr.train();
        print("Weights: " + lr.weights);
    }

    public static void runPredictions() {
        print("Enter the cause of the fire (HUMAN, UNKNOWN, or NATURAL): ");
        String fireCause = s.nextLine().toUpperCase();
        while (!fireCause.equals("HUMAN") && !fireCause.equals("UNKNOWN") && !fireCause.equals("NATURAL")) {
            print("Invalid cause. Please enter HUMAN, UNKNOWN, or NATURAL: ");
            fireCause = s.nextLine().toUpperCase();
        }

        double fireCauseValue = 0;
        if (fireCause.equals("HUMAN")) {
            fireCauseValue = 1;
        } else if (fireCause.equals("UNKNOWN")) {
            fireCauseValue = 0;
        } else if (fireCause.equals("NATURAL")) {
            fireCauseValue = -1;
        }

        print("Enter the latitude: ");
        double latitude = s.nextDouble() - 36;

        print("Enter the longitude: ");
        double longitude = s.nextDouble() + 120;

        print("Enter the month (1-12): ");
        int month = s.nextInt();
        while (month < 1 || month > 12) {
            print("Invalid month. Please enter a value between 1 and 12: ");
            month = s.nextInt();
        }

        print("\nPerforming transformation into Z space...");
        double[] input = {fireCauseValue, latitude, longitude, month, longitude * longitude, latitude * latitude, latitude * longitude};
        print("Running calculations...");
        LinearRegression lr = new LinearRegression(new Vector(calculatedWeights));
        double prediction = lr.predict(input);
        String predictionStr = String.format("%.2f", prediction);
        print("\n\nExpected # of acres burned: " + predictionStr);
    }

    public static void print(Object o) {
        System.out.println(o);
    }
}