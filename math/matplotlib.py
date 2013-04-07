#scientific plotting library

##install:

    #sudo pip install matplotlib

import matplotlib.pyplot as plt

##data

plt.plot([1,2,3,4])
plt.show()

plt.plot([1,2,3,4], [1,4,9,16])
plt.show()

plt.plot(1,1)
plt.plot(2,2)
plt.show()

##format

#-: lines linking points
#o: circles, no lines linking points
plt.plot([1,2,3,4], [1,4,9,16],format)

##subplots

plt.subplots('411')
plt.plot([1,1,1,1])
plt.subplots('411')
plt.plot([1,1,1,1])
plt.subplots('412')
plt.plot([2,2,2,2])
plt.subplots('421')
plt.plot([3,3,3,3])
plt.subplots('422')
plt.plot([4,4,4,4])
plt.show()

plt.subplots('411')
plt.plot([1,1,1,1])
plt.subplots('412')
plt.plot([2,2,2,2])
plt.subplots('413')
plt.plot([3,3,3,3])
plt.subplots('414')
plt.plot([4,4,4,4])
plt.show()

##labels and title
plt.xlabel('x')
plt.ylabel('y')
plt.title('title')
plt.plot([1,2,3])
