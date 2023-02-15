package imageKernels;

import java.util.List;
import java.util.function.Function;
import java.util.stream.IntStream;
import java.util.stream.Collectors;

import java.io.ByteArrayOutputStream;
import java.io.ByteArrayInputStream;
import java.io.ObjectInputStream;
import java.io.ObjectOutputStream;
import java.io.IOException;

import imageKernels.Matrix;
import imageKernels.Kernel;


public class MatrixOperation {
    private MatrixOperation() {}

    public static Matrix apply(Matrix m1, Kernel k) {
        Matrix m2 = m1.cloneEmpty();
        apply(m1, k, m2, m1.indexes());
        return m2;
    }

    private static void apply(Matrix m1, Kernel k, Matrix m2, IntStream range) {
        range.forEachOrdered(i -> {
            //System.out.println(i);
            m2.m(i, k.apply(m1.data(i)));
        });
    }

    public static Matrix applyThreaded(Matrix m1, Kernel k       ) {return applyThreaded(m1,k,4);}
    public static Matrix applyThreaded(Matrix m1, Kernel k, int t) {
        Matrix m2 = m1.cloneEmpty();
        IntStream.range(0, t)
            .mapToObj(threadNumber -> {
                int batch_size = (int)(m1.dataSize() / t);
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
                catch (InterruptedException e) {e.printStackTrace();}
            });
        return m2;
    }

    public static Matrix applyNetwork(Matrix m1, Kernel k       ) {return applyNetwork(m1,k,4);}
    public static Matrix applyNetwork(Matrix m1, Kernel k, int t) {
        Matrix m2 = m1.cloneEmpty();

        // Output matrix segments to byte stream
        ByteArrayOutputStream inMemoryStream = new ByteArrayOutputStream();
        try {
            ObjectOutputStream outputStream = new ObjectOutputStream(inMemoryStream);
        
            IntStream.range(0, t)
                .forEach(segmentNumber -> {
                    int batch_size = (((int)(m1.dataSize() / t) / m1.d.width)+1)*m1.d.width;
                    int offset = segmentNumber * batch_size;
                    String threadName = String.format("%s: offset:%s length:%s",segmentNumber,offset,batch_size);

                    try {
                        if (offset + batch_size > m1.dataSize()) {batch_size = m1.dataSize() - offset;}
                        //System.out.println(String.format("%s %s", offset_round_down, offset_round_down+batch_size_round_up));
                        outputStream.writeObject(m1.cloneSegment(offset, batch_size));
                    } catch (IOException e) {e.printStackTrace();}
                });

            outputStream.close();
        } catch (IOException e) {e.printStackTrace();}

        // Input matrix segments from byte stream
        try {
            ByteArrayInputStream inputStream = new ByteArrayInputStream(inMemoryStream.toByteArray());
            ObjectInputStream in = new ObjectInputStream(inputStream);

            while (true) {
                Matrix m3;
                try {m3 = (Matrix)in.readObject();} catch (IOException ex) {break;}

                var m4 = m3.cloneSegment();
                apply(m3, k, m4, m3.indexesSafe());
                // TODO: send m4 back over network

                // temp for now
                m2.mergeSegment(m4);
            }

            in.close();
            inputStream.close();
            inMemoryStream.close();
        }
        catch (IOException e) {e.printStackTrace();}
        catch (ClassNotFoundException e) {e.printStackTrace();}

        return m2;
    }
}