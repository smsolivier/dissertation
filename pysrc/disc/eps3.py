#!/usr/bin/env python3

import numpy as np
import matplotlib.pyplot as plt
import re 
import texTools as tex

from OutputCycler import * 
oc = OutputCycler()

base = 'data/dgvef/tdl_3p'
orthog = 'data/dgvef/tdl_orthog/'
sweeps = [1,2,3]
method = 'ip'
eps = np.arange(1,5)

table = tex.Tabular(r'$\epsilon$', *[str(s) for s in sweeps])
for e in eps:
	t = ['$10^{-' + str(e) + '}$']
	for s in sweeps:
		f = open(base+str(s)+'/'+method+str(e)+'.txt', 'r')
		file = f.read()
		outer = int(re.findall(r'outer =\s([0-9]*)', file)[0])
		f.close()

		t.append(str(outer))

	# f = open(orthog+method+str(e)+'.txt', 'r')
	# outer = int(re.findall(r'outer =\s([0-9]*)', f.read())[0])
	# t.append(str(outer))
	# f.close()

	table.AddRow(*t)
# table.AddColumnGroup('Triple Point', 1, len(sweeps))
# table.AddColumnBreak(0)
if (oc.Good()):
	table.Write(oc.Get())
else:
	print(table)