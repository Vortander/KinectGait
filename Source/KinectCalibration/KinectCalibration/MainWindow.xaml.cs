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
using Microsoft.Research.Kinect;
using Microsoft.Research.Kinect.Nui;

namespace KinectGait
{
    /// <summary>
    /// Interaction logic for Window1.xaml
    /// </summary>
    public partial class DialogoCalibrar : Window
    {

        Runtime nui = new Runtime();
        int angulo = 0;


        public DialogoCalibrar()
        {
            InitializeComponent();
        }

        //VIDEO
        private void nui_ColorFrameReady(object sender, ImageFrameReadyEventArgs e)
        {
            PlanarImage Image = e.ImageFrame.Image;
            image1.Source = BitmapSource.Create(Image.Width, Image.Height, 96, 96, PixelFormats.Bgr32, null, Image.Bits, Image.Width * Image.BytesPerPixel);
        }
        //

        private void button1_Click(object sender, RoutedEventArgs e)
        {
            try
            {
                nui.NuiCamera.ElevationAngle = angulo;
            }
            catch (InvalidOperationException)
            {
                MessageBox.Show("Espere alguns instantes...");
            }
        }

        private void slider1_ValueChanged(object sender, RoutedEventArgs e)
        {
            angulo = (Convert.ToInt32(slider1.Value));
            textBox1.Text = Convert.ToString(angulo);
        }

        private void Window_Loaded(object sender, RoutedEventArgs e)
        {
            nui.Initialize(RuntimeOptions.UseColor);

            try
            {
                nui.VideoStream.Open(ImageStreamType.Video, 2, ImageResolution.Resolution640x480, ImageType.Color);

            }
            catch (InvalidOperationException)
            {
                MessageBox.Show("Problema na abertura dos Streams de Video e/ou Profundidade");
            }

            nui.VideoFrameReady += new EventHandler<ImageFrameReadyEventArgs>(nui_ColorFrameReady);
 
        }
    }
}

