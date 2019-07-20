using System;
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


    public class dicionarioPontos { 
        private Dictionary<string, int[,,]> pontosDic = new Dictionary<string, int[,,]>();

        public dicionarioPontos() { }

        public void SetPontosDic(string chave, int[,,] pontos) {
            pontosDic.Add(chave, pontos);
        }

        public int[,,] GetPontosDic(string chave) {
            return pontosDic[chave];
        }
	}
    
}
