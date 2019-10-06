import matplotlib.pyplot as plt

def plotHist(ax):
    ax.hist([1,2,3,4,2,1,2])
    plt.title('hahs')
    plt.xticks()
    plt.xlabel('abc')


fig = plt.figure()
ax1 = fig.add_subplot(331)
plotHist(ax1)
ax2 = fig.add_subplot(332)
plotHist(ax2)
plt.show()

