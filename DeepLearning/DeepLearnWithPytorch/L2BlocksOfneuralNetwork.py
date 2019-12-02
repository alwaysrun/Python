

# show the point[x,y] and the linear-line
plt.plot(x,y, 'b.')
startx = x.min()
endx = x.max()
plt.plot([startx,endx], [w*startx+b, w*endx+b], 'r')
plt.show()
