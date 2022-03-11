#!/usr/bin/env python3

import numpy as np
import matplotlib.pyplot as plt
import scipy.sparse as sp 
import scipy.sparse.linalg as spla 
from OutputCycler import OutputCycler
oc = OutputCycler()

p = 1
Ne = 16
def FileMatrix(fname):
	f = open(fname, 'r')
	line = next(f) 
	while (line.startswith('%')):
		line = next(f) 

	[n,m,nnz] = line.strip().split(' ')
	n = int(n) 
	m = int(m) 
	nnz = int(nnz) 
	data = [] 
	row = [] 
	col = [] 

	for line in f:
		[r,c,d] = line.strip().split(' ') 
		row.append(int(r)-1)
		col.append(int(c)-1) 
		data.append(float(d)) 

	f.close()
	return sp.coo_matrix((data, (row, col)), (n,m))

C = FileMatrix('data/rtvef/hybsp/C.txt') 
CEt = FileMatrix('data/rtvef/hybsp/CEt.txt') 

NJ = C.shape[1]
Nlam = C.shape[0] 
Nphi = (p+1)**2*Ne

bsize_J = int(NJ/Ne/2)
M = sp.lil_matrix((NJ,NJ))
Mi = sp.lil_matrix((NJ,NJ))
D = sp.lil_matrix((Nphi, NJ))
Ma = sp.lil_matrix((Nphi, Nphi))
for d in range(2):
	for e in range(Ne):
		idx1 = e*bsize_J + d*int(NJ/2) 
		idx2 = (e+1)*bsize_J + d*int(NJ/2) 
		M[idx1:idx2, idx1:idx2] = np.ones((bsize_J, bsize_J))

		D[e*(p+1)**2:(e+1)*(p+1)**2, idx1:idx2] = np.ones(((p+1)**2, bsize_J))
		Ma[e*(p+1)**2:(e+1)*(p+1)**2, e*(p+1)**2:(e+1)*(p+1)**2] = np.ones(((p+1)**2, (p+1)**2))

P = sp.lil_matrix((NJ+Nphi+Nlam, NJ+Nphi+Nlam))
bsize = int(NJ/Ne) + (p+1)**2 
count = 0
for e in range(Ne):
	for d in range(2):
		for i in range(bsize_J):
			idx = e*bsize_J + d*int(NJ/2) + i
			P[count, idx] = 1 
			count += 1 
	for i in range((p+1)**2):
		idx = NJ + e*(p+1)**2 + i
		P[count, idx] = 1 
		count += 1

for i in range(Nlam):
	P[NJ+Nphi+i,NJ+Nphi+i] = 1 

block = sp.bmat([[M, D.T, CEt], [D, Ma, None], [C, None, None]])
# alpha_block = np.zeros(block.shape)
# for i in range(block.shape[0]):
# 	for j in range(block.shape[1]):
# 		alpha_block[i,j] = abs(block[i,j])>1e-10
plt.spy(block.todense(), alpha=(np.fabs(block.todense()) > 0).astype('float'))
plt.axhline(NJ-.5, color='k', alpha=.1)
plt.axvline(NJ-.5, color='k', alpha=.1) 
plt.axhline(NJ+Nphi-.5, color='k', alpha=.1) 
plt.axvline(NJ+Nphi-.5, color='k', alpha=.1) 
plt.axis('off')
if (oc.Good()):
	plt.savefig(oc.Get())

plt.figure()
block = P@block@P.T 
plt.spy(block.todense(), alpha=(np.fabs(block.todense()) > 0).astype('float'))
plt.axhline(NJ+Nphi-.5, color='k', alpha=.1) 
plt.axvline(NJ+Nphi-.5, color='k', alpha=.1) 
plt.axis('off')
if (oc.Good()):
	plt.savefig(oc.Get())

plt.figure()
S = C*(D.T*D*M)*CEt
reduced = P@sp.bmat([[M, D.T, CEt], [D, Ma, None], [None, None, S]])@P.T
plt.spy(reduced.todense(), alpha=(np.fabs(reduced.todense())>0).astype('float'))
plt.axhline(NJ+Nphi-.5, color='k', alpha=.1) 
plt.axvline(NJ+Nphi-.5, color='k', alpha=.1) 
plt.axis('off')
if (oc.Good()):
	plt.savefig(oc.Get())
else:
	plt.show()