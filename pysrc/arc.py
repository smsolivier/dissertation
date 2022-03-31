#!/usr/bin/env python3

import numpy as np
import matplotlib.pyplot as plt

T = 45
R = 1 
dr = 1

theta = np.linspace(np.pi/2+T*np.pi/180, np.pi/2-T*np.pi/180, 4)
r = np.linspace(R, R+dr, 3)
x = np.outer(r, np.cos(theta))
y = np.outer(r, np.sin(theta))
for i in range(len(r)):
	s = r'\draw '
	for j in range(len(theta)):
		s += '({},{}) '.format(x[i,j], y[i,j])
		if (j<len(theta)-1):
			s += '-- '
		else:
			s += ';'
	print(s) 
for i in range(len(theta)):
	print('\\draw ({},{}) -- ({},{});'.format(x[0,i], y[0,i], x[-1,i], y[-1,i]))

i = 1
j = 1
print('\\draw ({},{}) -- ({},{});'.format(
	(x[i,j] + x[i+1,j])/2,
	(y[i,j] + y[i+1,j])/2, 
	(x[i,j+1] + x[i+1,j+1])/2,
	(y[i,j+1] + y[i+1,j+1])/2
	)
)
i = 0
j = 2
print('\\draw ({},{}) -- ({},{});'.format(
	(x[i,j] + x[i,j+1])/2,
	(y[i,j] + y[i,j+1])/2, 
	(x[i+1,j] + x[i+	1,j+1])/2,
	(y[i+1,j] + y[i+	1,j+1])/2
	)
)


for radius in r: 
	plt.plot(radius*np.cos(theta), radius*np.sin(theta))
plt.xlim([-2,2])
plt.ylim([-2,2])
plt.show()