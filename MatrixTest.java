import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;

public class MatrixTest {
    @Test
    public void testMultiply() {
        double[][] values1 = {{1, 2, 3}, {4, 5, 6}};
        double[][] values2 = {{7, 8}, {9, 10}, {11, 12}};
        Matrix matrix1 = new Matrix(values1);
        Matrix matrix2 = new Matrix(values2);
        Matrix expected = new Matrix(new double[][]{{58, 64}, {139, 154}});
        Matrix result = matrix1.multiply(matrix2);
        assertEquals(expected.toString(), result.toString());
    }
}