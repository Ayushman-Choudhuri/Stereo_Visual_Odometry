# Stereo_Visual_Odometry
This repository contains an implementation of stereo visual odometry using images from the KITTI Odometry dataset. This project uses stereo depth estimation using the open-cv python package. The motion is estimated by reconstructing the 3D position of matched keypoints in one frame using the estimated stereo depth map and estimating the pose of the camera in the next frame using thesolvePnPRansac() function.It will then use this framework to compare performance of different combinations of stereo matchers, feature matchers, distance thresholds for filtering feature matches, and use of lidar correction of stereo depth estimation.

# Dependencies 


# Directory Structure
``` bash
.
├── dataset
│   ├── data_odometry_calib
│   ├── data_odometry_gray
│   ├── data_odometry_poses
│   └── data_odometry_velodyne
├── Images
├── README.md
└── Stereo Visual Odometry.ipynb
```

# Runnning the Project 


# Future Work



