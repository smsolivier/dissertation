#!/usr/bin/env python3

import numpy as np
import matplotlib.pyplot as plt
import re 
import texTools as tex

from OutputCycler import * 
oc = OutputCycler()

groups = [
	{'types': ['ip', 'br2', 'mdldg', 'cg'], 'loc': 'data/dgvef/', 'dirs': ['tdl_orthog', 'tdl_3p1']},
	{'types': ['rt', 'hrt'], 'loc': 'data/rtvef/', 'dirs': ['tdl_orthog', 'tdl_3p']}, 
	{'types': ['ip', 'cg', 'rt', 'hrt'], 'loc': 'data/smm/', 'dirs': ['tdl_orthog', 'tdl_3p']}
	]

d = []
methods = []
for g in groups:
	methods += [t.upper() for t in g['types']]
for i in range(2):
	table = tex.Tabular(r'$\epsilon$', *methods)
	for e in range(1,5):
		s = ['$10^{{-{}}}$'.format(e)]
		for g in groups:
			types = g['types']
			for t in types:
				fname = g['loc'] + '{}/{}{}.txt'.format(g['dirs'][i], t, e)
				f = open(fname, 'r')
				outer = int(re.findall(r'outer = ([0-9]*)', f.read())[0])
				f.close()

				s.append(str(outer))
		table.AddRow(*s)
	table.AddColumnGroup('VEF', 1, 6)
	table.AddColumnGroup('SMM', 7, 4)
	table.AddColumnBreak(0)
	if (oc.Good()):
		table.Write(oc.Get())
	else:
		print(table)


