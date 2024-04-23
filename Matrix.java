public class Matrix {
    private double[][] values;
    public Matrix(double[][] values) {
        this.values = values;
    }

    public double get(int row, int col) {
        return values[row][col];
    }

    public void set(int row, int col, double value) {
        values[row][col] = value;
    }

    public int rows() {
        return values.length;
    }

    public int cols() {
        return values[0].length;
    }

    public Vector multiply(Vector vector) {
        double[] result = new double[values.length];
        for (int i = 0; i < values.length; i++) {
            result[i] = new Vector(values[i]).dot(vector);
        }
        return new Vector(result);
    }

    public Matrix multiply(Matrix other) {
        if (cols() != other.rows()) {
            throw new IllegalArgumentException("Invalid matrix dimensions");
        }

        double[][] result = new double[values.length][other.cols()];
        for (int i = 0; i < values.length; i++) {
            for (int j = 0; j < other.cols(); j++) {
                double sum = 0;
                for (int k = 0; k < values[0].length; k++) {
                    sum += values[i][k] * other.get(k, j);
                }
                result[i][j] = sum;
            }
        }
        return new Matrix(result);
    }

    public Matrix transpose() {
        double[][] result = new double[values[0].length][values.length];
        for (int i = 0; i < values.length; i++) {
            for (int j = 0; j < values[0].length; j++) {
                result[j][i] = values[i][j];
            }
        }
        return new Matrix(result);
    }

    @Override
    public String toString() {
        StringBuilder sb = new StringBuilder();
        sb.append("[");
        for (int i = 0; i < values.length; i++) {
            sb.append("[");
            for (int j = 0; j < values[0].length; j++) {
                sb.append(values[i][j]);
                if (j < values[0].length - 1) {
                    sb.append(", ");
                }
            }
            sb.append("]");
            if (i < values.length - 1) {
                sb.append(", ");
            }
        }
        sb.append("]");
        return sb.toString();
    }
}