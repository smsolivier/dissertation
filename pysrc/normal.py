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

trans = mesh.trans[0]
plt.figure()
xi = np.linspace(-1,1)
x = np.zeros((len(xi), 2))
for i in range(len(xi)):
	x[i,:] = trans.Transform(np.array([-1,xi[i]]))
plt.plot(x[:,0], x[:,1], 'k', alpha=.1)
for i in range(len(xi)):
	x[i,:] = trans.Transform(np.array([1,xi[i]]))
plt.plot(x[:,0], x[:,1], 'k')
for i in range(len(xi)):
	x[i,:] = trans.Transform(np.array([xi[i],-1]))
plt.plot(x[:,0], x[:,1], 'k', alpha=.1)
for i in range(len(xi)):
	x[i,:] = trans.Transform(np.array([xi[i],1]))
plt.plot(x[:,0], x[:,1], 'k', alpha=.1)

trans = mesh.trans[1]
for i in range(len(xi)):
	x[i,:] = trans.Transform(np.array([1,xi[i]]))
plt.plot(x[:,0], x[:,1], 'k', alpha=.1)
for i in range(len(xi)):
	x[i,:] = trans.Transform(np.array([xi[i],-1]))
plt.plot(x[:,0], x[:,1], 'k', alpha=.1)
for i in range(len(xi)):
	x[i,:] = trans.Transform(np.array([xi[i],1]))
plt.plot(x[:,0], x[:,1], 'k', alpha=.1)

for e,trans in enumerate(mesh.trans):
	c = trans.Centroid()
	plt.annotate('$K_' + str(e+1) + '$', xy=(c[0],c[1]), fontsize=20, 
		horizontalalignment='center', verticalalignment='center')

line = nodes[[2,7,12],:]
trans = FaceTrans(line)

xi = np.linspace(-1,1,5)
xic = np.zeros(len(xi)-1)
for i in range(len(xic)):
	xic[i] = (xi[i] + xi[i+1])/2
xi = xic

nors = np.zeros((len(xi),2))
tans = np.zeros((len(xi),2))
Xs = np.zeros((len(xi),2))
for i in range(len(xi)):
	Xs[i,:] = trans.Transform(xi[i])
	F = trans.F(xi[i]) 
	tans[i,:] = F/np.linalg.norm(F)
	nor = trans.Normal(xi[i]) 
	nors[i,:] = nor/np.linalg.norm(nor)

s = 0 
ip, w = quadrature.Get1D(p+1)
for i in range(len(w)):
	s += trans.Jacobian(ip[i]) * w[i] 

print('length =', s) 

plt.quiver(Xs[:,0], Xs[:,1], tans[:,0], tans[:,1], color='#1f77b4', clip_on=True, label=r'$\boldsymbol{\mathrm{t}}$')
plt.quiver(Xs[:,0], Xs[:,1], nors[:,0], nors[:,1], color='#ff7f0e', clip_on=True, label=r'$\boldsymbol{\mathrm{n}}$')
plt.legend(loc='lower right')
plt.xlabel('$x$')
plt.ylabel('$y$')
plt.axis('off')
if (oc.Good()):
	plt.savefig(oc.Get())
else:
	plt.show()