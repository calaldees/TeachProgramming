
// Discussion about "Coupling" .. Do the Stars need to know about the rest of the system? how do they get this data?

namespace Stars

{


  class Star {

    public int x;

    public int y;

    public int speed;

    //public PictureBox pictureBox;


    public void move() { // int width

      x = x + speed;

      if (x >= Form1.width)

      { //pictureBox.Width

        x = 0;

      }

    }

  }


  public partial class Form1 : Form

  {

    int count = 0;

    Star[] stars = new Star[100];

    Random random = new Random();


    public static int width = 0;


    void log(string s) { System.Diagnostics.Debug.WriteLine(s); }

    public Form1()

    {

      InitializeComponent();

      timer1.Interval = 1000 / 60;

      log("hello");

      width = pictureBox1.Width;


      for (int i = 0; i < stars.Length; i++)

      {

        Star s = new Star();

        //s.pictureBox = pictureBox1;

        s.x = random.Next(0, pictureBox1.Width);

        s.y = random.Next(0, pictureBox1.Height);

        s.speed = random.Next(1,7);

        stars[i] = s;

      }


      timer1.Start();

    }


    private void timer1_Tick(object sender, EventArgs e)

    {

      log($"hello {count}");

      count += 1;


      Graphics g = pictureBox1.CreateGraphics();

      int width = (int)g.VisibleClipBounds.Width;

      int height = (int)g.VisibleClipBounds.Height;


      g.FillRectangle(new SolidBrush(Color.Black), 0, 0, width, height);

      g.FillRectangle(new SolidBrush(Color.White), count, 100, 20, 20);


      foreach (Star s in stars) {

        s.move();

        //if (s.x > width) {

        //  s.x = 0;

        //  s.y = random.Next(0, height);

        //}

        g.FillRectangle(new SolidBrush(Color.White), s.x, s.y, s.speed, 2);

      }

    }

  }

}

