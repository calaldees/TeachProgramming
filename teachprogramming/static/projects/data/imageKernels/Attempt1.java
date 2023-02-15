import java.util.Random;
import java.util.function.Supplier;
import java.awt.Dimension;

import imageKernels.Kernel;
import imageKernels.Matrix;
import imageKernels.MatrixOperation;


class Attempt1 {
    public static void main(String[] args) {
        // https://setosa.io/ev/image-kernels/

        final Random r = new Random();
        Supplier<Integer> rand_int = () -> r.nextInt(0,10);

        Matrix m1 = new Matrix(new Dimension(10,10), rand_int);
        System.out.println(m1.toString());

        Matrix m2 = MatrixOperation.apply(m1, Kernel.BLUR);
        System.out.println(m2.toString());

        Matrix m3 = MatrixOperation.applyThreaded(m1, Kernel.BLUR);
        //System.out.println(m3.toString());
        assert m2.equals(m3) : "single thread and multi thread matrix should match";

        Matrix m5 = MatrixOperation.applyNetwork(m1, Kernel.BLUR);
        System.out.println(m5.toString());
        assert m2.equals(m5) : "single thread and network matrix should match";

        //Matrix m4 = m1.cloneSegment(80, 120);
        Matrix m4 = m1.cloneSegment(20, 40);
        assert m1.m(31) == m4.m(31) : "clone segment data should match";
        m4.m(31, 0);
        m1.mergeSegment(m4);
        assert 0 == m4.m(31) : "merged segment data should match";
        //System.out.println(m1.toString());

        

    }
}