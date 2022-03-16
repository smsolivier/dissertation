#!/usr/bin/env python3

import numpy as np
import matplotlib.pyplot as plt

from OutputCycler import * 
oc = OutputCycler()

p = oc.GetOpt(0, 3)
r = oc.GetOpt(1, 3) 

base = 'data/disc/iguess/'
files = ['true', 'false']
leg = ['Previous', 'Zero']
outer = []
tot = []
for i,f in enumerate(files):
	df = np.loadtxt(base+f+'_{}_{}.txt'.format(p,r))
	outer.append(df.shape[0])
	tot.append(np.sum(df[:,0]))
	plt.plot(np.arange(1,outer[i]+1), df[:,0], '-o', label=leg[i])
	plt.xticks(np.arange(1,outer[i]+1, 2))
assert(len(np.unique(outer))==1)
plt.legend()
plt.xlabel('Outer Iteration Number')
plt.ylabel('Inner Iterations to Convergence')
if (oc.Good()):
	plt.savefig(oc.Get())
else:
	plt.show()