import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

# img RGB
img = mpimg.imread('/butta/a.jpg')
imgplot = plt.imshow(img)
plt.title('The original image')
plt.show()
print("Original: {}".format(img.shape))

# separating channels
red_channel = img[:,:,0]
print("Red: {}".format(red_channel.shape))
green_channel = img[:,:,1]
blue_channel = img[:,:,2]
plt.imshow(red_channel,cmap='hot')
plt.title('RED channel')
plt.show()
plt.imshow(green_channel,cmap='summer')
plt.title('GREEN channel')
plt.show()
plt.imshow(blue_channel,cmap='winter')
plt.title('BLUE channel')
plt.show()

# stacking 3 channels:
three_stacked_img = np.hstack((red_channel,green_channel,blue_channel))
plt.imshow(three_stacked_img,cmap='gray')
plt.title('RED, GREEN and BLUE channels compared')
plt.show()

# merging channels RGB -> BRG
new_img = np.zeros(tuple(img.shape),dtype=int)
print("New image shape {}".format(new_img.shape))
new_img[:,:,0] = blue_channel
new_img[:,:,1] = red_channel
new_img[:,:,2] = green_channel
imgplot = plt.imshow(new_img)
plt.title('The image with channels swiched')
plt.show()

