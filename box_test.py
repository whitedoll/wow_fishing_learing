# importing required libraries
import pandas as pd
import matplotlib.pyplot as plt
# %matplotlib inline
from matplotlib import patches
from PIL import Image
# read the csv file using read_csv function of pandas
train = pd.read_csv('BloodImage_00000.csv')
train.head()

# reading single image using imread function of matplotlib
# image = plt.imread('BCCD\JPEGImages\BloodImage_00000.jpg')
# plt.imshow(image)
# plt.show()

# Number of unique training images
# file_name_count = train['filename'].nunique()
# Number of classes
cell_type_count = train['class_name'].value_counts()
# print(file_name_count)
print(cell_type_count)

fig = plt.figure()

# add axes to the image
ax = fig.add_axes([0, 0, 1, 1])

# read and plot the image
image = plt.imread('BloodImage_00000.jpg')
image2 = Image.open('BloodImage_00000.jpg')
plt.imshow(image)

# aaa_test = []
# # print(train.loc['filename'].values)
# print(len(train.filename))
# for i in range(len(train.filename)):
#     if train.iloc[i, 0] == "000000000360.jpg":
#         xmin2 = train.loc[[i]].cell_type.values[0]
#         print(xmin2)

# print(aaa_test)

# aaa = 0
# if train.iloc[1, 0] == "000000000360.jpg":
#     aaa = aaa + 1
#     print(aaa)
#
# for i in ['aaa', 'bbb', 'ccc']:
#     print(i)


# print(train['filename', 'BloodImage_00000.jpg'])

print(train.shape[0])
print(image2.size[0])
print(train.loc[[0]].x1.values[0])
print(train.loc[[0]].class_name.values[0])

# iterating over the image for different objects
for i in range(train.shape[0]):
    # if train.iloc[i, 0] == "000000000360.jpg":
    # for _, row in train[train.image_names == "BloodImage_00000.jpg"].iterrows():
    x1 = train.loc[[i]].x1.values[0]
    y1 = train.loc[[i]].y1.values[0]
    w = train.loc[[i]].w.values[0]
    h = train.loc[[i]].h.values[0]

    width = w * image2.size[0]
    height = h * image2.size[1]
    centerx = x1 * image2.size[0]
    centery = y1 * image2.size[1]

    # assign different color to different classes of objects
    if str(train.loc[[i]].class_name.values[0]) == '0':
        edgecolor = 'r'
        ax.annotate('Person', xy=(x1 - 40, y1 + 20))
    elif str(train.loc[[i]].class_name.values[0]) == '1':
        edgecolor = 'b'
        ax.annotate('31', xy=(x1 - 40, y1 + 20))
    elif str(train.loc[[i]].class_name.values[0]) == '40':
        edgecolor = 'g'
        ax.annotate('40', xy=(x1 - 40, y1 + 20))

    # add bounding boxes to the image
    rect = patches.Rectangle((centerx - width/2, centery - height/2), width, height, edgecolor=edgecolor, facecolor='none')

    ax.add_patch(rect)

plt.show()

# data = pd.DataFrame()
# data['format'] = train['image_names']
#
# # as the images are in train_images folder, add train_images before the image name
# for i in range(data.shape[0]):
#     data['format'][i] = 'train_images/' + data['format'][i]
#
# # add xmin, ymin, xmax, ymax and class as per the format required
# for i in range(data.shape[0]):
#     data['format'][i] = data['format'][i] + ',' + str(train['xmin'][i]) + ',' + str(train['ymin'][i]) + ',' + \
#                         str(train['xmax'][i]) + ',' + str(train['ymax'][i]) + ',' + train['cell_type'][i]
#
# data.to_csv('annotate.txt', header=None, index=None, sep=' ')