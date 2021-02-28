using Numpy;
using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Drawing.Drawing2D;
using System.Drawing.Imaging;
using System.IO;
using System.Linq;
using System.Runtime.InteropServices;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;
using Python.Runtime;
using Keras.PreProcessing.Image;
using Keras;
using System.Reflection;
using Newtonsoft.Json;

namespace KyleNet_UI
{
    public partial class landing : Form
    {
        private Keras.Models.BaseModel model;
        private Keras.Backend backend = new Backend();
        

        public landing()
        {
            InitializeComponent();
        }

        private async void landing_LoadAsync(object sender, EventArgs e)
        {
            backend.Parameters.Clear();

            Text = "KyleNet UI";
            AllowDrop = true;
            DragEnter += new DragEventHandler(landing_DragEnter);
            DragDrop += new DragEventHandler(landing_DragDrop);
            
            MaximumSize = new Size(708, 375);

            // Model must be loaded asynchronously to prevent the application hanging when opened for the first time
            model = await Task.Run(() => Keras.Models.BaseModel.LoadModel(@"C:\Users\Kyle\Desktop\RGU Coursework\Thesis\KyleNet\models\Experiment 4.h5"));
        }

        private string DoPrediction(string path)
        {
            string[] classLabels = new string[] { "COVID-19", "NON-COVID" };
            dynamic img = ImageUtil.LoadImg(path, target_size: (224, 224));
            NDarray x = ImageUtil.ImageToArray(img) / 255;
            x = np.expand_dims(x, axis: 0);
            int prediction = (model.Predict(x, batch_size: 128) > 0.5).asscalar<int>();

            return classLabels[prediction];
        }

        private async void BuildResults(string file)
        {
            landingProgressBar.Visible = true;
            gatheringLabel.Visible = true;

            // Going too quick throws System.AccessViolationException because the model hasn't finished building
            var predict = await Task.Run(() => DoPrediction(file));
            var gradcam = await Task.Run(() => BuildGradCAM(file));
            
            landingProgressBar.Increment(100);


            Hide();
            results _results = new results(file, gradcam, predict);
            _results.Closed += (s, args) => Close();
            _results.Show();
        }

        private Bitmap BuildGradCAM(string path)
        {
            return new Bitmap(path);
        }

        protected override void OnPaint(PaintEventArgs e)
        {
            // Drag and drop dashed rectangle
            Pen blackPen = new Pen(Color.FromArgb(255, 0, 0, 0), 1);
            blackPen.DashStyle = DashStyle.Dash;
            e.Graphics.DrawRectangle(blackPen, 70, 100, 550, 150);
        }

        protected void landing_DragDrop(object sender, DragEventArgs e)
        {
            if (e.Data.GetDataPresent(DataFormats.FileDrop)) e.Effect = DragDropEffects.Copy;
        }

        protected void landing_DragEnter(object sender, DragEventArgs e)
        {
            // Handles drag and dropping images onto the landing page
            string[] files = (string[]) e.Data.GetData(DataFormats.FileDrop);
            BuildResults(files[0]);
        }

        private void landing_Click(object sender, EventArgs e)
        {
            // Opens a file dialog when the landing page is clicked
            var file = string.Empty;

            using (OpenFileDialog openFileDialog = new OpenFileDialog())
            {
                openFileDialog.InitialDirectory = "C:\\";
                openFileDialog.Filter = "Image Files (*.PNG;*.JPG;*.JPEG)|*.PNG;*.JPG;*.JPEG";
                openFileDialog.FilterIndex = 2;
                openFileDialog.RestoreDirectory = true;

                if (openFileDialog.ShowDialog() == DialogResult.OK)
                {
                    //Get the path of specified file
                    file = openFileDialog.FileName;
                }
            }
            
            BuildResults(file);
        }
    }
}
