import cv2
import datetime


def compute_left_disparity_map(left_image , right_image , match_algo = 'bm' , rgb = False , verbose = False):

    sad_window = 6 # sum of absolute differences window
    num_disp =  sad_window*16
    block_size = 11

    if match_algo == 'bm':

        matcher = cv2.StereoBM_create(numDisparities=num_disp , blockSize= block_size)

    elif match_algo == 'sgbm':
        
        matcher = cv2.StereoSGBM_create(numDisparities=num_disp, 
                                        minDisparity=0,
                                        blockSize=block_size,
                                        P1 = 8*3*sad_window**2,
                                        P2 = 32*3*sad_window**2,
                                        mode = cv2.STEREO_SGBM_MODE_SGBM_3WAY
                                        )
        
    if rgb:
        left_image = cv2.cvtColor(left_image, cv2.COLOR_BGR2GRAY)
        right_image = cv2.cvtColor(right_image, cv2.COLOR_BGR2GRAY)

    start = datetime.datetime.now()
    disparity_left = matcher.compute(left_image, right_image).astype(np.float32)/16
    end = datetime.datetime.now()
    if verbose:
        print(f'Time to compute disparity map using Stereo{match_algo.upper()}:', end-start)

    return disparity_left


def decompose_projection_matrix(p):

    k, r, t, _,_,_,_ = cv2.decomposeProjectionMatrix(p)
    t = (t / t[3])[:3]

    return k, r, t


def calc_depth_map(disp_left, k_left, t_left, t_right, rectified=True):

    # Get focal length of x axis for left camera
    f = k_left[0][0]

    # Calculate baseline of stereo pair
    if rectified:
        b = t_right[0] - t_left[0] 
    else:
        b = t_left[0] - t_right[0]
        
    # Avoid instability and division by zero
    disp_left[disp_left == 0.0] = 0.1
    disp_left[disp_left == -1.0] = 0.1

    # Make empty depth map then fill with depth
    depth_map = np.ones(disp_left.shape)
    depth_map = f * b / disp_left

    return depth_map

def stereo_to_depth(left_image , right_image , P0 , P1 , matcher = 'bm' , rgb=False , verbose = False, rectified = True ):

    #Compute Disparity Map
    disp_map = compute_left_disparity_map(left_image , 
                                            right_image ,
                                            match_algo = matcher , 
                                            rgb=rgb , 
                                            verbose=verbose)

    # Decompose Projection Matrix
    k_left , r_left , t_left = decompose_projection_matrix(P0)
    k_right , r_right , t_right = decompose_projection_matrix(P1)

    # Calculate depth map of left camera image
    depth_map = calc_depth_map(disp_map , k_left , t_left , t_right)

    return depth_map