import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.util.ArrayList;
import java.util.List;

public class Main {
    public static String csvPath = "filtered_data.csv";
    public static double learningRate = 0.00003;
    public static int epochs = 10000;

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
        // Step 1: Load the data
        Pair<Matrix, Vector> data = loadCSV(csvPath);
        Matrix trainingData = data.getFirst();
        Vector targets = data.getSecond();

        // Step 2: Create a LinearRegression object
        LinearRegression lr = new LinearRegression(trainingData, targets, learningRate, epochs);

        // Step 3: Train the model
        lr.train();
        System.out.println("Weights: " + lr.weights);

        // Step 4: Predict the output
        double[] input = {0,3.7629329999999968,-2.805316000000005,8};
        double output = lr.predict(input);

        System.out.println("Output: " + output);
    }
}