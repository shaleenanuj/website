import numpy as np
import matplotlib.pyplot as plt
np.random.seed(6789)
x = np.random.gamma(4, 0.5, 1000)
result = plt.hist(x, bins=20, color='c', edgecolor='k', alpha=0.65)
plt.axvline(x.mean(), color='k', linestyle='dashed', linewidth=1)

_, max_ = plt.ylim()
plt.text(x.mean() + x.mean()/10, 
         max_ - max_/10, 
         'Mean: {:.2f}'.format(x.mean()))
