namespace Stars
{
    public partial class Form1 : Form
    {
        readonly Random random = new Random();
        readonly Color COLOR_BACKGROUND = Color.FromArgb(0, 0, 0);

        Bitmap screen;
        Star[] stars;

        public Form1()
        {
            InitializeComponent();
            timer1.Interval = 1000 / 60;
            pictureBox1_SizeChanged(null, null);
        }

        private void log(string str) { System.Diagnostics.Debug.WriteLine(str); }

        void reset()
        {
            stars = new Star[150];
            for (int i = 0; i < stars.Length; i++)
            {
                Star s = new Star();
                s.x = random.Next(0, screen.Width-1);
                s.y = random.Next(0, screen.Height-1);
                s.speed = random.Next(1, 7);
                stars[i] = s;
            }
            timer1.Start();
        }
        private void timer1_Tick(object sender, EventArgs e)
        {
            Graphics g = Graphics.FromImage(screen);
            Pen whitePen = new Pen(Color.White, 1);
            g.FillRectangle(new SolidBrush(COLOR_BACKGROUND), 0, 0, screen.Width, screen.Height);
            foreach (var s in stars) {
                s.x += s.speed;
                if (s.x >= screen.Width) {
                    s.x = 0;
                    s.y = random.Next(0, screen.Height-1);
                }
                //byte c = (byte)(255 - s.speed * 31);
                //byte c = 255;
                //screen.SetPixel(s.x, s.y, Color.FromArgb(c, c, c));
                g.DrawLine(whitePen, s.x, s.y, s.x - s.speed, s.y);
            }
            pictureBox1.Refresh();
        }

        private void pictureBox1_SizeChanged(object sender, EventArgs e)
        {
            screen = new Bitmap(pictureBox1.Width, pictureBox1.Height);
            pictureBox1.Image = screen;
            reset();
        }

        private void pictureBox1_Click(object sender, EventArgs e)
        {

        }
    }

    class Star {
        public int x;
        public int y;
        public int speed;
        public Star() {}
    }
}