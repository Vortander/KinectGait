using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Windows;
using System.Windows.Controls;
using System.Windows.Data;
using System.Windows.Documents;
using System.Windows.Input;
using System.Windows.Media;
using System.Windows.Media.Imaging;
using System.Windows.Shapes;

namespace KinectGait
{
    /// <summary>
    /// Logica de interação para DialogoNovaCaptura.xaml
    /// </summary>
    public partial class DialogoNovaCaptura : Window
    {
        public DialogoNovaCaptura()
        {
            InitializeComponent();
        }

        private void button1_Click(object sender, RoutedEventArgs e)
        {

        }

        private void button2_Click(object sender, RoutedEventArgs e)
        {
            Window.GetWindow(this).Close();
        }

        private void checkBox1_Checked_1(object sender, RoutedEventArgs e)
        {

        }

    }
}
