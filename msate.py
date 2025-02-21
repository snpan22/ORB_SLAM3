import numpy as np
import pandas as pd
import os
import sys
from scipy.interpolate import interp1d

slam_file_tum = input("Enter name of .tum file: ")
if not os.path.isfile(slam_file_tum):
    print(f"Error: The file '{slam_file_tum}' was not found.")
    sys.exit()
gt_file = input("Enter path to ground truth file: ")
if not os.path.isfile(gt_file):
    print(f"Error: The  file '{gt_file}' was not found.")
    sys.exit()

data = np.loadtxt(slam_file_tum)
data[:, 0] *= 1e9
df = pd.DataFrame(data, columns=["timestamp", "x", "y", "z", "qx", "qy", "qz", "qw"])

gt_data = np.loadtxt(gt_file, delimiter = ',', skiprows=1)
gt_t, gt_xyz = gt_data[:, 0], gt_data[:, 1:4]  # Extract timestamps and positions
slam_t = df["timestamp"]

if np.max(gt_t) > 1e12:
    gt_t /= 1e9
if np.max(slam_t) > 1e12:
    slam_t /= 1e9

interp_x = interp1d(gt_t, gt_xyz[:, 0], kind='linear', fill_value="extrapolate")
interp_y = interp1d(gt_t, gt_xyz[:, 1], kind='linear', fill_value="extrapolate")
interp_z = interp1d(gt_t, gt_xyz[:, 2], kind='linear', fill_value="extrapolate")

gtx = interp_x(slam_t)
gty = interp_y(slam_t)
gtz = interp_z(slam_t)

slamx = df["x"]
slamy = df["y"]
slamz = df["z"]

gtxyz = np.column_stack([gtx, gty, gtz])
sxyz = np.column_stack([slamx, slamy, slamz])
msate = np.mean(np.linalg.norm(sxyz - gtxyz, axis = 1)**2)
print("Mean Squared Absolute Trajectory error (m^2): ", msate)