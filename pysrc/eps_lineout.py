#!/usr/bin/env python3

import numpy as np
import matplotlib.pyplot as plt
import os 
import sys 
from OutputCycler import * 
oc = OutputCycler() 
direction = oc.GetOpt(0, 0)
bases = ['data/dgvef/tdl_orthog/'+f for f in ['ip', 'br2', 'mdldg', 'cg']] \
	+ ['data/rtvef/tdl_orthog/'+f for f in ['h1', 'rt', 'hrt']] \
	+ ['data/smm/tdl_orthog/'+f for f in ['ip', 'cg', 'rt', 'hrt']]
for base in bases:
	plt.figure()
	for e in range(1,5):
		f = open(base+str(e)+'.csv', 'r')
		head = next(f).strip().replace('"','').split(',')
		d = {key: [] for key in head}
		for line in f:
			sp = line.strip().split(',')
			for i in range(len(sp)):
				d[head[i]].append(float(sp[i]))

		f.close() 

		plt.plot(d['Points:'+str(direction)], d['phi'], label=r'$\epsilon = 10^{-' + str(e) + '}$')
	plt.legend()
	plt.xlabel('$x$' if direction==0 else '$y$')
	plt.ylabel(r'$\varphi$')
	if (oc.Good()):
		ext = os.path.basename(base)
		if ('smm' in base):
			ext += 'sm'
		plt.savefig(oc.Get(0, ext))
if not(oc.Good()):
	plt.show()