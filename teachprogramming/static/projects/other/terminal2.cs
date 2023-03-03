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

    class Point {
        public int x;
        public int y;
        public Point(int x, int y) {this.x = x; this.y = y;}
        public Point(Point p) {this.x = p.x; this.y = p.y;}
        public override bool Equals (object obj){return Equals(obj as Point);}
        public bool Equals (Point p){return p != null && this.x == p.x && this.y == p.y;}
        public override string ToString() {return $"Point(x={x}, y={y})";}
    }

    interface MatrixApply {
        Point apply(Point p);
    }

    class Matrix : MatrixApply {
        // hard coded 3x3 matrix for 2d transforms
        private double[] m = new double[]{1,0,0,0,1,0,0,0,1};  // identity matrix
        public Matrix() {}
        public Matrix(double[] m) {this.m = m;}  // assert length equal?  //params 
        public Matrix(Matrix m) {this.m = m.m;}  // assert length equal?
        public override bool Equals (object obj){return Equals(obj as Matrix);}
        public bool Equals (Matrix m){return Enumerable.SequenceEqual(this.m, m.m);} //return m != null; for (int i ; i<m.length ; i++) {}}
        public override string ToString() {return $"Matrix({String.Join(',',m)})";}
        public Point apply(Point p) {
            return new Point(Convert.ToInt32(m[0]*p.x + m[1]*p.y + m[2]), Convert.ToInt32(m[3]*p.x + m[4]*p.y + m[5]));
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
            m[0]*=x;
            m[4]*=y;
            return this;
        }
        public Matrix translate(double x, double y) {
            m[2]+=x;
            m[5]+=y;
            return this;
        }
        public Matrix rotate(double r) {
            m[0] = Math.Cos(r);
            m[3] = Math.Sin(r);
            m[1] = -m[3];
            m[4] = m[0];
            return this;
        }
        public Matrix invertX() {m[0] = -m[0]; return this;}
        public Matrix invertY() {m[4] = -m[4]; return this;}
    }

    class Polygon {
        public List<Point> pp;
        public Polygon() {this.pp = new List<Point>();}
        public Polygon(IEnumerable<Point> pp) {this.pp = new List<Point>(pp);}
        //public add(Point p) {this.p.Add(p);}
        public Polygon apply(MatrixApply m) {
            return new Polygon(pp.Select((p)=> m.apply(p)));
        }
        public override string ToString() {return $"Polygon({String.Join(',',pp.Select((i)=>i.ToString()))})";}
    }

    public static void Main(string[] args) { new Task(); }
    Task() {
        // https://docs.microsoft.com/en-us/dotnet/api/system.console?view=net-5.0#common-operations
        /*
function csharp {
  mcs "$1" && clear && mono "${1%.*}.exe" && rm "${1%.*}.exe";
}
*/

        /*
        Console.WriteLine(Console.BufferWidth);
        Console.WriteLine(Console.BufferHeight);
        Console.Clear();
        Console.WriteLine(Console.CursorLeft);
        Console.WriteLine(Console.CursorTop);
        Console.Clear();
        Console.SetCursorPosition(10, 10);
        
        Console.ForegroundColor = ConsoleColor.Red;
        Console.Write("Yee");
        Console.SetCursorPosition(10, 10);
        Console.ForegroundColor = ConsoleColor.Green;
        Console.Write("P");
        Console.BackgroundColor = ConsoleColor.Red;
        Console.ForegroundColor = ConsoleColor.Yellow;
        Console.SetCursorPosition(0, 0);
        Console.Write(Console.WindowHeight);
        */

        Console.SetCursorPosition(0, 0);
        Console.BackgroundColor = ConsoleColor.Black;
        Console.ForegroundColor = ConsoleColor.White;

        //line(new Point(0,0), new Point(20,10));
        //Thread.Sleep(1000);
        //line(new Point(0,0), new Point(10,20));
        //Thread.Sleep(1000);
        //line_bresenham(new Point(-1,6),new Point(4,10));

        
        
        Polygon shape = new Polygon();
        shape.pp.AddRange(new Point[]{new Point(0,0),new Point(10,0),new Point(10,10),new Point(0,10), new Point(0,0)});
        /*
        //drawPoly(shape);
        //Console.ReadLine(); Console.Clear();
        Matrix m = new Matrix().scaleY(0.6).translate(5,0);
        drawPoly(shape.apply(m));
        */
        
        


        double r = 0;
        //Point p1 = new Point(0,0);
        //Point p2 = new Point(10,0);
        //Matrix t1 = new Matrix();
        //t1.translate(10,10);
        //t1.translate(-Console.BufferWidth/2, -Console.BufferHeight/2);
        //Matrix t2 = new Matrix();
        //t2.translate(-5,0);
        //t2.translate(Console.BufferWidth/2, Console.BufferHeight/2);
        for (int i=0 ; i<70 ; i++) {
            //Matrix m = new Matrix().rotate(r).translate(20,20);
            //Matrix m = new Matrix().multiply(new Matrix().rotate(r)).multiply(new Matrix().translate(20,20)).multiply(new Matrix().scale(1, 0.65));
            Matrix m = new Matrix()
                .multiply(new Matrix().translate(Console.BufferWidth/2,Console.BufferHeight/2))
                .multiply(new Matrix().scale(1, 0.65))
                .multiply(new Matrix().rotate(r))
                .multiply(new Matrix().scale(2, 2))
                .multiply(new Matrix().translate(-5,-5))
            ;

            //m.rotate(r);
            //m = t1.multiply(m);
            //debug(m.ToString());
            Console.BackgroundColor = ConsoleColor.Black;
            Console.ForegroundColor = ConsoleColor.White;
            drawPoly(shape.apply(m));
            //line(m.apply(p1), m.apply(p2));
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


        Console.ReadLine();
    }


    void debug(string message) {
        Console.BackgroundColor = ConsoleColor.Black;
        Console.ForegroundColor = ConsoleColor.Yellow;
        Console.SetCursorPosition(1, Console.BufferHeight-1);
        Console.Write(message);
        //Thread.Sleep(1000);
        Console.ReadLine();
    }


    public delegate void DrawPixel(int x, int y);

    DrawPixel drawPixel = (x, y) => {
        if (x<0 || y<0 || x>=Console.BufferWidth || y>Console.BufferHeight) {return;}
        Console.SetCursorPosition(x, y);
        Console.Write('#');
    };

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

    void line_bresenham(Point p1, Point p2) {
        // https://en.wikipedia.org/wiki/Bresenham%27s_line_algorithm
        int dx = Math.Abs(p1.x - p2.x);
        int dy = Math.Abs(p1.y - p2.y);
        if (dy<dx) {
            if (p1.x>p2.x) {(p1, p2) = (p2, p1);}
            line_bresenham_x(p1,p2);
        } else {
            if (p1.y>p2.y) {(p1, p2) = (p2, p1);}
            line_bresenham_y(p1,p2);
        }
    }
    void line_bresenham_x(Point p1, Point p2) {
        int dx = p2.x - p1.x;
        int dy = p2.y - p1.y;
        int yi = 1;
        if (dy < 0) {yi = -1; dy = -dy;}
        int D = (2*dy) - dx;
        int y = p1.y;
        //debug($"line_bresenham_x dx={dx} dy={dy} yi={yi} D={D} y={y}");
        for (int x=p1.x ; x<p2.x ; x++) {
            drawPixel(x,y);
            if (D > 0) {y += yi; D = D + (2*(dy - dx));}
            else       {         D = D +  2 *dy       ;}
        }
    }
    void line_bresenham_y(Point p1, Point p2) {
        int dx = p2.x - p1.x;
        int dy = p2.y - p1.y;
        int xi = 1;
        if (dx < 0) {xi = -1; dx = -dx;}
        int D = (2*dx) - dy;
        int x = p1.x;
        for (int y=p1.y ; y<p2.y ; y++) {
            drawPixel(x,y);
            if (D > 0) {x += xi; D = D + (2*(dx - dy));}
            else       {         D = D +  2 *dx       ;}
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
    void drawPoly(Polygon pp) {
        Point _p = null;
        foreach (Point p in pp.pp) {
            if (_p==null || p==null) {_p = p; continue;}
            //debug($"Hey {_p.ToString()} to {p.ToString()}");
            line_bresenham(_p,p);
            _p = p;
        }
    }
}