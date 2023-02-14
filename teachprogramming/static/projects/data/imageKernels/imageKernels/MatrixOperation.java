package imageKernels;

import java.util.List;
import java.util.function.Function;
import java.util.stream.IntStream;
import java.util.stream.Collectors;

import imageKernels.Matrix;
import imageKernels.Kernel;


public class MatrixOperation {
    private MatrixOperation() {}

    public static Matrix apply(Matrix m1, Kernel k) {
        Matrix m2 = m1.clone();
        apply(m1, k, m2, IntStream.range(0, m1.m.length));
        return m2;
    }

    private static void apply(Matrix m1, Kernel k, Matrix m2, IntStream range) {
        range.forEachOrdered(i -> {
            //System.out.println(i);
            m2.m[i] = k.apply(m1.data(i));
        });
    }

    public static Matrix applyThreaded(Matrix m1, Kernel k       ) {return applyThreaded(m1,k,4);}
    public static Matrix applyThreaded(Matrix m1, Kernel k, int t) {
        Matrix m2 = m1.clone();
        IntStream.range(0, t)
            .mapToObj(threadNumber -> {
                int batch_size = (int)(m1.m.length / t);
                int i = threadNumber * batch_size;
                int j = i + batch_size;
                String threadName = String.format("%s: %s->%s",threadNumber,i,j);
                //System.out.println(threadName);
                Thread thread = new Thread(() -> apply(m1, k, m2, IntStream.range(i,j)),  threadName);
                thread.start();
                return thread;
            })
            .forEach(thread -> {
                try {thread.join();}
                catch (InterruptedException ex) {}
            });
        return m2;
    }
}