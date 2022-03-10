#!/usr/bin/env python3

import numpy as np
import matplotlib.pyplot as plt

from trans2d import * 
from OutputCycler import * 
oc = OutputCycler()

p = 2 
x = np.linspace(0,2,2*p+1)
y = np.linspace(0,1,p+1)
X,Y = np.meshgrid(x,y) 
nodes = np.array([X.flatten(), Y.flatten()]).transpose()

nodes[1,1] += .1 
nodes[2,1] += .135
nodes[3,1] += .1 
nodes[11,1] += .1 
nodes[12,1] += .135
nodes[13,1] += .1 
nodes[7,0] += .1
nodes[7,1] += .135
nodes[6,1] += .1 
nodes[6,0] += .1
nodes[8,1] += .1
nodes[8,0] += .1  
nodes[5,0] += .1 
nodes[9,0] += .1 

theta = 5*np.pi/180 
R = np.array([[np.cos(theta), -np.sin(theta)], [np.sin(theta), np.cos(theta)]])
nodes = nodes@R.T

ele = [] 
for e in range(2):
	loc = [e*p, e*p+1, e*p+2, 
		2*p+1+e*p, 2*p+2+e*p, 2*p+3+e*p,
		2*(2*p+1)+e*p, 2*(2*p+1)+e*p+1, 2*(2*p+1)+e*p+2]
	ele.append(loc)

mesh = AbstractMesh(nodes, np.array(ele), 2)

sz = 9
# color = '#003262'
color = 'k'

trans = mesh.trans[0]
plt.figure()
xi = np.linspace(-1,1)
x = np.zeros((len(xi), 2))
for i in range(len(xi)):
	x[i,:] = trans.Transform(np.array([-1,xi[i]]))
plt.plot(x[:,0], x[:,1], 'k')
for i in range(len(xi)):
	x[i,:] = trans.Transform(np.array([1,xi[i]]))
plt.plot(x[:,0], x[:,1], 'k')
for i in range(len(xi)):
	x[i,:] = trans.Transform(np.array([xi[i],-1]))
plt.plot(x[:,0], x[:,1], 'k')
for i in range(len(xi)):
	x[i,:] = trans.Transform(np.array([xi[i],1]))
plt.plot(x[:,0], x[:,1], 'k')
trans = mesh.trans[1]
for i in range(len(xi)):
	x[i,:] = trans.Transform(np.array([1,xi[i]]))
plt.plot(x[:,0], x[:,1], 'k')
for i in range(len(xi)):
	x[i,:] = trans.Transform(np.array([xi[i],-1]))
plt.plot(x[:,0], x[:,1], 'k')
for i in range(len(xi)):
	x[i,:] = trans.Transform(np.array([xi[i],1]))
plt.plot(x[:,0], x[:,1], 'k')
for i in range(nodes.shape[0]):
	plt.plot(nodes[i,0], nodes[i,1], 'o', color=color, markersize=sz)
	plt.annotate(str(i), xy=(nodes[i,0]-.075, nodes[i,1]-.075), 
		verticalalignment='bottom', horizontalalignment='left', usetex=False)

plt.axis('off')
plt.xlim(np.min(nodes[:,0])-.1,np.max(nodes[:,0])+.1)
plt.ylim(np.min(nodes[:,1])-.1,np.max(nodes[:,1])+.1)

if (oc.Good()):
	plt.savefig(oc.Get())
else:
	plt.show()