using System;
using System.IO;
using System.Collections.Generic;
using System.Configuration;
using System.Data;
using System.Linq;
using System.Windows;
using Microsoft.Research.Kinect;

namespace KinectGait
{
    /// <summary>
    /// Interaction logic for App.xaml
    /// </summary>
    public partial class App : Application
    {
        
    }

    public class classePublica{
        private int _teste = 200;
        
        public classePublica(){}

        public int GetTeste() {
            return _teste;
        }

        public void SetTeste(int TesteVal) { 
            _teste = TesteVal;
        }
    }

 // static class Individuo
    static class Person 
    {
        //private static string individuo;
        //private static int contador_de_arquivos;
        private static string person;
        private static int file_counter;

        //public static void SetNovoIndividuo(string name) {
        public static void SetNewPerson(string name)
        {
            person = name;
        }

        //public static string GetIndividuo() {
        public static string GetPerson()
        {
            return person;
        }

        //public static int SetContadorArquivos(int valor)
        public static int SetFileCounter(int value)
        {
            file_counter = value;
            return file_counter;
        }

        //public static int GetContadorArquivos()
        public static int GetFileCounter()
        {
            return file_counter;
        }
    }

//    public class ListaPontos 
    public class PointList
    { 
        private List<string> pointList = new List<string>();

        public PointList() { }

        public void SetPointList(string key, float[] points) {
            string capturedPoint = string.Join(";", points);
            string line = key + ";" + capturedPoint;
            
            pointList.Add(line);
        }

        public List<string> GetPointList() {
            return pointList;
        }

        public void ClearList(){
            pointList.Clear();
        }

        public string capturedPoint { get; set; }
    }

 // public class CriaDiretorio
    public class CreateDirectory
    {
        public CreateDirectory() { }

        public int createDirectory(string name) 
        {
            try
            {
                if (!Directory.Exists(name))
                {
                    System.IO.Directory.CreateDirectory(name);
                    return 0 + 1;
                }
                else
                {
                    System.IO.DirectoryInfo dirInfo = new System.IO.DirectoryInfo(name);
                    int count = dirInfo.GetFiles().Length;
                    return count + 1;
                }
            }
            catch (System.IO.IOException e)
            {
                MessageBox.Show(e.Message);
                return 0;
            }
        }    
    }

//    public class ArquivoPontos
    public class PointsFile
    {
        private TextWriter textWriter;

        public PointsFile() { }

        public void SavePoints(string name, List<string> list_of_points) 
        {

            string fileName = name + ".txt";
            string directory = Person.GetPerson();
            string pathDOS = Path.Combine(directory, fileName);
            
            try
            {
                textWriter = new StreamWriter(pathDOS);

                foreach (string line in list_of_points)
                    textWriter.WriteLine(line);

                textWriter.Close();

                //MessageBox.Show("Arquivo de captura salvo com sucesso!");
                MessageBox.Show("Captured walk file saved");
            }
            catch (System.IO.IOException e)
            {
                MessageBox.Show(e.Message);
            }
           
        }

    }
    
}
