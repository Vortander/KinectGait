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
using System.Windows.Navigation;
using System.Windows.Shapes;

namespace KinectGait
{
    /// <summary>
    /// Interaction logic for MainWindow.xaml
    /// </summary>
    public partial class MainWindow : Window
    {
        public MainWindow()
        {
            InitializeComponent();
        }

        private void NovaCaptura_Click(object sender, RoutedEventArgs e)
        {
            var novaCaptura = new DialogoNovaCaptura();
            novaCaptura.Show();
        }

        private void texto1_TextChanged(object sender, TextChangedEventArgs e)
        {

        }

        private void button1_Click(object sender, RoutedEventArgs e)
        {
            var _testeLocal = new classePublica();

            texto1.AppendText("Teste de acesso por fora ");
            texto1.AppendText(Convert.ToString(_testeLocal.GetTeste()));
        }
 
    }
}
