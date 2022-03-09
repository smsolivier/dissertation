#!/usr/bin/env python3

import numpy as np
import matplotlib.pyplot as plt
import re 
import texTools as tex

from OutputCycler import * 
oc = OutputCycler()

groups = [
	{'types': ['ip', 'br2', 'mdldg', 'cg'], 'loc': 'data/dgvef/', 'dirs': ['tdl_orthog', 'tdl_3p1'], 'ext': 'dgvef'},
	{'types': ['h1', 'rt', 'hrt'], 'loc': 'data/rtvef/', 'dirs': ['tdl_orthog', 'tdl_3p'], 'ext': 'rtvef'},
	{'types': ['ip', 'cg', 'rt', 'hrt'], 'loc': 'data/smm/', 'dirs': ['tdl_orthog', 'tdl_3p'], 'ext': 'smm'}
]
for g in groups:
	dirs = g['dirs']
	types = g['types']
	df = {okey: {ikey: [] for ikey in types} for okey in dirs}
	for e in range(1,5):
		for t in types: 
			for d in dirs:
				fname = g['loc'] + '{}/{}{}.txt'.format(d, t, e)
				f = open(fname, 'r') 
				for line in f: 
					if ('outer =' in line):
						outer = int(re.findall(r'outer = ([0-9]*)', line)[0])
						df[d][t].append(outer) 

	table = tex.Tabular()
	table.SetHeader(r'$\epsilon$', *[t.upper() for t in types]*len(dirs))
	for e in range(0,4):
		eps = '$10^{{-{}}}$'.format(e+1) 
		s = [eps]
		for i,d in enumerate(dirs):
			for t in types:
				s.append(str(df[d][t][e]))
		table.AddRow(*s)
	table.AddColumnGroup('Orthogonal', 1, len(types))
	table.AddColumnGroup('Triple Point', 1+len(types), len(types)) 
	table.AddColumnBreak(0)

	if (oc.Good()):
		table.Write(oc.Get(0, g['ext']))
	else:
		print(table)