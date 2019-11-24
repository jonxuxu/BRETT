# Import dependencies
import numpy as numpy
import argparse
import imutils
import cv2

# Add input arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", type=str,
                required=True, help="path to real image")
ap.add_argument("-h", "--heatmap", type=str,
                required=True, help="path to heat map"
                )
ap.add_argument("-a", "--alpha", type=float, required=True,
                help="the alpha value for the image, from [0.0, 1.0]")
args = vars(ap.parse_args())

# Load images
print("Loading image and heatmap...")
image = cv2.imread(args["image"])
heatmap = cv2.imread(args["heatmap"])
alpha = float(args["alpha"])

beta = 1.0 - alpha

# Blend images
print("Blending images...")
merged = cv2.addWeighted(image, alpha, heatmap, beta, 0.0)

# Display and save image
cv2.imwrite("merged.png", merged)
cv2.imshow("Merged", merged)
cv2.waitKey(0)
