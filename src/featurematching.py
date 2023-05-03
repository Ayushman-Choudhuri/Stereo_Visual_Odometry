import cv2
import matplotlib.pyplot as plt

def extract_features(image , detector_algo = 'sift' , mask = None): 

    if detector_algo == 'sift':
        det = cv2.SIFT_create()
    elif detector_algo == 'orb':
        det = cv2.ORB_create()
    elif detector_algo == 'surf':
        det = cv2.xfeatures2d.SURF_create()
    else : print("Please enter the correct feature extraction algorithm")
        
    keypoints, descriptors = det.detectAndCompute(image, mask)
    
    return keypoints, descriptors

def match_features(des1, des2, matching='BF', detector='sift', sort=True, k=2):

    if matching == 'BF':
        if detector == 'sift':
            matcher = cv2.BFMatcher_create(cv2.NORM_L2, crossCheck=False)
        elif detector == 'orb':
            matcher = cv2.BFMatcher_create(cv2.NORM_HAMMING2, crossCheck=False)
        matches = matcher.knnMatch(des1, des2, k=k)

        
    elif matching == 'FLANN':
        FLANN_INDEX_KDTREE = 1
        index_params = dict(algorithm = FLANN_INDEX_KDTREE, trees=5)
        search_params = dict(checks=50)
        matcher = cv2.FlannBasedMatcher(index_params, search_params)
        matches = matcher.knnMatch(des1, des2, k=k)
    
    if sort:
        matches = sorted(matches, key = lambda x:x[0].distance)

    return matches

def visualize_matches(image1, kp1, image2, kp2, match):

    image_matches = cv2.drawMatches(image1, kp1, image2, kp2, match, None, flags=2)
    plt.figure(figsize=(16, 6), dpi=100)
    plt.imshow(image_matches)