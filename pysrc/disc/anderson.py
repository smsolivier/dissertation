#!/usr/bin/env python3

import numpy as np
import matplotlib.pyplot as plt
import re 
import texTools as tex

from OutputCycler import * 
oc = OutputCycler()

base = 'data/dgvef/anderson/'
types = ['fp', 'low', 'aug']
eps = np.arange(1,5)

table = tex.Tabular(r'$\epsilon$', 'Fixed Point', 'Low Memory', 'Augmented')
for e in eps:
	s = ['$10^{-' + str(e) + '}$']
	for i,t in enumerate(types):
		f = open(base+t+str(e)+'.txt', 'r')
		file = f.read()
		outer = int(re.findall(r'outer =\s([0-9]*)', file)[0])
		inner = re.findall(r'inner =\s([0-9]*),\s([0-9]*),\s([0-9]*),\s([0-9]+\.?[0-9]*)', file)[0]
		total = int(inner[0])
		mx = int(inner[1])
		mn = int(inner[2])
		avg = float(inner[3])
		f.close()

		s.append(str(outer))

	table.AddRow(*s)
if (oc.Good()):
	table.Write(oc.Get())
else:
	print(table)