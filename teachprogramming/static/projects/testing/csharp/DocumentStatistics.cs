using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace DocumentStatistics
{
    public partial class FormMainApp : Form
    {
        public FormMainApp()
        {
            InitializeComponent();
        }

        /// <summary>
        /// Button to calculate the statistics of the text supplied in the textbox
        /// </summary>
        /// <param name="sender"></param>
        /// <param name="e"></param>
        private void buttonCalculate_Click(object sender, EventArgs e)
        {
            if (checkBoxNumberofWords.Checked)
            {
                labelNumberofWords.Text = "Number of Words:" + StringCalcStat.GetWordCount(textBoxTextToCalculateStatistics.Text).ToString();
            }
        }

        
    }

    static public class StringCalcStat
    {
        /// <summary>
        /// Tries to find the number of words in a string
        /// </summary>
        /// <param name="text">The string which should be used to find how many words it contains</param>
        /// <returns>The number of words. It should return zero if no word could be found.</returns>
        static public int GetWordCount(string text)
        {
            int wordCount = 0;
            int index = 0;

            while (index < text.Length)
            {
                // Go through each character of a word
                while (!char.IsWhiteSpace(text[index]))
                    index++;

                // Found a word
                wordCount++;

                // Go through all whitespace until next word begins
                while (char.IsWhiteSpace(text[index]))
                    index++;
            }

            return wordCount;
        }
    }
}
