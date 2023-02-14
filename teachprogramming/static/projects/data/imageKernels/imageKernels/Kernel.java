package imageKernels;

import java.lang.Math;

public enum Kernel {
    IDENTITY (new double[]{0,0,0,0,1,0,0,0,0}),
    BLUR (new double[]{0.0625,0.125,0.0625,0.125,0.25,0.125,0.0625,0.125,0.0625}),
    SHARPEN (new double[]{0,-1,0, -1,5,-1, 0,-1,0}),
    ;


    public final double[] k;
    Kernel(double... k) {
        assert k.length==9 : "kernel length fail";
        this.k = k;
    }
    public int apply(int... data) {
        assert data.length==9 : "data length fail";
        double sum = 0;
        for (int i=0 ; i<data.length ; i++) {
            sum += this.k[i] * data[i];
        }
        //return Math.min(9,Math.max(0,(int)sum));  // temp range restrict
        return (int)sum;
    }
}