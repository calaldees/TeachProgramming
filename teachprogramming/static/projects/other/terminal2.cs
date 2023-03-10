using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading;


public class Task
{
    void AssertIsEqual<A> (A a, A b) {AssertIsEqual(a,b,"");}
    void AssertIsEqual<A> (A a, A b, string message) {
        if (!a.Equals(b)) {
            throw new Exception($"Failed AssertIsEqual({a} == {b}): {message}");
        }
    }

    public class Point {
        public double x;
        public double y;
        public Point(int x, int y) {this.x = x; this.y = y;}
        //public Point(double x, double y) {this.x = Convert.ToInt32(x); this.y = Convert.ToInt32(y);}
        public Point(double x, double y) {this.x = x; this.y = y;}
        public Point(Point p) {this.x = p.x; this.y = p.y;}
        public override bool Equals (object obj){return Equals(obj as Point);}
        public bool Equals (Point p){return p != null && this.x == p.x && this.y == p.y;}
        public override string ToString() {return $"Point(x={x}, y={y})";}
    }


    class Matrix {
        // hard coded 3x3 matrix for 2d transforms
        private double[] m = new double[]{1,0,0,0,1,0,0,0,1};  // identity matrix
        public Matrix() {}
        public Matrix(double[] m) {this.m = m;}  // assert length equal?  //params 
        public Matrix(Matrix m) {this.m = m.m;}  // assert length equal?
        public override bool Equals (object obj){return Equals(obj as Matrix);}
        public bool Equals (Matrix m){return Enumerable.SequenceEqual(this.m, m.m);}
        public override string ToString() {return $"Matrix({String.Join(',',m)})";}
        public Point apply(Point p) {
            //Convert.ToInt32(
            return new Point(m[0]*p.x + m[1]*p.y + m[2], m[3]*p.x + m[4]*p.y + m[5]);
        }
        public Matrix multiply(Matrix nn) {
            double[] n = nn.m;
            return new Matrix(new double[]{
                m[0]*n[0] + m[1]*n[3] + m[2]*n[6], m[0]*n[1] + m[1]*n[4] + m[2]*n[7], m[0]*n[2] + m[1]*n[5] + m[2]*n[8],
                m[3]*n[0] + m[4]*n[3] + m[5]*n[6], m[3]*n[1] + m[4]*n[4] + m[5]*n[7], m[3]*n[2] + m[4]*n[5] + m[5]*n[8],
                m[6]*n[0] + m[7]*n[3] + m[8]*n[6], m[6]*n[1] + m[7]*n[4] + m[8]*n[7], m[6]*n[2] + m[7]*n[5] + m[8]*n[8],
            });
        }
        public Matrix scale(double s) {return scale(s,s);}
        public Matrix scale(double x, double y) {
            return multiply(new Matrix(new double[]{x,0,0,0,y,0,0,0,1}));
        }
        public Matrix translate(double x, double y) {
            return multiply(new Matrix(new double[]{1,0,x,0,1,y,0,0,1}));
        }
        public Matrix rotate(double r) {
            double cos = Math.Cos(r);
            double sin = Math.Sin(r);
            return multiply(new Matrix(new double[]{cos,-sin,0,sin,cos,0,0,0,1}));
        }
    }

    class Polygon {
        public List<Point> pp;
        public Polygon() {this.pp = new List<Point>();}
        public Polygon(IEnumerable<Point> pp) {this.pp = new List<Point>(pp);}
        //public add(Point p) {this.p.Add(p);}
        public Polygon apply(Matrix m) {
            return new Polygon(pp.Select((p)=> m.apply(p)));
        }
        public override string ToString() {return $"Polygon({String.Join(',',pp.Select((i)=>i.ToString()))})";}
    }

    void drawPolygon(Polygon pp) {
        Point _p = null;
        foreach (Point p in pp.pp) {
            if (_p==null || p==null) {_p = p; continue;}
            //debug($"Hey {_p.ToString()} to {p.ToString()}");
            line_bresenham(_p,p);
            _p = p;
        }
    }

    public static void Main(string[] args) { new Task(); }
    Task() {
        // https://docs.microsoft.com/en-us/dotnet/api/system.console?view=net-5.0#common-operations
        /*
function csharp {
  mcs "$1" && clear && mono "${1%.*}.exe" && rm "${1%.*}.exe";
}
*/


        Console.SetCursorPosition(0, 0);
        Console.BackgroundColor = ConsoleColor.Black;
        Console.ForegroundColor = ConsoleColor.White;

        
        Polygon shape = new Polygon();
        shape.pp.AddRange(new Point[]{new Point(0,0),new Point(10,0),new Point(10,10),new Point(0,10), new Point(0,0)});
        

        double r = 0;
        for (int i=0 ; i<70 ; i++) {
            Matrix m = new Matrix()  // transforms applyed in reverse order
                .translate(Console.BufferWidth/2,Console.BufferHeight/2)  // center on screen
                .scale(1, 0.65) // compensate for ascii-character-pixels being taller than they are wider
                .rotate(r)      // rotate the shape
                .scale(2, 2)    // the original square was 10by10, this enlarges it to 20by20
                .translate(-5,-5) // rotation is about the origin 0,0 - we want to rotate around the shapes center of 5,5
            ;
            Console.BackgroundColor = ConsoleColor.Black;
            Console.ForegroundColor = ConsoleColor.White;
            drawPolygon(shape.apply(m));

            r-=0.1;
            Thread.Sleep(100);
            Console.Clear();
        }

        /*
        Matrix a = new Matrix();
        Matrix b = new Matrix();
        AssertIsEqual(a, a.multiply(b));
        AssertIsEqual(b.apply(new Point(1,1)) , new Point(1,1));
        b.scale(2);
        b.translate(1,0);
        AssertIsEqual(b.apply(new Point(1,1)) , new Point(3,2));
        */


        //Console.ReadLine();
    }


    void debug(string message) {
        Console.BackgroundColor = ConsoleColor.Black;
        Console.ForegroundColor = ConsoleColor.Yellow;
        Console.SetCursorPosition(1, Console.BufferHeight-1);
        Console.Write(message);
        //Thread.Sleep(1000);
        Console.ReadLine();
    }


    public delegate void DrawPixel(Point p);

    DrawPixel drawPixel = (p) => {
        int _x = Convert.ToInt32(p.x);
        int _y = Convert.ToInt32(p.y);
        if (_x<0 || _y<0 || _x>=Console.BufferWidth || _y>Console.BufferHeight) {return;}
        Console.SetCursorPosition(_x, _y);
        Console.Write('#');
    };


    void line_bresenham(Point p1, Point p2) {
        // https://en.wikipedia.org/wiki/Bresenham%27s_line_algorithm
        var dx = Math.Abs(p1.x - p2.x);
        var dy = Math.Abs(p1.y - p2.y);
        if (dy<dx) {
            if (p1.x>p2.x) {(p1, p2) = (p2, p1);}
            line_bresenham_x(p1,p2);
        } else {
            if (p1.y>p2.y) {(p1, p2) = (p2, p1);}
            line_bresenham_y(p1,p2);
        }
    }
    void line_bresenham_x(Point p1, Point p2) {
        var dx = p2.x - p1.x;
        var dy = p2.y - p1.y;
        var yi = 1;
        if (dy < 0) {yi = -1; dy = -dy;}
        var D = (2*dy) - dx;
        var y = p1.y;
        //debug($"line_bresenham_x dx={dx} dy={dy} yi={yi} D={D} y={y}");
        for (var x=p1.x ; x<p2.x ; x++) {
            drawPixel(new Point(x,y));
            if (D > 0) {y += yi; D = D + (2*(dy - dx));}
            else       {         D = D +  2 *dy       ;}
        }
    }
    void line_bresenham_y(Point p1, Point p2) {
        var dx = p2.x - p1.x;
        var dy = p2.y - p1.y;
        var xi = 1;
        if (dx < 0) {xi = -1; dx = -dx;}
        var D = (2*dx) - dy;
        var x = p1.x;
        for (var y=p1.y ; y<p2.y ; y++) {
            drawPixel(new Point(x,y));
            if (D > 0) {x += xi; D = D + (2*(dx - dy));}
            else       {         D = D +  2 *dx       ;}
        }
    }
    



    // Old poo lines
    /*
    void line_naive(Point p1, Point p2) {
        // https://en.wikipedia.org/wiki/Line_drawing_algorithm#A_naive_line-drawing_algorithm
        int dx = p2.x - p1.x;
        int dy = p2.y - p1.y;
        for (int x=p1.x ; x<p2.x ; x++) {
            int y = p1.y + dy * (x - p1.x) / dx;
            Console.SetCursorPosition(x, y);
            Console.Write('#');
        }
    }

    void line(Point p1, Point p2, char c = '#') {
        // inspired by https://www.tutorialspoint.com/computer_graphics/line_generation_algorithm.htm
        double x = Convert.ToDouble(p1.x);
        double y = Convert.ToDouble(p1.y);
        int dx = Math.Abs(p1.x - p2.x);
        int dy = Math.Abs(p1.y - p2.y);
        int steps = (dx>dy) ? dx : dy;
        double x_step = Convert.ToDouble(dx)/steps;
        double y_step = Convert.ToDouble(dy)/steps;
        for(int v=0; v < steps; v++) {
            x = x + x_step;
            y = y + y_step;
            if (x<0 || y<0 || x>Console.BufferWidth || y>Console.BufferHeight) {continue;}
            Console.SetCursorPosition(Convert.ToInt32(Math.Floor(x)), Convert.ToInt32(Math.Floor(y)));
            Console.Write(c);
        }
    }
    */

}