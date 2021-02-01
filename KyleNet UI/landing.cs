using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Drawing.Drawing2D;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace KyleNet_UI
{
    public partial class landing : Form
    {
        public landing()
        {
            InitializeComponent();
        }

        private void landing_Load(object sender, EventArgs e)
        {
            Text = "KyleNet UI";
        }

        protected override void OnPaint(PaintEventArgs e)
        {
            // Drag and drop dashed rectangle
            Pen blackPen = new Pen(Color.FromArgb(255, 0, 0, 0), 1);
            blackPen.DashStyle = DashStyle.Dash;
            e.Graphics.DrawRectangle(blackPen, 70, 100, 550, 150);
        }
    }
}
