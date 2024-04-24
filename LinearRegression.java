public class LinearRegression {
    private Matrix trainingData;
    private Vector targets;
    public Vector weights;
    private double learningRate;
    private int epochs;

    public LinearRegression(Matrix trainingData, Vector targets, double learningRate, int epochs) {
        this.trainingData = trainingData;
        this.targets = targets;
        this.weights = new Vector(new double[trainingData.cols()]);
        this.learningRate = learningRate;
        this.epochs = epochs;
    }

    public LinearRegression(Vector weights) {
        this.weights = weights;
    }

    public void train() {
        double previous_rsme = Double.MAX_VALUE;

        for (int epoch = 0; epoch < epochs; epoch++) {
            Vector predictions = trainingData.multiply(weights);
            Vector errors = predictions.subtract(targets);
            Vector gradient = trainingData.transpose().multiply(errors).multiply(1.0 / targets.size());
            weights = weights.subtract(gradient.multiply(learningRate));

            if (epoch % 10 == 0) {
                double rmse = Math.sqrt(errors.dot(errors) / targets.size());
                System.out.println("Epoch: " + epoch + " RMSE: " + rmse + " weights: " + weights);
                if (rmse >= previous_rsme) {
                    System.out.println("Converged after " + epoch + " epochs");
                    break;
                }
                previous_rsme = rmse;
            }
        }
    }

    public double predict(double[] input) {
        double[] biased = new double[input.length + 1];
        biased[0] = 1.0; // Bias term
        for (int i = 0; i < input.length; i++) {
            biased[i + 1] = input[i];
        }
        return Math.pow(Math.E, new Vector(biased).dot(weights));
    }
}