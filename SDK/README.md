## Old Microsoft SDKs to work with Kinect SDK Version 1.0

### Atention!!!
#### Before downlowding any of these old installers, search it in Microsoft repository!
#### In case of no other valid alternative found, USE IT AT YOUR OWN RISK!!!

## Instructions to install Microsoft Kinect 360 

Installation prerequisites, according to Microsoft technical specifications:
1. 32-bit (x86) or 64-bit (x64) processor
2. Dual-core 2.66-GHz or faster processor
3. Dedicated USB 2.0 bus 
4. 2 GB RAM
5. A retail Kinect for Xbox 360 sensor, which includes special USB / power cabling
from: http://www.microsoft.com/en-us/kinectforwindows/develop/beta.aspx

Before you install the SDK:
1. To program with the SDK: Download and install Visual Studio Express 2010 C ++ and C #
at: http://www.visualstudio.com/en-us/downloads/download-visual-studio-vs#DownloadFamilies_2 (vc_web.exe) (vcs_web.exe)

2. .NET Framework 4.0
	at: http://www.microsoft.com/en-us/download/confirmation.aspx?id=17851 (dotNetFx40_Full_setup.exe)

Installation Instructions:

1o. Download the SDKs: KinectSDK-v1.0-beta2-x86.msi or KinectSDK-v1.0-beta2-x64.msi (for Windows 32 or 64-bit respectively)
    of the address: http://download.microsoft.com/download/F/9/9/F99791F2-D5BE-478A-B77A-830AD14950C3/KinectSDK-v1.0-beta2-x86.msi (KinectSDK-v1.0-beta2 -x86.msi)
                 http://download.microsoft.com/download/F/9/9/F99791F2-D5BE-478A-B77A-830AD14950C3/KinectSDK-v1.0-beta2-x64.msi (KinectSDK-v1.0-beta2-x64. msi)
                 address: http://www.microsoft.com/en-us/kinectforwindows/develop/beta.aspx

2nd. Click and run the chosen .msi installer with Kinect NOT PLUGED ON USB.

3rd. When you finish installing the SDK, run from the .msi file, plug the Kinect into USB and plug it into the external power supply.
    In this step, Windows will download some drivers needed to run automatically, with the status warning on the bottom right side of the taskbar.
    After the installation is complete, Kinect should already be working properly.

(Non-mandatory step) To run the samples that ship with the SDK, install the Microsoft DirectX SDK and Runtime for Microsoft DirectX 9.
                        sdk at: http://www.microsoft.com/en-us/download/details.aspx?id=6812 (DXSDK_Jun10.exe)
                        runtime: http://www.microsoft.com/en-us/download/details.aspx?id=35 (dxwebsetup.exe)

                        Note: Instructions for using speech see http://www.microsoft.com/en-us/kinectforwindows/develop/beta.aspx.

4th. Run capture .exe applications. Observe the value of fps (frames per second).