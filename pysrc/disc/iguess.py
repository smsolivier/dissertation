#!/usr/bin/env python3

import numpy as np
import matplotlib.pyplot as plt

from OutputCycler import * 
oc = OutputCycler()

r = 3 
cumulative = oc.GetOpt(0, False)
orders = [1,2,3]

for p in orders:
	base = 'data/disc/iguess/'
	files = ['true', 'false']
	leg = ['Previous', 'Zero']
	outer = []
	tot = []
	plt.figure()
	for i,f in enumerate(files):
		df = np.loadtxt(base+f+'_{}_{}.txt'.format(p,r))
		outer.append(df.shape[0])
		tot.append(np.sum(df[:,0]))
		cum = np.zeros(df.shape[0])
		cum[0] = df[0,0]
		for j in range(1, df.shape[0]):
			cum[j] = cum[j-1] + df[j,0]
		plt.plot(np.arange(1,outer[i]+1), cum if cumulative else df[:,0], '-o', label=leg[i])
		plt.xticks(np.arange(1,outer[i]+1, 2))
	assert(len(np.unique(outer))==1)
	print((tot[1] - tot[0])/tot[1]*100)
	if (cumulative):
		plt.legend(loc='upper left')
	else:
		plt.legend(loc='lower left')
	plt.xlabel('Outer Iteration Number')
	if (cumulative):
		plt.ylabel('Cumalative Number of Inner Iterations')
	else:
		plt.ylabel('Inner Iterations to Convergence')
	if (oc.Good()):
		plt.savefig(oc.Get())
if not(oc.Good()):
	plt.show()