#!/usr/bin/env python3

import numpy as np
import matplotlib.pyplot as plt
from OutputCycler import * 
from trans2d import * 

oc = OutputCycler()

N = 2
p = 2
x,y = np.meshgrid(np.linspace(0,1,N*p+1), np.linspace(0,1,N*p+1))
x = x.flatten()
y = y.flatten()

nodes = np.zeros((len(x), 2))
nodes[:,0] = x 
nodes[:,1] = y

dt = .003
sigma = .01
for n in range(125):
	for i in range(nodes.shape[0]):
		x = nodes[i,0] 
		y = nodes[i,1] 
		if (x<1e-12 or x>1-1e-12 or y<1e-12 or y>1-1e-12):
			continue 
		c1 = [1/2,1/2]
		c2 = [1/2,-1/4]
		alpha = 1
		beta = 0
		r1 = (x-c1[0])**2 + (y-c1[1])**2 
		r2 = (x-c2[0])**2 + (y-c2[1])**2 
		nodes[i,0] += dt * (2*alpha*np.exp(-r1)*(y-c1[1]) - 2*beta*np.exp(-r2)*(y-c2[1]))
		nodes[i,1] += dt * (-2*alpha*np.exp(-r1)*(x-c1[0]) + 2*beta*np.exp(-r2)*(x-c2[0]))

ele = np.zeros((N*N, (p+1)**2), dtype=int)

for i in range(N):
	for j in range(N):
		e = i*N + j 
		base = j*p + i*(N*p+1)*p
		for k in range(p+1):
			for l in range(p+1):
				ele[e,l+k*(p+1)] = base + (N*p+1)*k + l

mesh = AbstractMesh(nodes, ele, p)
for e in range(mesh.Ne):
	trans = mesh.trans[e]
	c = trans.Centroid()
	plt.annotate('$K_' + str(e+1) + '$', xy=(c[0],c[1]), fontsize=16, 
		horizontalalignment='center', verticalalignment='center')
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
plt.annotate(r'$\boldsymbol{\mathrm{\Omega}}$', xy=(.015,.55), xytext=(.475,.65), xycoords='data', textcoords='data',
	arrowprops=dict(facecolor='black', arrowstyle='<|-', lw=1.5), fontsize=20)
plt.axis('off')
if (oc.Good()):
	plt.savefig(oc.Get())
else:
	plt.show()