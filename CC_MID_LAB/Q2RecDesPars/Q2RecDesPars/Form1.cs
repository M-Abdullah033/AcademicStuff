using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace Q2RecDesPars
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void ParseButton_Click(object sender, EventArgs e)
        {
            string input = InputTextBox.Text;
            bool isValid = ParseInput(input);

            if (isValid)
            {
                ResultLabel.Text = "Input is valid.";
            }
            else
            {
                ResultLabel.Text = "Input is not valid.";
            }
        }

        private bool ParseInput(string input)
        {
            // Split the input by commas and remove leading/trailing spaces
            string[] items = input.Split(',').Select(item => item.Trim()).ToArray();

            foreach (string item in items)
            {
                if (!(item == "id" || item == "num" || item == "string"))
                {
                    return false; // Invalid item found
                }
            }

            return true; // All items are valid
        }

        private void InputLabel_Click(object sender, EventArgs e)
        {

        }

    }
}