# Stereo_Visual_Odometry
![Project Status](https://img.shields.io/badge/Project%20Status-Under%20Development-green)


![Python Version](https://img.shields.io/badge/python-3.9-blue)
![Jupyter Notebook](https://img.shields.io/badge/Jupyter%20Notebook-%3E%3D5.0-orange.svg)
![Conda Version](https://img.shields.io/badge/conda-22.9.0-green.svg?style=flat-square&logo=anaconda&logoColor=white)
![OpenCV Version](https://img.shields.io/badge/OpenCV-4.6.0-blue?logo=OpenCV)
![Docker Version](https://img.shields.io/badge/docker-23.0.4-blue)






This repository contains an implementation of stereo visual odometry using images from the KITTI Odometry dataset. This project uses stereo depth estimation using the open-cv python package. 

# Dataset

You can download the following data files from the [KITTI dataset](https://www.cvlibs.net/datasets/kitti/eval_odometry.php)

* odometry_data_set(grayscale) ~ 22GB
* odometry_data_set(velodyne_laser_data) ~ 80GB
* odometry_data_set(calibration_files) ~ 1MB
* odometry_ground_truth_poses ~ 4 MB

download and place them in your data folder as shown in the directory structure section of the readme file. 

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
Stereo_Visual_Odometry
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

# Running the Project 


# Future Work



