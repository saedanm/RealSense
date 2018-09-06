import numpy as np
import Queue

class realsense_image(object):
    def __init__(self, depth_image, color_image):
        self.depth = depth_image
        self.color = color_image

q = Queue.Queue(2)

dept_image = np.zeros((4,4), dtype=int)
color_image = np.zeros((4,4,3), dtype=int)
image = realsense_image(dept_image, color_image)
q.put(image)


dept_image = np.ones((4,4), dtype=int)
color_image = np.ones((4,4,3), dtype=int)
image = realsense_image(dept_image, color_image)
q.put(image)

image1 = q.get_nowait()
print(image1.depth)

image1 = q.get_nowait()
print(image1.depth)

image1 = q.get_nowait()
print(image1.depth)
