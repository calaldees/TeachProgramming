package imageKernels;

import java.util.Arrays;
import java.util.function.Supplier;
import java.lang.Math;
import java.awt.Dimension;
import java.util.stream.Stream;
import java.util.stream.IntStream;
import java.util.stream.Collectors;
import java.lang.StringBuilder;


public class Matrix {
    public final Dimension d;
    public final int[] m;

    public Matrix(Dimension d) {this(d, new int[d.width*d.height]);}
    public Matrix(Dimension d, int _default) {this(d, ()->_default);}
    public Matrix(Dimension d, Supplier<Integer> data_func) {
        this(d);
        for (int i=0 ; i<m.length ; i++) {m[i] = data_func.get();}
    }
    public Matrix(Dimension d, int[] m) {
        this.d = d;
        assert m.length == d.width*d.height;
        this.m = m;
    }

    public Matrix clone() {
        return new Matrix(d);
    }

    public int[] data(int x, int y) {return data((y*d.width) + x);}
    public int[] data(int i) {
        return new int[]{
            m(i-1-d.width), m(i-d.width), m(i+1-d.width),
            m(i-1)        , m(i)        , m(i+1),
            m(i-1+d.width), m(i+d.width), m(i+1+d.width),
        };
    }
    private int m(int i) {
        //return i>=0 && i<m.length ? m[i] : 0;
        return m[mod(i, m.length)];  //i%m.length
    }

    private int mod(int n, int m) {
        return ((n % m) + m) % m;
    }

    @Override
    public boolean equals(Object obj) {
        if (obj == null) {return false;}
        if (obj.getClass() != this.getClass()) {return false;}
        Matrix m2 = (Matrix)obj;
        return this.d.equals(m2.d) && Arrays.equals(this.m, m2.m);
    }

    @Override
    public String toString() {
        // Java streams distracted me for far to long
        // DAMNIT! Java streams have forsaken me .. this is a messy hack
        var s = new StringBuilder();
        for (int y=0 ; y<d.height ; y++) {
            s.append(
                //ArraysStreamByte(Arrays.copyOfRange(m, (y+0)*d.width, (y+1)*d.width))
                Arrays.stream(
                    Arrays.copyOfRange(m, (y+0)*d.width, (y+1)*d.width)
                )
                .boxed()
                .map(j->j.toString())
                .collect(Collectors.joining())
            );
            s.append("\n");
        }
        return s.toString();

        //.forEach(s -> System.out.println("yee:"+s));
        /*
        return IntStream.range(0, d.height)
            .map(y -> 
            )
            .collect(Collectors.joining("\n"));
        */
    }
    // `Arrays.stream(byte[] array)` does not exist - polyfill
    // Inspired by https://stackoverflow.com/questions/59003896/create-a-stream-from-a-T-to-a-primitive-T-stream
    Stream<Byte> ArraysStreamByte(byte[] byteArray) {
        return IntStream.range(0, byteArray.length).mapToObj(i -> byteArray[i]);
    }

}