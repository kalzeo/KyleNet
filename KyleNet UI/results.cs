using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.IO;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace KyleNet_UI
{
    public partial class results : Form
    {
        public results(string image, Bitmap gradcam, string prediction)
        {
            InitializeComponent();
            originalImageBox.Image = new Bitmap(image);
            xaiImageBox.Image = gradcam;
            predictionLabel.Text = prediction;

            Color color = prediction == "COVID-19" ? Color.Red : Color.SeaGreen;
            predictionLabel.ForeColor = color;

            resultListBox.Items.Add(Path.GetFileName(image));
        }

        private void results_Load(object sender, EventArgs e)
        {
            Text = "KyleNet UI";
            MaximumSize = new Size(1006, 633);
        }

        

        private void aboutToolStripMenuItem_Click(object sender, EventArgs e)
        {
            MessageBox.Show("Created by Kyle McPherson as part of a honours degree project.",
                "About KyleNet UI",
                MessageBoxButtons.OK,
                MessageBoxIcon.Information);
        }

        private void closeToolStripMenuItem_Click(object sender, EventArgs e)
        {
            Hide();
            landing _landing = new landing();
            _landing.Closed += (s, args) => Close();
            _landing.ShowDialog();
        }

        private void closeToolStripMenuItem1_Click(object sender, EventArgs e)
        {
            DialogResult result = MessageBox.Show("Are you sure you want to exit?", "Exiting", MessageBoxButtons.YesNo, MessageBoxIcon.Question);
            
            if (result == DialogResult.Yes)
                Application.Exit();
        }
    }
}
