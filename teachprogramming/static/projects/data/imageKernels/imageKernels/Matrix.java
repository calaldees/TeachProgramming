package imageKernels;

import java.io.Serializable;
import java.util.Arrays;
import java.util.function.Supplier;
import java.lang.Math;
import java.awt.Dimension;
import java.util.stream.Stream;
import java.util.stream.IntStream;
import java.util.stream.Collectors;
import java.lang.StringBuilder;


public class Matrix implements Serializable {
    public final Dimension d;
    private final int[] m;
    private final int offset;

    public Matrix(Dimension d) {this(d, new int[d.width*d.height]);}
    public Matrix(Dimension d, int _default) {this(d, ()->_default);}
    public Matrix(Dimension d, Supplier<Integer> data_func) {
        this(d);
        for (int i=0 ; i<m.length ; i++) {m[i] = data_func.get();}
    }
    public Matrix(Dimension d, int[] m) {this(d,m,0);}
    public Matrix(Dimension d, int[] m, int o) {
        //assert m.length == d.width*d.height;
        assert o+m.length <= d.width*d.height : "offset+data is bigger than data-size!";
        assert o        % d.width == 0 : "offset must be multiple of width";
        assert m.length % d.width == 0 : "data segment must be multiple of width";
        if (o > 0) {
            //assert m.length >= d.width*3 : "data length is too low to be safe with buffer of one layer each side of this data chunk";
        }
        this.d = d;
        this.offset = o;
        this.m = m;
    }

    public Matrix cloneEmpty() {
        return new Matrix(d);
    }
    public Matrix cloneSegment() {
        return new Matrix(d, new int[this.m.length], this.offset);
    }
    public Matrix cloneSegment(int offset, int length) {
        return new Matrix(d, Arrays.copyOfRange(m, offset, offset+length), offset);
    }
    public void mergeSegment(Matrix m2) {
        assert this.d.equals(m2.d) : "only matrix of the same size can be merged";
        m2.indexesSafe().forEach(i -> {
            this.m(i, m2.m(i));
        });
    }


    public int dataSize() {return m.length;}
    public IntStream indexes() {
        return IntStream.range(offset, offset+m.length);
    }
    public IntStream indexesSafe() {
        if (offset==0) {return indexes();}
        return IntStream.range(offset+d.width, offset+m.length-d.width);
    }

    public int[] data(int x, int y) {return data((y*d.width) + x);}
    public int[] data(int i) {
        return new int[]{
            m(i-1-d.width), m(i-d.width), m(i+1-d.width),
            m(i-1        ), m(i        ), m(i+1        ),
            m(i-1+d.width), m(i+d.width), m(i+1+d.width),
        };
    }
    public int m(int i) {
        //return i>=0 && i<m.length ? m[i] : 0;
        return m[mod(i-offset, m.length)];  //i%m.length
    }
    public void m(int i, int value) {
        m[i-offset] = value;
    }

    private int mod(int n, int m) {
        return ((n % m) + m) % m;
    }

    @Override
    public boolean equals(Object obj) {
        if (obj == null) {return false;}
        if (obj.getClass() != this.getClass()) {return false;}
        Matrix m2 = (Matrix)obj;
        return this.d.equals(m2.d) && this.offset==m2.offset && Arrays.equals(this.m, m2.m);
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