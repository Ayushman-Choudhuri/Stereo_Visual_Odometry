import numpy as np
import cv2

class Dataset_Handler():

    def __init__(self , sequence , lidar_data_option = False ):


        # If LIDAR data is being supplied to the odometry function , set lidar_data to True else set it to False
        
        self.lidar_data_option = lidar_data_option

        #Set paths to the image sequence directory, the ground truth directory , sensor calibration data directory
        self.img_seq_dir = './dataset/data_odometry_gray/dataset/sequences/{}/'.format(sequence) #File path to image sequence folder
        self.gt_poses_dir = './dataset/data_odometry_poses/dataset/poses/{}.txt'.format(sequence) #File path to ground truth poses
        self.calib_data_dir = './dataset/data_odometry_calib/dataset/sequences/{}'.format(sequence) #File path to camera calibration data
        

        #Files to iterate through 
        self.left_camera_image_files = sorted(os.listdir(self.img_seq_dir +'image_0'))
        self.right_camera_image_files = sorted(os.listdir(self.img_seq_dir +'image_1'))

        #################################### check ####################################
        if self.lidar_data_option :
            self.velodyne_files = os.listdir(self.seq_dir + 'velodyne')
            self.lidar_path = self.seq_dir + 'velodyne/'
        ###############################################################################


        # Extract Sensor Calibration Parameters
        # P0,P1 - greyscale cameras , P2,P3 - RGB Cameras , Tr - Transformation matrix of Velodyne LIDAR
        sensor_calib_data = pd.read_csv(self.calib_data_dir + '/calib.txt', delimiter=' ', header = None , index_col=0)
        
        self.P0 = np.array(sensor_calib_data.loc['P0:']).reshape((3,4))
        self.P1 = np.array(sensor_calib_data.loc['P1:']).reshape((3,4))
        self.P2 = np.array(sensor_calib_data.loc['P2:']).reshape((3,4))
        self.P3 = np.array(sensor_calib_data.loc['P3:']).reshape((3,4))  
        self.Tr = np.array(sensor_calib_data.loc['Tr:']).reshape((3,4))

        #Extract ground truth poses
        gt_poses = pd.read_csv(self.gt_poses_dir , delimiter=' ' , header = None)
        self.gt = np.zeros((len(gt_poses) , 3,4))

        for i in range(len(gt_poses)): 
            self.gt[i] = np.array(gt_poses.iloc[i]).reshape((3,4))

        #Extract image timestamps
        self.time_stamps = np.array(pd.read_csv(self.calib_data_dir + '/times.txt' , delimiter = ' ' , header = None ))

        #Load Image and LIDAR Data

        self.reset_generator()

        self.first_image_left = cv2.imread(self.img_seq_dir + 'image_0/' + self.left_camera_image_files[0],0)
        self.first_image_right= cv2.imread(self.img_seq_dir + 'image_1/' + self.right_camera_image_files[0],0)
        self.second_image_left= cv2.imread(self.img_seq_dir + 'image_0/' + self.left_camera_image_files[1],0)

        #################### Optional : Load LIDAR Data #################################

        ######################################################################

        self.imheight = self.first_image_left.shape[0]
        self.imwidth = self.first_image_left.shape[1]
        
    def reset_generator(self):

        self.images_left = (cv2.imread(self.img_seq_dir + 'image_0/' + name_left , 0)
                            for name_left in self.left_camera_image_files)
        self.images_left = (cv2.imread(self.img_seq_dir + 'image_1/' + name_right , 0)
                            for name_right in self.left_camera_image_files)
        
        ########################## Optional: Reset LIDAR generator #########################

        pass