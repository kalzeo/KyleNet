using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace KyleNet_UI
{
    public partial class results : Form
    {
        public results()
        {
            InitializeComponent();
        }

        private void results_Load(object sender, EventArgs e)
        {
            Text = "KyleNet UI";

            
        }

        private void optionsToolStripMenuItem_Click(object sender, EventArgs e)
        {

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
            MessageBox.Show("Are you sure you want to exit?", "Exiting", MessageBoxButtons.YesNo, MessageBoxIcon.Question);
        }
    }
}
