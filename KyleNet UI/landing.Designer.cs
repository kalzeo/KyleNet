namespace KyleNet_UI
{
    partial class landing
    {
        /// <summary>
        /// Required designer variable.
        /// </summary>
        private System.ComponentModel.IContainer components = null;

        /// <summary>
        /// Clean up any resources being used.
        /// </summary>
        /// <param name="disposing">true if managed resources should be disposed; otherwise, false.</param>
        protected override void Dispose(bool disposing)
        {
            if (disposing && (components != null))
            {
                components.Dispose();
            }
            base.Dispose(disposing);
        }

        #region Windows Form Designer generated code

        /// <summary>
        /// Required method for Designer support - do not modify
        /// the contents of this method with the code editor.
        /// </summary>
        private void InitializeComponent()
        {
            this.label1 = new System.Windows.Forms.Label();
            this.landingProgressBar = new System.Windows.Forms.ProgressBar();
            this.gatheringLabel = new System.Windows.Forms.Label();
            this.SuspendLayout();
            // 
            // label1
            // 
            this.label1.Anchor = System.Windows.Forms.AnchorStyles.Top;
            this.label1.Font = new System.Drawing.Font("Segoe UI", 15.75F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.label1.ForeColor = System.Drawing.SystemColors.ControlText;
            this.label1.Location = new System.Drawing.Point(178, 54);
            this.label1.Name = "label1";
            this.label1.Size = new System.Drawing.Size(335, 30);
            this.label1.TabIndex = 0;
            this.label1.Text = "Drag and drop or upload an image";
            // 
            // landingProgressBar
            // 
            this.landingProgressBar.Location = new System.Drawing.Point(140, 301);
            this.landingProgressBar.Name = "landingProgressBar";
            this.landingProgressBar.Size = new System.Drawing.Size(426, 23);
            this.landingProgressBar.TabIndex = 1;
            this.landingProgressBar.Visible = false;
            // 
            // gatheringLabel
            // 
            this.gatheringLabel.AutoSize = true;
            this.gatheringLabel.Font = new System.Drawing.Font("Segoe UI", 9.75F, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.gatheringLabel.ForeColor = System.Drawing.SystemColors.ControlDarkDark;
            this.gatheringLabel.Location = new System.Drawing.Point(287, 281);
            this.gatheringLabel.Name = "gatheringLabel";
            this.gatheringLabel.Size = new System.Drawing.Size(130, 17);
            this.gatheringLabel.TabIndex = 2;
            this.gatheringLabel.Text = "Gathering results ...";
            this.gatheringLabel.Visible = false;
            // 
            // landing
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 13F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(692, 336);
            this.Controls.Add(this.gatheringLabel);
            this.Controls.Add(this.landingProgressBar);
            this.Controls.Add(this.label1);
            this.FormBorderStyle = System.Windows.Forms.FormBorderStyle.FixedToolWindow;
            this.Name = "landing";
            this.Text = "KyleNet UI";
            this.Load += new System.EventHandler(this.landing_LoadAsync);
            this.Click += new System.EventHandler(this.landing_Click);
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private System.Windows.Forms.Label label1;
        private System.Windows.Forms.ProgressBar landingProgressBar;
        private System.Windows.Forms.Label gatheringLabel;
    }
}

