using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace Q3PasswordGenerate
{
    public partial class Form1 : Form
    {
        private static Random random = new Random();
        public Form1()
        {
            InitializeComponent();
        }

        private void GeneratePasswordButton_Click(object sender, EventArgs e)
        {
            string firstName = FirstNameTextBox.Text;
            string lastName = LastNameTextBox.Text;
            string registrationNumber = RegistrationNumberTextBox.Text;

            string password = GeneratePassword(firstName, lastName, registrationNumber);

            GeneratedPasswordLabel1.Text = "Generated Password: " + password;
            MessageBox.Show("Generated Password: " + password);
        }

        private string GeneratePassword(string firstName, string lastName, string registrationNumber)
        {
            const int maxLength = 20;
            const int specialCharCount = 2;
            const int numberCount = 4;

           // if (firstName.Length + lastName.Length + registrationNumber.Length > maxLength)
            if (firstName.Length > maxLength - 6)
            {
                throw new ArgumentException("Input names and registration number are too long.");
            }

            char firstNameInitial = firstName.Length > 0 ? char.ToUpper(firstName[0]) : 'X';
            char lastNameInitial = lastName.Length > 0 ? char.ToUpper(lastName[0]) : 'Y';

            string lastTwoDigits = new string(registrationNumber.Where(char.IsDigit).Reverse().Take(2).Reverse().ToArray());

            string specialChars = "!@#$%^&*()_+-=[]{}|;:,.<>?";

            string numbers = "0123456789";

            string password = new string(
                Enumerable.Repeat(specialChars, specialCharCount)
                          .Concat(Enumerable.Repeat(numbers, numberCount))
                          .Select(s => s[random.Next(s.Length)])
                          .OrderBy(c => random.Next())
                          .ToArray());

            password += firstNameInitial.ToString() + lastNameInitial.ToString() + lastTwoDigits;

            password = new string(password.ToCharArray().OrderBy(c => random.Next()).ToArray());

            return password;
        }

        private void GeneratePasswordButton_Click_1(object sender, EventArgs e)
        {
             string firstName = FirstNameTextBox.Text;
            string lastName = LastNameTextBox.Text;
            string registrationNumber = RegistrationNumberTextBox.Text;

            string password = GeneratePassword(firstName, lastName, registrationNumber);

            //GeneratedPasswordLabel1.Text = "Generated Password: " + password;
            MessageBox.Show("Generated Password: " + password);
        }
    }
}
