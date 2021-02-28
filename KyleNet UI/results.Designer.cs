namespace KyleNet_UI
{
    partial class results
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
            System.ComponentModel.ComponentResourceManager resources = new System.ComponentModel.ComponentResourceManager(typeof(results));
            this.originalImageBox = new System.Windows.Forms.PictureBox();
            this.xaiImageBox = new System.Windows.Forms.PictureBox();
            this.resultListBox = new System.Windows.Forms.ListBox();
            this.menuStrip1 = new System.Windows.Forms.MenuStrip();
            this.fileToolStripMenuItem = new System.Windows.Forms.ToolStripMenuItem();
            this.closeToolStripMenuItem = new System.Windows.Forms.ToolStripMenuItem();
            this.closeToolStripMenuItem1 = new System.Windows.Forms.ToolStripMenuItem();
            this.aboutToolStripMenuItem = new System.Windows.Forms.ToolStripMenuItem();
            this.predictionLabel = new System.Windows.Forms.Label();
            this.label1 = new System.Windows.Forms.Label();
            this.originalImageHeader = new System.Windows.Forms.TextBox();
            this.gradCamHeader = new System.Windows.Forms.TextBox();
            this.panel1 = new System.Windows.Forms.Panel();
            ((System.ComponentModel.ISupportInitialize)(this.originalImageBox)).BeginInit();
            ((System.ComponentModel.ISupportInitialize)(this.xaiImageBox)).BeginInit();
            this.menuStrip1.SuspendLayout();
            this.panel1.SuspendLayout();
            this.SuspendLayout();
            // 
            // originalImageBox
            // 
            this.originalImageBox.BorderStyle = System.Windows.Forms.BorderStyle.FixedSingle;
            this.originalImageBox.Image = ((System.Drawing.Image)(resources.GetObject("originalImageBox.Image")));
            this.originalImageBox.Location = new System.Drawing.Point(234, 82);
            this.originalImageBox.Name = "originalImageBox";
            this.originalImageBox.Size = new System.Drawing.Size(346, 248);
            this.originalImageBox.SizeMode = System.Windows.Forms.PictureBoxSizeMode.Zoom;
            this.originalImageBox.TabIndex = 0;
            this.originalImageBox.TabStop = false;
            // 
            // xaiImageBox
            // 
            this.xaiImageBox.BorderStyle = System.Windows.Forms.BorderStyle.FixedSingle;
            this.xaiImageBox.Image = ((System.Drawing.Image)(resources.GetObject("xaiImageBox.Image")));
            this.xaiImageBox.Location = new System.Drawing.Point(602, 82);
            this.xaiImageBox.Name = "xaiImageBox";
            this.xaiImageBox.Size = new System.Drawing.Size(346, 248);
            this.xaiImageBox.SizeMode = System.Windows.Forms.PictureBoxSizeMode.Zoom;
            this.xaiImageBox.TabIndex = 1;
            this.xaiImageBox.TabStop = false;
            // 
            // resultListBox
            // 
            this.resultListBox.Font = new System.Drawing.Font("Segoe UI", 9.75F, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.resultListBox.FormattingEnabled = true;
            this.resultListBox.ItemHeight = 17;
            this.resultListBox.Location = new System.Drawing.Point(12, 61);
            this.resultListBox.Name = "resultListBox";
            this.resultListBox.Size = new System.Drawing.Size(198, 497);
            this.resultListBox.TabIndex = 2;
            // 
            // menuStrip1
            // 
            this.menuStrip1.Items.AddRange(new System.Windows.Forms.ToolStripItem[] {
            this.fileToolStripMenuItem,
            this.aboutToolStripMenuItem});
            this.menuStrip1.Location = new System.Drawing.Point(0, 0);
            this.menuStrip1.Name = "menuStrip1";
            this.menuStrip1.Size = new System.Drawing.Size(990, 24);
            this.menuStrip1.TabIndex = 3;
            this.menuStrip1.Text = "menuStrip1";
            // 
            // fileToolStripMenuItem
            // 
            this.fileToolStripMenuItem.DropDownItems.AddRange(new System.Windows.Forms.ToolStripItem[] {
            this.closeToolStripMenuItem,
            this.closeToolStripMenuItem1});
            this.fileToolStripMenuItem.Name = "fileToolStripMenuItem";
            this.fileToolStripMenuItem.Size = new System.Drawing.Size(37, 20);
            this.fileToolStripMenuItem.Text = "File";
            // 
            // closeToolStripMenuItem
            // 
            this.closeToolStripMenuItem.Name = "closeToolStripMenuItem";
            this.closeToolStripMenuItem.Size = new System.Drawing.Size(108, 22);
            this.closeToolStripMenuItem.Text = "New";
            this.closeToolStripMenuItem.Click += new System.EventHandler(this.closeToolStripMenuItem_Click);
            // 
            // closeToolStripMenuItem1
            // 
            this.closeToolStripMenuItem1.Name = "closeToolStripMenuItem1";
            this.closeToolStripMenuItem1.Size = new System.Drawing.Size(108, 22);
            this.closeToolStripMenuItem1.Text = "Close";
            this.closeToolStripMenuItem1.Click += new System.EventHandler(this.closeToolStripMenuItem1_Click);
            // 
            // aboutToolStripMenuItem
            // 
            this.aboutToolStripMenuItem.Name = "aboutToolStripMenuItem";
            this.aboutToolStripMenuItem.Size = new System.Drawing.Size(52, 20);
            this.aboutToolStripMenuItem.Text = "About";
            this.aboutToolStripMenuItem.Click += new System.EventHandler(this.aboutToolStripMenuItem_Click);
            // 
            // predictionLabel
            // 
            this.predictionLabel.Anchor = ((System.Windows.Forms.AnchorStyles)((System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Bottom)));
            this.predictionLabel.AutoSize = true;
            this.predictionLabel.Font = new System.Drawing.Font("Segoe UI Semibold", 14.25F, System.Drawing.FontStyle.Bold);
            this.predictionLabel.ForeColor = System.Drawing.Color.SeaGreen;
            this.predictionLabel.Location = new System.Drawing.Point(531, 437);
            this.predictionLabel.Name = "predictionLabel";
            this.predictionLabel.Size = new System.Drawing.Size(122, 25);
            this.predictionLabel.TabIndex = 5;
            this.predictionLabel.Text = "NON-COVID";
            // 
            // label1
            // 
            this.label1.Anchor = System.Windows.Forms.AnchorStyles.Bottom;
            this.label1.AutoSize = true;
            this.label1.Font = new System.Drawing.Font("Segoe UI", 21.75F, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.label1.ForeColor = System.Drawing.SystemColors.ControlDarkDark;
            this.label1.Location = new System.Drawing.Point(470, 397);
            this.label1.Name = "label1";
            this.label1.Size = new System.Drawing.Size(240, 40);
            this.label1.TabIndex = 6;
            this.label1.Text = "Predicted Result";
            // 
            // originalImageHeader
            // 
            this.originalImageHeader.BackColor = System.Drawing.SystemColors.Window;
            this.originalImageHeader.Cursor = System.Windows.Forms.Cursors.Default;
            this.originalImageHeader.Enabled = false;
            this.originalImageHeader.Font = new System.Drawing.Font("Segoe UI", 12F, System.Drawing.FontStyle.Bold);
            this.originalImageHeader.ForeColor = System.Drawing.SystemColors.ControlDarkDark;
            this.originalImageHeader.Location = new System.Drawing.Point(234, 62);
            this.originalImageHeader.Name = "originalImageHeader";
            this.originalImageHeader.ReadOnly = true;
            this.originalImageHeader.Size = new System.Drawing.Size(346, 29);
            this.originalImageHeader.TabIndex = 7;
            this.originalImageHeader.Text = "Original Image";
            this.originalImageHeader.TextAlign = System.Windows.Forms.HorizontalAlignment.Center;
            // 
            // gradCamHeader
            // 
            this.gradCamHeader.BackColor = System.Drawing.SystemColors.Window;
            this.gradCamHeader.Cursor = System.Windows.Forms.Cursors.Default;
            this.gradCamHeader.Enabled = false;
            this.gradCamHeader.Font = new System.Drawing.Font("Segoe UI", 12F, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.gradCamHeader.ForeColor = System.Drawing.SystemColors.ControlDarkDark;
            this.gradCamHeader.Location = new System.Drawing.Point(602, 62);
            this.gradCamHeader.Name = "gradCamHeader";
            this.gradCamHeader.ReadOnly = true;
            this.gradCamHeader.Size = new System.Drawing.Size(346, 29);
            this.gradCamHeader.TabIndex = 8;
            this.gradCamHeader.Text = "Grad-CAM (todo)";
            this.gradCamHeader.TextAlign = System.Windows.Forms.HorizontalAlignment.Center;
            // 
            // panel1
            // 
            this.panel1.Controls.Add(this.label1);
            this.panel1.Controls.Add(this.predictionLabel);
            this.panel1.Dock = System.Windows.Forms.DockStyle.Fill;
            this.panel1.Location = new System.Drawing.Point(0, 0);
            this.panel1.Name = "panel1";
            this.panel1.Size = new System.Drawing.Size(990, 594);
            this.panel1.TabIndex = 9;
            // 
            // results
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 13F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(990, 594);
            this.Controls.Add(this.gradCamHeader);
            this.Controls.Add(this.originalImageHeader);
            this.Controls.Add(this.resultListBox);
            this.Controls.Add(this.xaiImageBox);
            this.Controls.Add(this.originalImageBox);
            this.Controls.Add(this.menuStrip1);
            this.Controls.Add(this.panel1);
            this.FormBorderStyle = System.Windows.Forms.FormBorderStyle.FixedToolWindow;
            this.MainMenuStrip = this.menuStrip1;
            this.Name = "results";
            this.Text = "KyleNet UI";
            this.Load += new System.EventHandler(this.results_Load);
            ((System.ComponentModel.ISupportInitialize)(this.originalImageBox)).EndInit();
            ((System.ComponentModel.ISupportInitialize)(this.xaiImageBox)).EndInit();
            this.menuStrip1.ResumeLayout(false);
            this.menuStrip1.PerformLayout();
            this.panel1.ResumeLayout(false);
            this.panel1.PerformLayout();
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private System.Windows.Forms.PictureBox originalImageBox;
        private System.Windows.Forms.PictureBox xaiImageBox;
        private System.Windows.Forms.ListBox resultListBox;
        private System.Windows.Forms.MenuStrip menuStrip1;
        private System.Windows.Forms.ToolStripMenuItem fileToolStripMenuItem;
        private System.Windows.Forms.ToolStripMenuItem aboutToolStripMenuItem;
        private System.Windows.Forms.ToolStripMenuItem closeToolStripMenuItem;
        private System.Windows.Forms.Label predictionLabel;
        private System.Windows.Forms.Label label1;
        private System.Windows.Forms.TextBox originalImageHeader;
        private System.Windows.Forms.TextBox gradCamHeader;
        private System.Windows.Forms.ToolStripMenuItem closeToolStripMenuItem1;
        private System.Windows.Forms.Panel panel1;
    }
}