#Algorithm to use RealSense D435 to extract person from background

from threading import Thread
import pyrealsense2 as rs
import numpy as np
import cv2
import time


#start __main__
# Configure depth and color streams
pipeline = rs.pipeline()
config = rs.config()
config.enable_stream(rs.stream.depth, 640, 480, rs.format.z16, 15)
config.enable_stream(rs.stream.color, 640, 480, rs.format.bgr8, 15)

# Start streaming
profile = pipeline.start(config)


# Getting the depth sensor's depth scale (see rs-align example for explanation)
depth_sensor = profile.get_device().first_depth_sensor()
depth_scale = depth_sensor.get_depth_scale()
print("Depth Scale is: " , depth_scale)

# Create an align object
# rs.align allows us to perform alignment of depth frames to others frames
# The "align_to" is the stream type to which we plan to align depth frames.
align_to = rs.stream.color
align = rs.align(align_to)

prv_time = time.time()

#Start the thread to read frames from the video stream
iscapture = True
realsense_capture_thread = Thread(target=RealSenseCapture, args=(iscapture,))
realsense_capture_thread.start()

#---------------------------------------------------------------------------------------
#end __main__


def ProcessDepthGrayscale():
    


def RealSenseCapture(iscapture):
	try:
		while iscapture:
			# Wait for a coherent pair of frames: depth and color
			frames = pipeline.wait_for_frames()

			# Align the depth frame to color frame
			aligned_frames = align.process(frames)

			# Get aligned frames
			depth_frame = aligned_frames.get_depth_frame().as_depth_frame() # aligned_depth_frame is a 640x480 depth image
			color_frame = aligned_frames.get_color_frame()

			if not depth_frame or not color_frame:
				continue

			# Convert images to numpy arrays
			depth_image = np.asanyarray(depth_frame.get_data())
			color_image = np.asanyarray(color_frame.get_data())
	finally:
    	# Stop streaming
    	pipeline.stop()

	print("RealSense capture closed...")
