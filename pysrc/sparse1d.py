#!/usr/bin/env python3

import numpy as np
import matplotlib.pyplot as plt
from OutputCycler import * 
from trans1d import * 

oc = OutputCycler() 

Ne = 6
xe = np.linspace(0,1,Ne+1)

for p in range(1,4):
	fes = H1Space(xe, LobattoBasis(p))
	M = Assemble(fes, MassIntegrator, lambda x: 1, 2*p+1)

	plt.figure()
	plt.spy(M.todense())
	if (oc.Good()):
		plt.savefig(oc.Get())
if not(oc.Good()):
	plt.show()