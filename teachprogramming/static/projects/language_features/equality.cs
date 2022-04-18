class Point {
    int a;
    int b;
    public Point(int a, int b) {
        this.a = a;
        this.b = b;
    }
}

Point p1 = new Point(1,1);
Point p2 = new Point(1,1);

Console.WriteLine(p1 == p2);