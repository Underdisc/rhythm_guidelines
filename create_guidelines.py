# You will need these packages to use this script.
# python -m pip install -U matplotlib

import matplotlib.image as mpimg
import numpy as np
import os.path as path
import sys

# Read in the image file.
filename = sys.argv[1]
file_exists = path.exists(filename)
if not file_exists:
    sys.exit("The file " + filename + " does not exist") 
data = mpimg.imread(filename)

# Find all of the columns that bar lines will be on. 
num_bars = int(sys.argv[2])
row_length = len(data[0])
bar_delta = float(row_length) / float(num_bars)
bar_locations = []
for bar in range(1, num_bars):
    bar_locations.append(int(bar * bar_delta))

# Change the image data to display the bars.
pixel_size = len(data[0][0])
if pixel_size == 3:
    bar_color = np.array([0.0, 0.0, 0.0])
else:
    bar_color = np.array([0.0, 0.0, 0.0, 1.0])
for row in data:
    for bar_pos in bar_locations:
        row[bar_pos] = bar_color

# Write the new image file.
split_filename = filename.split('.')
output_filename = split_filename[0] + "_out." + split_filename[1]
mpimg.imsave(output_filename, data)

