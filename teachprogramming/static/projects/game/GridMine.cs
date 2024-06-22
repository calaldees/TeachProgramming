using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace GridMine
{
    public partial class Form1 : Form
    {

        private int[,] grid;
        public Form1()
        {
            InitializeComponent();
            initGrid(10, 10);
        }

        private void log(string str) {
            System.Diagnostics.Debug.WriteLine(str);
        }

        public void initGrid(int width, int height) {
            grid = new int[width, height];
            updateCellSize();
        }


        private Size cellSize;
        private void updateCellSize() {
            cellSize = new Size(Width / grid.GetLength(0), Height / grid.GetLength(1));
        }


        private void drawGrid(Graphics g) {
            for (int y = 0; y < grid.GetLength(1); y++){
                for (int x = 0; x < grid.GetLength(0); x++){
                    var v = grid[x, y];
                    Color c = v > 0 ? Color.Red : Color.Black;
                    var cellPos = new Point(x * cellSize.Width, y * cellSize.Height);
                    //g.DrawRectangle(new Pen(c, 1), new Rectangle(cellPos, cellSize));
                    g.FillRectangle(new SolidBrush(c), new Rectangle(cellPos, cellSize));
                    g.DrawString($"{x},{y}", DefaultFont, new SolidBrush(Color.Green), cellPos);
                }
            }

        }

        private void Form1_Paint(object sender, PaintEventArgs e) {
            drawGrid(e.Graphics);
        }

        private void Form1_SizeChanged(object sender, EventArgs e) {
            updateCellSize();
            Invalidate();
        }

        private void Form1_Click(object sender, EventArgs e) {
            var me = (MouseEventArgs)e;
            var (x, y) = (me.X / cellSize.Width, me.Y / cellSize.Height);
            grid[x,y] += 1;
            Invalidate();
        }
    }
}
