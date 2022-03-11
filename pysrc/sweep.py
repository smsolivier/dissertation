#!/usr/bin/env python3

import numpy as np
import matplotlib.pyplot as plt

from trans1d import * 
from OutputCycler import * 
oc = OutputCycler()

Ne = 5
p = 1
N = 4
quad = LegendreQuad(N)
basis = LegendreBasis(p)
xe = np.linspace(0,1,Ne+1)
space = L2Space(xe, basis) 
psi = TVector(space, quad) 
sigma_t = lambda x: 1 
sigma_s = lambda x: .9
Q = lambda x, mu: (mu*np.pi*np.cos(np.pi*x) + (sigma_t(x)-sigma_s(x))*np.sin(np.pi*x))/2
psi_in = lambda x, mu: 0 
sweep = DirectSweeper(space, quad, sigma_t, sigma_s, Q, psi_in)
sn = Sn(sweep)
M = sp.block_diag(sweep.LHS) 

d2m = [] 
Ms = sweep.Ms
for o in range(quad.N):
	tmp = []
	for a in range(quad.N):
		tmp.append(Ms*-quad.w[a]/2)	
	d2m.append(tmp) 

D2M = sp.bmat(d2m)
F = M + D2M 

plt.figure()
plt.spy(F.todense())
for a in range(1,quad.N):
	plt.axhline(a*space.Nu-.5, color='k', alpha=.1)
	plt.axvline(a*space.Nu-.5, color='k', alpha=.1)
plt.axis('off')
if (oc.Good()):
	plt.savefig(oc.Get())

plt.figure()
plt.spy(M.todense())
for a in range(1,quad.N):
	plt.axhline(a*space.Nu-.5, color='k', alpha=.1)
	plt.axvline(a*space.Nu-.5, color='k', alpha=.1)
plt.axis('off')
if (oc.Good()):
	plt.savefig(oc.Get())
else:
	plt.show()