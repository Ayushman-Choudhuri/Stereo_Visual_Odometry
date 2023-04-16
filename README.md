# Stereo_Visual_Odometry
This repository contains an implementation of stereo visual odometry using images from the KITTI Odometry dataset. This project uses stereo depth estimation using the open-cv python package. The motion is estimated by reconstructing the 3D position of matched keypoints in one frame using the estimated stereo depth map and estimating the pose of the camera in the next frame using thesolvePnPRansac() function.It will then use this framework to compare performance of different combinations of stereo matchers, feature matchers, distance thresholds for filtering feature matches, and use of lidar correction of stereo depth estimation.

# Dependencies 
The list of dependencies for the project can be found on the [environment.yml](environment.yml) file 

To recreate the environment used to develop this project, you can create a conda environment using the environment.yml file provided:
``` bash
conda env create -f environment.yml
```

This will create a new environment named stereo-visual-odometry-env with all the necessary packages installed. You can then activate the environment using the following command:

``` bash
conda activate stereo-visual-odometry-env
```

Once the environment is activated, you can run the project and use the packages listed above.

# Directory Structure
``` bash
.
├── dataset
│   ├── data_odometry_calib
│   ├── data_odometry_gray
│   ├── data_odometry_poses
│   └── data_odometry_velodyne
├── environment.yml
├── Images
├── README.md
└── Stereo Visual Odometry.ipynb

```

# Runnning the Project 


# Future Work



