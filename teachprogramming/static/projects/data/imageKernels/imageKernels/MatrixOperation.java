package imageKernels;

import imageKernels.Matrix;
import imageKernels.Kernel;

public class MatrixOperation {

    public static Matrix apply(Matrix m, Kernel k) {
        Matrix m2 = m.clone();
        for (int i=0 ; i<m.m.length ; i++) {
            m2.m[i] = k.apply(m.data(i));
        }
        return m2;
    }

    private MatrixOperation() {}
}