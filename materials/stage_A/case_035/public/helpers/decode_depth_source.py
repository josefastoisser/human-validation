import cv2
import numpy as np
import matplotlib.pyplot as plt

""" This function takes an input as either the filepath to the depth map 
    or the actual depth map image read via cv2

    Params:
    rgb_depth: Filepath or cv2 image of the RGB depth map. If the depth map
    is attached to the video frame, input only the depth map RGB.

    Output:
    depth: The pixel wise depth values in meters
"""
def decode_depth(rgb_depth) -> np.ndarray:
    if isinstance(rgb_depth, str):
        # Load the RGB depth image from the file
        rgb_depth_data = cv2.imread(rgb_depth)
    else:
        # Use the provided RGB depth image
        rgb_depth_data = rgb_depth

    # Convert RGB to HSV
    hsv_depth = cv2.cvtColor(rgb_depth_data, cv2.COLOR_BGR2HSV) / 255.

    # Decoding HSV to depth values
    depth = hsv_depth[:, :, 0] * 3  # Extracting hue and scaling to 0-3 meters range
    return depth


if __name__ == "__main__":

    # Example RGB depth data (replace this with your actual data)
    rgb_depth_data = cv2.imread("out.png")
    _, w, _ = rgb_depth_data.shape

    # If the depth map is attached to the video frame, extract only the depth map
    depth_map = rgb_depth_data[:, :int(w/2), :]

    # Decoding depth
    depth_values = decode_depth(depth_map)

    # Example output
    print("Depth values in meters:")
    print(depth_values)

    #note that there can be noise in the depth values, please make sure you filter them
    plt.imshow(depth_values)
    plt.show()

