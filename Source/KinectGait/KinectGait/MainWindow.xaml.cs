using System;
using System.Threading;
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
using Microsoft.Research.Kinect;
using Microsoft.Research.Kinect.Nui;

namespace KinectGait
{
    /// <summary>
    /// Interaction logic for MainWindow.xaml
    /// </summary>
    public partial class MainWindow : Window
    {

        PointList list_of_points = new PointList();

        Boolean buttonStart_isClicked = false;
        Boolean buttonStop_isClicked = true;

        //Globais KINECT
        Runtime nui;
        int totalFrames = 0;
        int lastFrames = 0;

        DateTime lastTime = DateTime.MaxValue;

        const int RED_IDX = 2;
        const int GREEN_IDX = 1;
        const int BLUE_IDX = 0;

        byte[] depthFrame32 = new byte[320 * 240 * 4];

        Dictionary<JointID, Brush> jointColors = new Dictionary<JointID, Brush>()
        {
            //{JointID.HipCenter, new SolidColorBrush(Color.FromRgb(169, 176, 155))},
            //{JointID.Spine, new SolidColorBrush(Color.FromRgb(169, 176, 155))},
            //{JointID.ShoulderCenter, new SolidColorBrush(Color.FromRgb(168, 230, 29))},
            //{JointID.Head, new SolidColorBrush(Color.FromRgb(200, 0, 0))},
            //{JointID.ShoulderLeft, new SolidColorBrush(Color.FromRgb(79, 84, 33))},
            //{JointID.ElbowLeft, new SolidColorBrush(Color.FromRgb(84, 33, 42))},
            //{JointID.WristLeft, new SolidColorBrush(Color.FromRgb(255, 126, 0))},
            //{JointID.HandLeft, new SolidColorBrush(Color.FromRgb(215, 86, 0))},
            //{JointID.ShoulderRight, new SolidColorBrush(Color.FromRgb(33, 79, 84))},
            //{JointID.ElbowRight, new SolidColorBrush(Color.FromRgb(33, 33, 84))},
            //{JointID.WristRight, new SolidColorBrush(Color.FromRgb(77, 109, 243))},
            //{JointID.HandRight, new SolidColorBrush(Color.FromRgb(37, 69, 243))},
            //{JointID.HipLeft, new SolidColorBrush(Color.FromRgb(77, 109, 243))},
            //{JointID.KneeLeft, new SolidColorBrush(Color.FromRgb(69, 33, 84))},
            //{JointID.AnkleLeft, new SolidColorBrush(Color.FromRgb(229, 170, 122))},
            //{JointID.FootLeft, new SolidColorBrush(Color.FromRgb(255, 126, 0))},
            //{JointID.HipRight, new SolidColorBrush(Color.FromRgb(181, 165, 213))},
            //{JointID.KneeRight, new SolidColorBrush(Color.FromRgb(71, 222, 76))},
            //{JointID.AnkleRight, new SolidColorBrush(Color.FromRgb(245, 228, 156))},
            //{JointID.FootRight, new SolidColorBrush(Color.FromRgb(77, 109, 243))}

            {JointID.HipCenter, new SolidColorBrush(Color.FromRgb(255, 0, 0))},
            {JointID.Spine, new SolidColorBrush(Color.FromRgb(255, 0, 0))},
            {JointID.ShoulderCenter, new SolidColorBrush(Color.FromRgb(255, 0, 0))},
            {JointID.Head, new SolidColorBrush(Color.FromRgb(255, 0, 0))},
            {JointID.ShoulderLeft, new SolidColorBrush(Color.FromRgb(255, 0, 0))},
            {JointID.ElbowLeft, new SolidColorBrush(Color.FromRgb(255, 0, 0))},
            {JointID.WristLeft, new SolidColorBrush(Color.FromRgb(255, 0, 0))},
            {JointID.HandLeft, new SolidColorBrush(Color.FromRgb(215, 86, 0))},
            {JointID.ShoulderRight, new SolidColorBrush(Color.FromRgb(255, 0, 0))},
            {JointID.ElbowRight, new SolidColorBrush(Color.FromRgb(255, 0, 0))},
            {JointID.WristRight, new SolidColorBrush(Color.FromRgb(255, 0, 0))},
            {JointID.HandRight, new SolidColorBrush(Color.FromRgb(255, 0, 0))},
            {JointID.HipLeft, new SolidColorBrush(Color.FromRgb(255, 0, 0))},
            {JointID.KneeLeft, new SolidColorBrush(Color.FromRgb(255, 0, 0))},
            {JointID.AnkleLeft, new SolidColorBrush(Color.FromRgb(255, 0, 0))},
            {JointID.FootLeft, new SolidColorBrush(Color.FromRgb(255, 0, 0))},
            {JointID.HipRight, new SolidColorBrush(Color.FromRgb(255, 0, 0))},
            {JointID.KneeRight, new SolidColorBrush(Color.FromRgb(255, 0, 0))},
            {JointID.AnkleRight, new SolidColorBrush(Color.FromRgb(255, 0, 0))},
            {JointID.FootRight, new SolidColorBrush(Color.FromRgb(255, 0, 0))}
        };

        //

                
        public MainWindow()
        {
            InitializeComponent();
        }

        public void NewCapture_Click(object sender, RoutedEventArgs e)
        {
            if (!buttonStop_isClicked)
            {
                if (buttonStart_isClicked)
                    MessageBox.Show("Click <Stop> to pause the current capture");
            }
            else
            {
                list_of_points.ClearList();

                var newCapture = new DialogNewCapture();
                newCapture.Show();
                 
            }
        }

        public void SaveCapture_Click(object sender, RoutedEventArgs e)
        {
            if (buttonStart_isClicked)
            {
                MessageBox.Show("Click <stop> to save current capture");
            }
            else
            {
                PointsFile file = new PointsFile();

                string capture_exists = Person.GetPerson();
                int capture = Person.GetFileCounter();

                if (String.IsNullOrEmpty(capture_exists))
                {
                    MessageBox.Show("There is no current capture to be saved");
                }
                else
                {
                    file.SavePoints(Convert.ToString(capture), list_of_points.GetPointList());
                    buttonStart_isClicked = false;
                    buttonStop_isClicked = true;
                }
            }
        }

        private void regularTilt_Click(object sender, RoutedEventArgs e)
        {
            //var novaRegulagem = new DialogoCalibrar();
            //this.Hide();
            //novaRegulagem.Show();
        }
       
        private void about_Click(object sender, RoutedEventArgs e)
        {
        
        }
        
        private void buttonStart_Click(object sender, RoutedEventArgs e)
        {
            string capture_exists = Person.GetPerson();
            if (String.IsNullOrEmpty(capture_exists))
            {
                MessageBox.Show("Start <New capture> on menu <Capture>");
            }
            else
            {
                buttonStart_isClicked = true;
                buttonStop_isClicked = false;
                personText.Text = capture_exists;
                counterText.Text = Convert.ToString(Person.GetFileCounter());
            }
        }

        private void buttonStop_Click(object sender, RoutedEventArgs e)
        {
            string capture_exists = Person.GetPerson();
            if (String.IsNullOrEmpty(capture_exists))
            {
                MessageBox.Show("Start <New capture> on menu <Capture>");
            }
            else
            {
                buttonStop_isClicked = true;
                buttonStart_isClicked = false;
            }
        }

        private void Window_Loaded(object sender, RoutedEventArgs e)
        {
            nui = new Runtime();

            try
            {
                nui.Initialize(RuntimeOptions.UseDepthAndPlayerIndex | RuntimeOptions.UseSkeletalTracking | RuntimeOptions.UseColor);
            }
            catch (InvalidOperationException)
            {
                MessageBox.Show("Problem starting NUI API");
            }

            try
            {
                nui.VideoStream.Open(ImageStreamType.Video, 2, ImageResolution.Resolution640x480, ImageType.Color);
                nui.DepthStream.Open(ImageStreamType.Depth, 2, ImageResolution.Resolution320x240, ImageType.DepthAndPlayerIndex);
            }
            catch (InvalidOperationException)
            {
                MessageBox.Show("Problem on Video/Depth Streams");
            }

            lastTime = DateTime.Now;

            ////aplicando um smoothing - verificar os parametros
            //this.nui.SkeletonEngine.TransformSmooth = true;
            //TransformSmoothParameters parameters = new TransformSmoothParameters();
            //parameters.Smoothing = 0.0f;
            //parameters.Correction = 0.3f;
            //parameters.Prediction = 0.4f;
            //parameters.JitterRadius = 0.5f;
            //parameters.MaxDeviationRadius = 0.5f;
            //this.nui.SkeletonEngine.SmoothParameters = parameters;

            nui.DepthFrameReady += new EventHandler<ImageFrameReadyEventArgs>(nui_DepthFrameReady);
            nui.SkeletonFrameReady += new EventHandler<SkeletonFrameReadyEventArgs>(nui_SkeletonFrameReady);
            nui.VideoFrameReady += new EventHandler<ImageFrameReadyEventArgs>(nui_ColorFrameReady);
        }


        //VIDEO
        public void nui_ColorFrameReady(object sender, ImageFrameReadyEventArgs e)
        {
            PlanarImage Image = e.ImageFrame.Image;
            video.Source = BitmapSource.Create(Image.Width, Image.Height, 96, 96, PixelFormats.Bgr32, null, Image.Bits, Image.Width * Image.BytesPerPixel);
        }
        //

        //PROFUNDIDADE

        private byte[] convertDepthFrame(byte[] depthFrame16)
        {
            for (int i16 = 0, i32 = 0; i16 < depthFrame16.Length && i32 < depthFrame32.Length; i16 += 2, i32 += 4)
            {
                int player = depthFrame16[i16] & 0x07;
                int realDepth = (depthFrame16[i16 + 1] << 5) | (depthFrame16[i16] >> 3);
                // transform 13-bit depth information into an 8-bit intensity appropriate
                // for display (we disregard information in most significant bit)
                byte intensity = (byte)(255 - (255 * realDepth / 0x0fff));

                depthFrame32[i32 + RED_IDX] = 0;
                depthFrame32[i32 + GREEN_IDX] = 0;
                depthFrame32[i32 + BLUE_IDX] = 0;

                // choose different display colors based on player
                switch (player)
                {
                    case 0:
                        depthFrame32[i32 + RED_IDX] = (byte)(intensity / 2);
                        depthFrame32[i32 + GREEN_IDX] = (byte)(intensity / 2);
                        depthFrame32[i32 + BLUE_IDX] = (byte)(intensity / 2);
                        break;
                    case 1:
                        depthFrame32[i32 + RED_IDX] = intensity;
                        break;
                    case 2:
                        depthFrame32[i32 + GREEN_IDX] = intensity;
                        break;
                    case 3:
                        depthFrame32[i32 + RED_IDX] = (byte)(intensity / 4);
                        depthFrame32[i32 + GREEN_IDX] = (byte)(intensity);
                        depthFrame32[i32 + BLUE_IDX] = (byte)(intensity);
                        break;
                    case 4:
                        depthFrame32[i32 + RED_IDX] = (byte)(intensity);
                        depthFrame32[i32 + GREEN_IDX] = (byte)(intensity);
                        depthFrame32[i32 + BLUE_IDX] = (byte)(intensity / 4);
                        break;
                    case 5:
                        depthFrame32[i32 + RED_IDX] = (byte)(intensity);
                        depthFrame32[i32 + GREEN_IDX] = (byte)(intensity / 4);
                        depthFrame32[i32 + BLUE_IDX] = (byte)(intensity);
                        break;
                    case 6:
                        depthFrame32[i32 + RED_IDX] = (byte)(intensity / 2);
                        depthFrame32[i32 + GREEN_IDX] = (byte)(intensity / 2);
                        depthFrame32[i32 + BLUE_IDX] = (byte)(intensity);
                        break;
                    case 7:
                        depthFrame32[i32 + RED_IDX] = (byte)(255 - intensity);
                        depthFrame32[i32 + GREEN_IDX] = (byte)(255 - intensity);
                        depthFrame32[i32 + BLUE_IDX] = (byte)(255 - intensity);
                        break;
                }
            }

            return depthFrame32;
        }

        public void nui_DepthFrameReady(object sender, ImageFrameReadyEventArgs e)
        {
            PlanarImage Image = e.ImageFrame.Image;
            byte[] convertedDepthFrame = convertDepthFrame(Image.Bits);
            depth.Source = BitmapSource.Create(Image.Width, Image.Height, 96, 96, PixelFormats.Bgr32, null, convertedDepthFrame, Image.Width * 4);
            ++totalFrames;

            DateTime cur = DateTime.Now;
            if (cur.Subtract(lastTime) > TimeSpan.FromSeconds(1))
            {
                int frameDiff = totalFrames - lastFrames;
                lastFrames = totalFrames;
                lastTime = cur;
                frameRate.Text = frameDiff.ToString() + " fps"; //não coloquei caixa de texto frameRate na interface
            }
        }

        //

        //ESQUELETO
        private Point getDisplayPosition(Joint joint)
        {
            float depthX, depthY;
            nui.SkeletonEngine.SkeletonToDepthImage(joint.Position, out depthX, out depthY);
            depthX = depthX * 320;
            depthY = depthY * 240;
            int colorX, colorY;
            ImageViewArea iv = new ImageViewArea();
            nui.NuiCamera.GetColorPixelCoordinatesFromDepthPixel(ImageResolution.Resolution640x480, iv, (int)depthX, (int)depthY, (short)0, out colorX, out colorY);
            return new Point((int)(esqueletoView.Width * colorX / 640.0), (int)(esqueletoView.Height * colorY / 480));    //"normalizado"
        }

        Polyline getBodySegment(Microsoft.Research.Kinect.Nui.JointsCollection joints, Brush brush, params JointID[] ids)
        {
            PointCollection points = new PointCollection(ids.Length);
            for (int i = 0; i < ids.Length; i++)
            {
                points.Add(getDisplayPosition(joints[ids[i]]));
            }
            Polyline polyline = new Polyline();
            polyline.Points = points;
            polyline.Stroke = brush;
            polyline.StrokeThickness = 5;
            return polyline;
        }

        public void nui_SkeletonFrameReady(object sender, SkeletonFrameReadyEventArgs e)
        {
            SkeletonFrame skeletonFrame = e.SkeletonFrame;
            int iSkeleton = 0;
            float[] coordenada3D = new float[3];
            
            Brush[] brushes = new Brush[6];
            brushes[0] = new SolidColorBrush(Color.FromRgb(128, 255, 255));
            brushes[1] = new SolidColorBrush(Color.FromRgb(0, 255, 0));
            brushes[2] = new SolidColorBrush(Color.FromRgb(0, 0, 255));
            brushes[3] = new SolidColorBrush(Color.FromRgb(255, 255, 64));
            brushes[4] = new SolidColorBrush(Color.FromRgb(255, 64, 255));
            brushes[5] = new SolidColorBrush(Color.FromRgb(128, 128, 255));

            
            esqueletoView.Children.Clear();

            foreach (SkeletonData data in skeletonFrame.Skeletons)
            {
                if (SkeletonTrackingState.Tracked == data.TrackingState) //check if skeleton is tracked
                {

                    personText.Text = Person.GetPerson();
                    
                    //Draw body segments
                    Brush brush = brushes[iSkeleton % brushes.Length];
                    esqueletoView.Children.Add(getBodySegment(data.Joints, brush, JointID.HipCenter, JointID.Spine, JointID.ShoulderCenter, JointID.Head));
                    esqueletoView.Children.Add(getBodySegment(data.Joints, brush, JointID.ShoulderCenter, JointID.ShoulderLeft, JointID.ElbowLeft, JointID.WristLeft, JointID.HandLeft));
                    esqueletoView.Children.Add(getBodySegment(data.Joints, brush, JointID.ShoulderCenter, JointID.ShoulderRight, JointID.ElbowRight, JointID.WristRight, JointID.HandRight));
                    esqueletoView.Children.Add(getBodySegment(data.Joints, brush, JointID.HipCenter, JointID.HipLeft, JointID.KneeLeft, JointID.AnkleLeft, JointID.FootLeft));
                    esqueletoView.Children.Add(getBodySegment(data.Joints, brush, JointID.HipCenter, JointID.HipRight, JointID.KneeRight, JointID.AnkleRight, JointID.FootRight));

                    //Draw joints
                    foreach (Joint joint in data.Joints)
                    {
                        Point jointPos = getDisplayPosition(joint);

                        Line jointLine = new Line();
                        jointLine.X1 = jointPos.X - 3;
                        jointLine.X2 = jointLine.X1 + 6;
                        jointLine.Y1 = jointLine.Y2 = jointPos.Y;
                        jointLine.Stroke = jointColors[joint.ID];
                        jointLine.StrokeThickness = 10;
                        
                        esqueletoView.Children.Add(jointLine);
                    }

                    if (buttonStart_isClicked) 
                    {
                        personText.Text = Person.GetPerson();
                        counterText.Text = Convert.ToString(Person.GetFileCounter());
                        
                        coordenada3D[0] = data.Joints[JointID.Head].Position.X;
                        coordenada3D[1] = data.Joints[JointID.Head].Position.Y;
                        coordenada3D[2] = data.Joints[JointID.Head].Position.Z;
                        list_of_points.SetPointList("Head", coordenada3D );

                        coordenada3D[0] = data.Joints[JointID.ShoulderCenter].Position.X;
                        coordenada3D[1] = data.Joints[JointID.ShoulderCenter].Position.Y;
                        coordenada3D[2] = data.Joints[JointID.ShoulderCenter].Position.Z;
                        list_of_points.SetPointList("Shoulder-center", coordenada3D);

                        coordenada3D[0] = data.Joints[JointID.ShoulderRight].Position.X;
                        coordenada3D[1] = data.Joints[JointID.ShoulderRight].Position.Y;
                        coordenada3D[2] = data.Joints[JointID.ShoulderRight].Position.Z;
                        list_of_points.SetPointList("Shoulder-right", coordenada3D);

                        coordenada3D[0] = data.Joints[JointID.ShoulderLeft].Position.X;
                        coordenada3D[1] = data.Joints[JointID.ShoulderLeft].Position.Y;
                        coordenada3D[2] = data.Joints[JointID.ShoulderLeft].Position.Z;
                        list_of_points.SetPointList("Shoulder-left", coordenada3D);

                        coordenada3D[0] = data.Joints[JointID.ElbowRight].Position.X;
                        coordenada3D[1] = data.Joints[JointID.ElbowRight].Position.Y;
                        coordenada3D[2] = data.Joints[JointID.ElbowRight].Position.Z;
                        list_of_points.SetPointList("Elbow-right", coordenada3D);

                        coordenada3D[0] = data.Joints[JointID.ElbowLeft].Position.X;
                        coordenada3D[1] = data.Joints[JointID.ElbowLeft].Position.Y;
                        coordenada3D[2] = data.Joints[JointID.ElbowLeft].Position.Z;
                        list_of_points.SetPointList("Elbow-left", coordenada3D);

                        coordenada3D[0] = data.Joints[JointID.WristRight].Position.X;
                        coordenada3D[1] = data.Joints[JointID.WristRight].Position.Y;
                        coordenada3D[2] = data.Joints[JointID.WristRight].Position.Z;
                        list_of_points.SetPointList("Wrist-right", coordenada3D);

                        coordenada3D[0] = data.Joints[JointID.WristLeft].Position.X;
                        coordenada3D[1] = data.Joints[JointID.WristLeft].Position.Y;
                        coordenada3D[2] = data.Joints[JointID.WristLeft].Position.Z;
                        list_of_points.SetPointList("Wrist-left", coordenada3D);

                        coordenada3D[0] = data.Joints[JointID.HandRight].Position.X;
                        coordenada3D[1] = data.Joints[JointID.HandRight].Position.Y;
                        coordenada3D[2] = data.Joints[JointID.HandRight].Position.Z;
                        list_of_points.SetPointList("Hand-right", coordenada3D);

                        coordenada3D[0] = data.Joints[JointID.HandLeft].Position.X;
                        coordenada3D[1] = data.Joints[JointID.HandLeft].Position.Y;
                        coordenada3D[2] = data.Joints[JointID.HandLeft].Position.Z;
                        list_of_points.SetPointList("Hand-left", coordenada3D);

                        coordenada3D[0] = data.Joints[JointID.Spine].Position.X;
                        coordenada3D[1] = data.Joints[JointID.Spine].Position.Y;
                        coordenada3D[2] = data.Joints[JointID.Spine].Position.Z;
                        list_of_points.SetPointList("Spine", coordenada3D);

                        coordenada3D[0] = data.Joints[JointID.HipCenter].Position.X;
                        coordenada3D[1] = data.Joints[JointID.HipCenter].Position.Y;
                        coordenada3D[2] = data.Joints[JointID.HipCenter].Position.Z;
                        list_of_points.SetPointList("Hip-center", coordenada3D);

                        coordenada3D[0] = data.Joints[JointID.HipRight].Position.X;
                        coordenada3D[1] = data.Joints[JointID.HipRight].Position.Y;
                        coordenada3D[2] = data.Joints[JointID.HipRight].Position.Z;
                        list_of_points.SetPointList("Hip-right", coordenada3D);

                        coordenada3D[0] = data.Joints[JointID.HipLeft].Position.X;
                        coordenada3D[1] = data.Joints[JointID.HipLeft].Position.Y;
                        coordenada3D[2] = data.Joints[JointID.HipLeft].Position.Z;
                        list_of_points.SetPointList("Hip-left", coordenada3D);

                        coordenada3D[0] = data.Joints[JointID.KneeRight].Position.X;
                        coordenada3D[1] = data.Joints[JointID.KneeRight].Position.Y;
                        coordenada3D[2] = data.Joints[JointID.KneeRight].Position.Z;
                        list_of_points.SetPointList("Knee-right", coordenada3D);

                        coordenada3D[0] = data.Joints[JointID.KneeLeft].Position.X;
                        coordenada3D[1] = data.Joints[JointID.KneeLeft].Position.Y;
                        coordenada3D[2] = data.Joints[JointID.KneeLeft].Position.Z;
                        list_of_points.SetPointList("Knee-left", coordenada3D);

                        coordenada3D[0] = data.Joints[JointID.AnkleRight].Position.X;
                        coordenada3D[1] = data.Joints[JointID.AnkleRight].Position.Y;
                        coordenada3D[2] = data.Joints[JointID.AnkleRight].Position.Z;
                        list_of_points.SetPointList("Ankle-right", coordenada3D);

                        coordenada3D[0] = data.Joints[JointID.AnkleLeft].Position.X;
                        coordenada3D[1] = data.Joints[JointID.AnkleLeft].Position.Y;
                        coordenada3D[2] = data.Joints[JointID.AnkleLeft].Position.Z;
                        list_of_points.SetPointList("Ankle-left", coordenada3D);

                        coordenada3D[0] = data.Joints[JointID.FootRight].Position.X;
                        coordenada3D[1] = data.Joints[JointID.FootRight].Position.Y;
                        coordenada3D[2] = data.Joints[JointID.FootRight].Position.Z;
                        list_of_points.SetPointList("Foot-right", coordenada3D);

                        coordenada3D[0] = data.Joints[JointID.FootLeft].Position.X;
                        coordenada3D[1] = data.Joints[JointID.FootLeft].Position.Y;
                        coordenada3D[2] = data.Joints[JointID.FootLeft].Position.Z;
                        list_of_points.SetPointList("Foot-left", coordenada3D);
                    }
                }
            }
            iSkeleton++;
        }

        //

   }
}
