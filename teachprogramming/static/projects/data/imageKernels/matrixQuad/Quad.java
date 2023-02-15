package matrixQuad;

import java.io.Serializable;
import java.lang.StringBuilder;


interface Node {}


public class Quad implements Serializable, Node {
    public enum Segment {
        TOP_LEFT(0),
        TOP_RIGHT(1),
        BOTTOM_LEFT(3),
        BOTTOM_RIGHT(4),
        ;
        public final int index;
        Segment(int index) {this.index = index;}
    }
    public final Node[] nodes = new Node[4];

    public Quad() {}

}

class Leaf implements Serializable, Node {

}