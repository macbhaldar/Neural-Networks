# Pooling layer in CNN
# Performing Max Pooling using keras 
import numpy as np
from keras.models import Sequential
from keras.layers import MaxPooling2D

# define input image
image = np.array([[2, 2, 7, 3],
				[9, 4, 6, 1],
				[8, 5, 2, 4],
				[3, 1, 2, 6]])
image = image.reshape(1, 4, 4, 1)

# define model containing just a single max pooling layer
model = Sequential(
	[MaxPooling2D(pool_size = 2, strides = 2)])

# generate pooled output
output = model.predict(image)

# print output image
output = np.squeeze(output)
print(output)


# Performing Average Pooling using keras 
import numpy as np
from keras.models import Sequential
from keras.layers import AveragePooling2D

# define input image
image = np.array([[2, 2, 7, 3],
				[9, 4, 6, 1],
				[8, 5, 2, 4],
				[3, 1, 2, 6]])
image = image.reshape(1, 4, 4, 1)

# define model containing just a single average pooling layer
model = Sequential(
	[AveragePooling2D(pool_size = 2, strides = 2)])

# generate pooled output
output = model.predict(image)

# print output image
output = np.squeeze(output)
print(output)


# Performing Global Pooling using keras 
import numpy as np
from keras.models import Sequential
from keras.layers import GlobalMaxPooling2D
from keras.layers import GlobalAveragePooling2D

# define input image
image = np.array([[2, 2, 7, 3],
				[9, 4, 6, 1],
				[8, 5, 2, 4],
				[3, 1, 2, 6]])
image = image.reshape(1, 4, 4, 1)

# define gm_model containing just a single global-max pooling layer
gm_model = Sequential(
	[GlobalMaxPooling2D()])

# define ga_model containing just a single global-average pooling layer
ga_model = Sequential(
	[GlobalAveragePooling2D()])

# generate pooled output
gm_output = gm_model.predict(image)
ga_output = ga_model.predict(image)

# print output image
gm_output = np.squeeze(gm_output)
ga_output = np.squeeze(ga_output)
print("gm_output: ", gm_output)
print("ga_output: ", ga_output)


# Padding_CNN
## Padding is simply a process of adding layers of zeros to our input images 
## so as to avoid the problems mentioned above.

# Types of padding in convolution layer
# Padding Full
x = [6, 2]
h = [1, 2, 5, 4]
y = np.convolve(x, h, "full")
print(y)

# Padding same :
## append zero to the left of the array and to the top of the 2D input matrix
x = [6, 2]
h = [1, 2, 5, 4]
y = np.convolve(x, h, "same")
print(y)

# Padding valid :
## reduced output matrix as the size of the output array is reduced
x = [6, 2]
h = [1, 2, 5, 4]
y = np.convolve(x, h, "valid")
print(y)
