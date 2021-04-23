from scipy.misc import imread, imresize
import matplotlib.pyplot as plt
f = r"C:\Users\Public\Pictures\Sample Pictures\Lighthouse.jpg"
img = imread(f)[:, :, 0]
fig, (ax1, ax2, ax3) = plt.subplots(1, 3, figsize=(8, 2.5))
ax1.imshow(img)
ax1.set_title('Original')
ax1.axis('off')

thresh = 100
ax2.hist(img)
ax2.set_title('Histogram')
ax2.axvline(x=thresh, color='r', linestyle='dashed', linewidth=2)

ax3.imshow(img, cmap=plt.cm.gray)
ax3.set_title('Thresholded')
ax3.axis('off')

plt.show()
