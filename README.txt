Data for student lab, fall 2023. Data was acquired at model basin facility at Valgrinda.

Overview: the data set includes wave probe data, as well as Schlieren data of free surface gradients. Data is in the format of .mat files from MATLAB.
The data set includes one case w/columns, and one w/o.

Parameters:
wave period: 0.46 s
target wave steepness: 0.02 (wave height / wavelength)
water depth: 0.475 m

column dimensions (when present): 70 mm diameter, 0.833 center-center-spacing (6 total spanning width of basin)

x-axis: along the direction of the incident waves (positive is toward to beach)
y-axis: cross-wave direction

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
./wave_probe_data

both files contain the following variables:
T: wave period in seconds
steepness: target wave steepness in (wave height / wavelength)
t: list of time values
value: structure of data channels as follows:

-flap: wavemaker flap position in motor angle
-flapCtl: wavemaker command position
-wp_xx: wave probes
-ultraSonic: ultrasonic probe in mounted in the vicinity of the wave probes.
camera_trig: trigger signal of the camera (disregard)

wave probe positions are 

WP#      1	2	3	4	5	6	7	8
x [m]	0.42	0.537	1.473	0.88	1.707	1.02	1.02	1.02
y [m]	-1.1	-1.1	-1.1	-1.1	-1.1	-0.5	0	0.5


%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
Schlieren data
each file contains a time series 5 periods long of gradient fields recorded by the camera. The framerate of the camera was 50 Hz, such that the temporal spacing between each image is 0.02 s.
The gradient fields are unitless i.e. [meters/meter]. 

fsss_firstWaves.mat: a representive window when the first waves produced by the wavemaker pass by the camera (before any reflections)
fsss_afterNoColumns.mat: after the incident wave train has passed by w/o columns, only reflected waves and tranverse sloshing modes are present
fsss_afterColumns.mat: same as above but for the case of columns mounted on the beach. The time window here is approximately the same as above relative to the wave train.

Each file contains the following variables:
gradX: free surface gradient component in the x-direction. size is [nx,ny,nt] where nx and ny are spatial dimensions, and nt is the frame number
gradY: free surface gradient component in the y-direction
x - list of x-coordinates in [m] along the first dimension (i.e. rows) of the images. Number of elements in x is the same as the first dimension of gradX/Y
y - list of y-coordinates in [m] along the second dimension (i.e. columns) of the images. Number of elements in x is the same as the second dimension of gradX/Y


