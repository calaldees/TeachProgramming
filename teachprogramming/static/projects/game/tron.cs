using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace WindowsFormsApp2
{
    // Requires timer1 and pictureBox1 with relevent events

    public partial class Form1 : Form
    {
        const short BORDER = 100;
        Color COLOR_BACKGROUND = Color.FromArgb(0,0,0);
        Bitmap screen;
        Player[] players;

        public Form1() {
            InitializeComponent();
            timer1.Interval = 1000 / 60;
            pictureBox1_SizeChanged(null, null);
        }
        void reset() {
            Graphics.FromImage(screen).FillRectangle(new SolidBrush(COLOR_BACKGROUND), 0, 0, screen.Width, screen.Height);
            players = new Player[]{
                new Player("Player 1", Color.Yellow, BORDER, BORDER),
                new Player("Player 2", Color.Red, (short)(screen.Width - BORDER), (short)(screen.Height - BORDER)),
            };
            players[0].right();
            players[1].left();
            timer1.Start();
        }


        private void timer1_Tick(object sender, EventArgs e) {
            foreach (Player p in players) {
                p.move();
                if (hasDied(p)) {
                    timer1.Stop();
                    MessageBox.Show($"{p.name} died");
                    reset();
                    return;
                }
                screen.SetPixel(p.x, p.y, p.color);
            }
            pictureBox1.Refresh();
        }

        bool hasDied(Player p) {
            Color pixel = Color.White;
            try { pixel = screen.GetPixel(p.x, p.y); }
            catch {}
            return !pixel.Equals(COLOR_BACKGROUND);
        }

        private void Form1_KeyDown(object sender, KeyEventArgs e)
        {
            if (e.KeyCode == Keys.Up) { players[0].up(); }
            if (e.KeyCode == Keys.Down) { players[0].down(); }
            if (e.KeyCode == Keys.Left) { players[0].left(); }
            if (e.KeyCode == Keys.Right) { players[0].right(); }

            if (e.KeyCode == Keys.W) { players[1].up(); }
            if (e.KeyCode == Keys.S) { players[1].down(); }
            if (e.KeyCode == Keys.A) { players[1].left(); }
            if (e.KeyCode == Keys.D) { players[1].right(); }
        }

        private void pictureBox1_SizeChanged(object sender, EventArgs e)
        {
            screen = new Bitmap(pictureBox1.Width, pictureBox1.Height);
            pictureBox1.Image = screen;
            reset();
        }
    }

    class Player {
        public string name;
        public short x;
        public short y;
        short x_move;
        short y_move;
        public Color color;

        public Player(string name, Color color, short x, short y) {
            this.name = name;
            this.color = color;
            this.x = x;
            this.y = y;
        }

        public void up() {x_move = 0; y_move = -1;}
        public void down() {x_move = 0; y_move = 1;}
        public void left() {x_move = -1; y_move = 0;}
        public void right() {x_move = 1; y_move = 0;}

        public void move() {x += x_move; y += y_move;}
    }
}
