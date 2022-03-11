#!/usr/bin/env python3

import numpy as np
import matplotlib.pyplot as plt

from trans2d import * 
from OutputCycler import * 
oc = OutputCycler()

Nref = oc.GetOpt(0, 2)
X = np.array([[ 0.245812, 0.232684 ],
	[ 0.264676,  0.2035   ],
	[ 0.282858,  0.163871 ],
	[ 0.288391,  0.139162 ],
	[ 0.274662,  0.234249 ],
	[ 0.309942,  0.169385 ],
	[ 0.331345,  0.0687922],
	[ 0.326657,  0.0430286],
	[ 0.345287,  0.119349 ],
	[ 0.3604  , -0.0105357],
	[ 0.342118, -0.125317 ],
	[ 0.330021, -0.111447 ],
	[ 0.368893, -0.0311913],
	[ 0.353896, -0.158651 ],
	[ 0.31284 , -0.184925 ],
	[ 0.305802, -0.154368 ]])
trans = ElementTrans(X)
el = Element(LegendreBasis, 1)

sz = 9
color = '#003262'

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
# for i in range(el.Nn):
# 	x = trans.Transform(el.nodes[i])
# 	plt.plot(x[0], x[1], 'o', color=color, markersize=sz)

plt.axis('off')
# plt.xlim(np.min(X[:,0]),np.max(X[:,0])+.1)
# plt.ylim(np.min(X[:,1]),np.max(X[:,1])+.1)

if (oc.Good()):
	plt.savefig(oc.Get())

plt.figure()
ref = np.linspace(-1,1,Nref+1)
Xn = np.zeros(((Nref+1)**2, 2))
for i in range(Nref+1):
	for j in range(Nref+1):
		Xn[j + i*len(ref)] = trans.Transform([ref[i], ref[j]])

trans = []
for i in range(Nref):
	for j in range(Nref):
		Xr = np.zeros((4,2))
		idx = j + i*(Nref+1)
		Xr[0] = Xn[idx]
		Xr[1] = Xn[idx+1]
		Xr[2] = Xn[idx+Nref+1]
		Xr[3] = Xn[idx+Nref+2]
		trans.append(ElementTrans(Xr))

sz = sz - int(Nref/2)+1
xi = np.linspace(-1,1)
x = np.zeros((len(xi), 2))
for i in range(Nref):
	for j in range(Nref):
		tno = j + i*Nref 
		for p in range(len(xi)):
			x[p,:] = trans[tno].Transform([-1.,xi[p]])
		plt.plot(x[:,0], x[:,1], 'k')
		for p in range(len(xi)):
			x[p,:] = trans[tno].Transform([xi[p], -1.])
		plt.plot(x[:,0], x[:,1], 'k')
		if (j==Nref-1):
			for p in range(len(xi)):
				x[p,:] = trans[tno].Transform([1.,xi[p]])
			plt.plot(x[:,0], x[:,1], 'k')
		if (i==Nref-1):
			for p in range(len(xi)):
				x[p,:] = trans[tno].Transform([xi[p],1.])
			plt.plot(x[:,0], x[:,1], 'k')

		# for n in range(el.Nn):
		# 	node = trans[tno].Transform(el.nodes[n])
		# 	plt.plot(node[0], node[1], 'o', color=color, markersize=sz)	

plt.axis('off')
# plt.xlim(np.min(X[:,0]),np.max(X[:,0])+.1)
# plt.ylim(np.min(X[:,1]),np.max(X[:,1])+.1)
if (oc.Good()):
	plt.savefig(oc.Get())
else:
	plt.show()