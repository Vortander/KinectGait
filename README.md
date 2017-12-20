# KinectGait
Anthropometric and Gait Data from Kinect Sensor.

DESCRIPTION 

This dataset contains raw data from 164 subjects extracted using a Kinect sensor. 
Each subject walked at least once over a semi-circular path and the sensor followed the movement using a spinning dish. 
All walks were performed indoors with artificial lighting, but lighting conditions were not controlled. 

Folders contain all walks for each subject. Each text file is composed of several frames. Each frame contains (x,y,z) coordinates for several points extracted using the sensor' SDK, starting with the Head. Frames are presented in sequence, without a proper separator - i.e. at each occurrence of Head, a new frame starts. 

The number of walks varies across subjects and the number of frames varies across walks. 

## HOW TO CITE 
To cite this dataset, use:

ANDERSSON, Virginia O.; ARAUJO, Ricardo M. Person Identification Using Anthropometric and Gait Data from Kinect Sensor. In: Proceedings of the 29th AAAI Conference. 2015.

@inproceedings{andersson2015person,
  title={Person Identification Using Anthropometric and Gait Data from Kinect Sensor.},
  author={Andersson, Virginia Ortiz and de Ara{\'u}jo, Ricardo Matsumura},
  booktitle={AAAI},
  pages={425--431},
  year={2015}
}



## DISCLAIMER: 
If the use of this API is intended for publishing purposes and academic papers, please cite as above mentioned and provide the link from this repository as reference. 
THIS MATERIAL IS PROVIDED AS IS, WITH ABSOLUTELY NO WARRANTY EXPRESSED OR IMPLIED! ANY USE IS AT YOUR OWN RISK!
