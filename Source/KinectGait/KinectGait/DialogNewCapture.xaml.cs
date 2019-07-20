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
    public partial class DialogNewCapture : Window
    {
        
        public DialogNewCapture()
        {
            InitializeComponent();
        }

        private void button1_Click(object sender, RoutedEventArgs e)
        {
            string nameDirectory = textBox1.Text;
            
            var directory = new CreateDirectory();
            
            int numero_arquivo = directory.createDirectory(nameDirectory);

            Person.SetNewPerson(nameDirectory);
            Person.SetFileCounter(numero_arquivo);
            Window.GetWindow(this).Close();
          
        }

        private void button2_Click(object sender, RoutedEventArgs e)
        {
            Window.GetWindow(this).Close();
        }
 
    }
}
