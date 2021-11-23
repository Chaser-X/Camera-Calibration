# Camera-Calibration
About the single,mutiply and stereo camera system calibration and implement with opencv in python.
### 1.Pinhole Camera Model
### Summary  
Camera calibration total include 16 parameters:  
Only camera related: 10 instric parameters:  
Camera to pixel: f,dx,dy,Xc,Yc; Distortion: radial(k1,k2,k3), tangential(p1,p2).  
Camera Pose in world coordination:  
Rotation: Rx,Ry,Rz;  
Translation: Tx,Ty,Tz;
