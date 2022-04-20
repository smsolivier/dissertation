#!/usr/bin/env python3

import numpy as np
import matplotlib.pyplot as plt
from OutputCycler import * 
from trans1d import * 

oc = OutputCycler()

Ne = 3
p = 1 
xe = np.linspace(0,1,Ne+1)
fes = H1Space(xe, LobattoBasis(p))

K = Assemble(fes, WeakPoissonIntegrator, lambda x: 1, 2*p+1)
b = AssembleRHS(fes, DomainIntegrator, lambda x: 1, 2*p+1)

K = K[1:-1,1:-1]
b = b[1:-1]

sol = np.linalg.solve(K.todense(), b)

n = 50
dist = 6
x = np.linspace(sol[0]-dist,sol[0]+dist,n)
y = np.linspace(sol[1]-dist,sol[1]+dist,n)
X,Y = np.meshgrid(x,y) 

phi = np.zeros(X.shape)
def Potential(u):
	return .5*u.T@K@u - u@b
for i in range(n):
	for j in range(n):
		u = np.array([X[i,j], Y[i,j]])
		phi[i,j] = Potential(u)

u0 = np.array([-4,-5])
plt.plot(u0[0], u0[1], 'ko')
pot = [Potential(u0)]
r = b - K@u0
p = r.copy()
for i in range(2):
	alpha = r@p/(p@K@p)
	u = u0 + alpha*p
	plt.plot(u[0], u[1], 'ko')
	pot.append(Potential(u))
	r = r - alpha*K@p
	beta = -(r@K@p)/(p@K@p)
	d = u - u0 
	plt.quiver(u0[0], u0[1], d[0], d[1], angles='xy', scale_units='xy', scale=1.0)
	p = r + beta*p 
	u0 = u.copy()
plt.contour(X,Y,phi, [-.01, 0,3,6.79,16,32,66,128,256], colors='k')
plt.xlabel('$u_1$')
plt.ylabel('$u_2$')
if (oc.Good()):
	plt.savefig(oc.Get())
else:
	plt.show()