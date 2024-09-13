namespace Q3PasswordGenerate
{
    partial class Form1
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
            this.label2 = new System.Windows.Forms.Label();
            this.label3 = new System.Windows.Forms.Label();
            this.FirstNameTextBox = new System.Windows.Forms.TextBox();
            this.LastNameTextBox = new System.Windows.Forms.TextBox();
            this.RegistrationNumberTextBox = new System.Windows.Forms.TextBox();
            this.GeneratePasswordButton = new System.Windows.Forms.Button();
            this.GeneratedPasswordLabel = new System.Windows.Forms.Label();
            this.GeneratedPasswordLabel1 = new System.Windows.Forms.Label();
            this.SuspendLayout();
            // 
            // label1
            // 
            this.label1.AutoSize = true;
            this.label1.Font = new System.Drawing.Font("Microsoft Sans Serif", 12F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.label1.Location = new System.Drawing.Point(89, 36);
            this.label1.Name = "label1";
            this.label1.Size = new System.Drawing.Size(137, 29);
            this.label1.TabIndex = 0;
            this.label1.Text = "First Name:";
            // 
            // label2
            // 
            this.label2.AutoSize = true;
            this.label2.Font = new System.Drawing.Font("Microsoft Sans Serif", 12F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.label2.Location = new System.Drawing.Point(92, 62);
            this.label2.Name = "label2";
            this.label2.Size = new System.Drawing.Size(134, 29);
            this.label2.TabIndex = 1;
            this.label2.Text = "Last Name:";
            // 
            // label3
            // 
            this.label3.AutoSize = true;
            this.label3.Font = new System.Drawing.Font("Microsoft Sans Serif", 12F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.label3.Location = new System.Drawing.Point(106, 96);
            this.label3.Name = "label3";
            this.label3.Size = new System.Drawing.Size(120, 29);
            this.label3.TabIndex = 2;
            this.label3.Text = "Reg. No. :";
            // 
            // FirstNameTextBox
            // 
            this.FirstNameTextBox.Location = new System.Drawing.Point(232, 36);
            this.FirstNameTextBox.Multiline = true;
            this.FirstNameTextBox.Name = "FirstNameTextBox";
            this.FirstNameTextBox.Size = new System.Drawing.Size(197, 26);
            this.FirstNameTextBox.TabIndex = 3;
            // 
            // LastNameTextBox
            // 
            this.LastNameTextBox.Location = new System.Drawing.Point(232, 68);
            this.LastNameTextBox.Multiline = true;
            this.LastNameTextBox.Name = "LastNameTextBox";
            this.LastNameTextBox.Size = new System.Drawing.Size(197, 26);
            this.LastNameTextBox.TabIndex = 4;
            // 
            // RegistrationNumberTextBox
            // 
            this.RegistrationNumberTextBox.Location = new System.Drawing.Point(232, 100);
            this.RegistrationNumberTextBox.Multiline = true;
            this.RegistrationNumberTextBox.Name = "RegistrationNumberTextBox";
            this.RegistrationNumberTextBox.Size = new System.Drawing.Size(197, 26);
            this.RegistrationNumberTextBox.TabIndex = 5;
            // 
            // GeneratePasswordButton
            // 
            this.GeneratePasswordButton.Font = new System.Drawing.Font("Microsoft Sans Serif", 11F, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.GeneratePasswordButton.Location = new System.Drawing.Point(205, 153);
            this.GeneratePasswordButton.Name = "GeneratePasswordButton";
            this.GeneratePasswordButton.Size = new System.Drawing.Size(306, 47);
            this.GeneratePasswordButton.TabIndex = 6;
            this.GeneratePasswordButton.Text = "Generate Button";
            this.GeneratePasswordButton.UseVisualStyleBackColor = true;
            this.GeneratePasswordButton.Click += new System.EventHandler(this.GeneratePasswordButton_Click_1);
            // 
            // GeneratedPasswordLabel
            // 
            this.GeneratedPasswordLabel.AutoSize = true;
            this.GeneratedPasswordLabel.Font = new System.Drawing.Font("Microsoft Sans Serif", 14F, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.GeneratedPasswordLabel.Location = new System.Drawing.Point(294, 243);
            this.GeneratedPasswordLabel.Name = "GeneratedPasswordLabel";
            this.GeneratedPasswordLabel.Size = new System.Drawing.Size(0, 32);
            this.GeneratedPasswordLabel.TabIndex = 7;
            // 
            // GeneratedPasswordLabel1
            // 
            this.GeneratedPasswordLabel1.AutoSize = true;
            this.GeneratedPasswordLabel1.Font = new System.Drawing.Font("Microsoft Sans Serif", 12F, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.GeneratedPasswordLabel1.Location = new System.Drawing.Point(200, 275);
            this.GeneratedPasswordLabel1.Name = "GeneratedPasswordLabel1";
            this.GeneratedPasswordLabel1.Size = new System.Drawing.Size(258, 29);
            this.GeneratedPasswordLabel1.TabIndex = 8;
            this.GeneratedPasswordLabel1.Text = "Generated Password";
            // 
            // Form1
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(9F, 20F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(799, 368);
            this.Controls.Add(this.GeneratedPasswordLabel1);
            this.Controls.Add(this.GeneratedPasswordLabel);
            this.Controls.Add(this.GeneratePasswordButton);
            this.Controls.Add(this.RegistrationNumberTextBox);
            this.Controls.Add(this.LastNameTextBox);
            this.Controls.Add(this.FirstNameTextBox);
            this.Controls.Add(this.label3);
            this.Controls.Add(this.label2);
            this.Controls.Add(this.label1);
            this.Name = "Form1";
            this.Text = "Form1";
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private System.Windows.Forms.Label label1;
        private System.Windows.Forms.Label label2;
        private System.Windows.Forms.Label label3;
        private System.Windows.Forms.TextBox FirstNameTextBox;
        private System.Windows.Forms.TextBox LastNameTextBox;
        private System.Windows.Forms.TextBox RegistrationNumberTextBox;
        private System.Windows.Forms.Button GeneratePasswordButton;
        private System.Windows.Forms.Label GeneratedPasswordLabel;
        private System.Windows.Forms.Label GeneratedPasswordLabel1;
    }
}

