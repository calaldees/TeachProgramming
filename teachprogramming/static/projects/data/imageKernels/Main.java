import java.util.Random;
import java.util.function.Supplier;
import java.awt.Dimension;

import imageKernels.Kernel;
import imageKernels.Matrix;
import imageKernels.MatrixOperation;


class Main {
    public static void main(String[] args) {
        // https://setosa.io/ev/image-kernels/

        final Random r = new Random();
        Supplier<Integer> rand_int = () -> r.nextInt(0,10);

        Matrix m1 = new Matrix(new Dimension(10,10), rand_int);
        System.out.println(m1.toString());

        Matrix m2 = MatrixOperation.apply(m1, Kernel.BLUR);
        System.out.println(m2.toString());

        //System.out.println(mm.m.length);
    }
}