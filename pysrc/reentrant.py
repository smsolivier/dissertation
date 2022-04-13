#!/usr/bin/env python3

import numpy as np
import matplotlib.pyplot as plt
from OutputCycler import * 
from trans2d import * 
import cycler 

oc = OutputCycler()

N = 2
p = 3
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
plt.figure()
for e in range(mesh.Ne):
	trans = mesh.trans[e]
	c = trans.Centroid()
	plt.annotate('$K_' + str(e+1) + '$', xy=(c[0],c[1]), fontsize=20, 
		horizontalalignment='center', verticalalignment='center')
	xi = np.linspace(-1,1,100)
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
start = (.015,.575)
end = (.45,.625)
Omega = np.zeros(2)
Omega[0] = end[0] - start[0] 
Omega[1] = end[1] - start[1] 
Omega /= np.linalg.norm(Omega) 
plt.annotate(r'$\boldsymbol{\mathrm{\Omega}}$', xy=start, xytext=end, xycoords='data', textcoords='data',
	arrowprops=dict(facecolor='black', arrowstyle='<|-', lw=1.5), fontsize=20)
plt.axis('off')
if (oc.Good()):
	plt.savefig(oc.Get())

plt.figure()
trans = mesh.trans[2] 
c = trans.Centroid()
plt.annotate(r'$\boldsymbol{\mathrm{\Omega}}$', xy=start, xytext=end, xycoords='data', textcoords='data',
	arrowprops=dict(facecolor='black', arrowstyle='<|-', lw=1.5), fontsize=20, zorder=0)
plt.annotate('$K_' + str(trans.ElNo+1) + '$', xy=(c[0],c[1]), fontsize=20, 
	horizontalalignment='center', verticalalignment='center')
xi = np.linspace(-1,1,100)
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
face = FaceTrans(trans.box[:(p+1)])

# root find Omega.nor = 0 with Newton
sw = 0 
OmegaR = np.array([Omega[1], -Omega[0]])
for i in range(25):
	H = face.H(sw) 
	nor = face.Normal(sw) 
	sw -= 1./OmegaR@H*(Omega@nor)

xi = np.linspace(-1,1,13)
xi1 = xi[np.argwhere(xi>sw)[:,0]]
xi2 = xi[np.argwhere(xi<=sw)[:,0]]
Odotn = r'\boldsymbol{\mathrm{\Omega}}\cdot \boldsymbol{\mathrm{n}}'
group = [{'xi': xi2, 'color': '#1f77b4'}, {'xi': xi1, 'color': '#ff7f0e'}]
for g in group:
	xi = g['xi']
	Xs = np.zeros((len(xi), 2))
	nors = np.zeros((len(xi), 2))
	for i in range(len(xi)):
		X = face.Transform(xi[i])
		nor = face.Normal(xi[i]) 
		Xs[i,:] = X 
		nors[i,:] = nor/np.linalg.norm(nor)
	if (nors[0,:]@Omega > 0):
		label = '$' + Odotn + '> 0$'
	else:
		label = '$' + Odotn + '< 0$'
	plt.quiver(Xs[:,0], Xs[:,1], nors[:,0], nors[:,1], clip_on=True, label=label, color=g['color'])
plt.axis('off')
plt.ylim(.4,1.05)
plt.legend(bbox_to_anchor=(.7,0), loc='lower left')
if (oc.Good()):
	plt.savefig(oc.Get())

xi = np.linspace(-1,1,100)
dot = np.zeros(len(xi))
upw = np.zeros(len(xi))
dnw = np.zeros(len(xi))
for i in range(len(xi)):
	nor = face.Normal(xi[i])
	dot[i] = np.dot(Omega, nor)
	upw[i] = .5*(dot[i] + abs(dot[i]))
	dnw[i] = .5*(dot[i] - abs(dot[i]))
mx = np.max(dot)
mn = np.min(dot) 
plt.figure()
plt.plot(.5*xi+.5, dot)
plt.xlabel(r'$\xi$')
plt.ylabel(r'$\boldsymbol{\mathrm{\Omega}}\cdot\boldsymbol{\mathrm{n}}$')
if (oc.Good()):
	plt.savefig(oc.Get())

plt.figure()
plt.plot(.5*xi+.5, upw)
plt.xlabel(r'$\xi$')
plt.ylabel(r'$\frac{1}{2}\boldsymbol{\mathrm{\Omega}}\cdot\boldsymbol{\mathrm{n}} + \frac{1}{2}|\boldsymbol{\mathrm{\Omega}}\cdot\boldsymbol{\mathrm{n}}|$')
if (oc.Good()):
	plt.savefig(oc.Get())

plt.figure()
plt.plot(.5*xi+.5, dnw) 
plt.xlabel(r'$\xi$')
plt.ylabel(r'$\frac{1}{2}\boldsymbol{\mathrm{\Omega}}\cdot\boldsymbol{\mathrm{n}} - \frac{1}{2}|\boldsymbol{\mathrm{\Omega}}\cdot\boldsymbol{\mathrm{n}}|$')
plt.xlabel(r'$\xi$')
if (oc.Good()):
	plt.savefig(oc.Get())
else:
	plt.show()