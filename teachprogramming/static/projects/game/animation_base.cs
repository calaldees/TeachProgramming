using System.Drawing;
using System.Drawing.Drawing2D;
using System.Windows.Forms;

namespace WinFormsApp5
{
    public partial class Form1 : Form
    {
        // Performant graphics loop in C# .Net Forms using the standard builtin System.Drawing libs
        // Inspired by 
        //   https://stackoverflow.com/questions/11020710/is-graphics-drawimage-too-slow-for-bigger-images/
        //   https://swharden.com/csdv/ -> https://github.com/swharden/Csharp-Data-Visualization
        readonly System.Threading.Timer timer;
        readonly Bitmap bmp = new Bitmap(320, 180, System.Drawing.Imaging.PixelFormat.Format32bppRgb);
        BufferedGraphics graphicsBuffer;

        readonly ISet<string> keys_pressed = new HashSet<string>();
        Point mouse = new Point(0, 0);

        int frame = 0;

        int x = 100;
        int y = 100;

        Image image = Image.FromFile("C:\\Users\\ac954\\code\\TeachProgramming\\teachprogramming\\static\\projects\\game\\images\\block.gif");

        public Form1()
        {
            InitializeComponent();

            initGraphicsBuffer();

            //timer1.Interval = 1000 / 60;
            //timer1.Start();

            const int fps = 60;
            timer = new System.Threading.Timer(obj =>
            {
                try { Invoke(() => timer1_Tick(null, null)); }
                catch (Exception ex) when (ex is System.ObjectDisposedException || ex is System.InvalidOperationException) { }
            }, null, 0, 1000 / fps);
        }
        void log(string s) { System.Diagnostics.Debug.WriteLine(s); }

        private void render(int frame)
        {
            using (Pen pen = new Pen(Color.White))
            using (SolidBrush brush = new SolidBrush(Color.Blue))
            using (Graphics g = Graphics.FromImage(bmp))
            {
                g.Clear(Color.Black);

                int t = frame % bmp.Width;
                pen.Color = System.Drawing.ColorTranslator.FromHtml("#f0b000");
                brush.Color = pen.Color;
                g.FillRectangle(brush, t, 10, 120, 80);

                t = frame % bmp.Height;
                pen.Color = Color.Red;
                pen.Width = 5;
                g.DrawLine(pen, t, t, t + 10, t + 10);

                g.DrawImage(image, mouse);

                if (keys_pressed.Contains("Up")) { y += -1; }
                if (keys_pressed.Contains("Down")) { y += 1; }
                if (keys_pressed.Contains("Left")) { x += -1; }
                if (keys_pressed.Contains("Right")) { x += 1; }
                g.DrawImage(image, x, y);
            }

        }


        protected override void OnPaintBackground(PaintEventArgs e) {/* just rely on the bitmap to fill the screen */}
        protected override void OnPaint(PaintEventArgs e)
        { // Called after `Invalidate()` or `Update()`
            Graphics g = graphicsBuffer.Graphics;
            g.CompositingMode = CompositingMode.SourceCopy;
            g.InterpolationMode = InterpolationMode.NearestNeighbor;
            g.DrawImage(bmp, 0, 0, Width, Height);
            graphicsBuffer.Render(e.Graphics);
        }
        private void initGraphicsBuffer()
        {
            if (graphicsBuffer != null) { graphicsBuffer.Dispose(); }
            graphicsBuffer = BufferedGraphicsManager.Current.Allocate(CreateGraphics(), new Rectangle(new Point(0, 0), Size));
        }


        private void timer1_Tick(object sender, EventArgs e)
        {
            //if (keys_pressed.Count > 0) { log(String.Join(",", keys_pressed)); }
            if (keys_pressed.Contains("Escape")) { Close(); }
            // Fullscreen (one way, you can't currently swtich back)
            if (keys_pressed.Contains("Menu") && keys_pressed.Contains("Return")) {
                if (this.FormBorderStyle != FormBorderStyle.None) {
                    this.TopMost = true;
                    this.FormBorderStyle = FormBorderStyle.None;
                    this.WindowState = FormWindowState.Maximized;
                }
            }

            render(frame++);
            Invalidate();
        }

        private void Form1_Resize(object sender, EventArgs e) { initGraphicsBuffer(); }
        private void Form1_KeyDown(object sender, KeyEventArgs e) { keys_pressed.Add(e.KeyCode.ToString()); }
        private void Form1_KeyUp(object sender, KeyEventArgs e) { keys_pressed.Remove(e.KeyCode.ToString()); }
        private void Form1_MouseMove(object sender, MouseEventArgs e)
        {
            mouse.X = (int)((e.Location.X / (double)Width) * bmp.Width);
            mouse.Y = (int)((e.Location.Y / (double)Height) * bmp.Height);
        }
    }
}