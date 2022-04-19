#!/usr/bin/env python3

import numpy as np
import matplotlib.pyplot as plt
import re 
import pandas as pd 
from OutputCycler import * 
import texTools as tex

oc = OutputCycler()

groups = [{'base': 'data/dgvef/weak/', 'files': ['ip', 'cg'], 'labels': ['IP', 'CG']},
	{'base': 'data/rtvef/weak/', 'files': ['rt', 'hrt'], 'labels': ['RT', 'HRT']},
	{'base': 'data/smm/weak/', 'files': ['ip', 'cg', 'rt_bicg', 'hrt'], 'labels': ['IP', 'CG', 'RT', 'HRT']}
	]

d = {}
for g in groups:
	for file in g['files']:
		f = open(g['base'] + file + '.txt', 'r')
		s = f.read()
		f.close()
		Ne = list(map(int, re.findall(r'global NE = ([0-9]*)', s)))
		out = re.findall(r'np =\s*([0-9]*), it = ([0-9]*)', s)
		nproc = [] 
		it = [] 
		for ele in out:
			nproc.append(int(ele[0]))
			it.append(int(ele[1]))
		d[g['base']+file] = {'Ne': Ne, 'it': it, 'np': nproc}

labels = [] 
for g in groups:
	labels += g['labels']

table = tex.Tabular('Processors', '$N_e$', *labels)
ele = d[list(d.keys())[0]]['Ne']
nproc = d[list(d.keys())[0]]['np']

for i in range(len(ele)):
	s = [str(nproc[i]), tex.utils.writeNumber(ele[i], '{}')]
	for key in d.keys():
		s.append(str(d[key]['it'][i]))
	table.AddRow(*s)
table.AddColumnGroup('VEF', 2, 4)
table.AddColumnGroup('SMM', 6, 4)

if (oc.Good()):
	table.Write(oc.Get())
else:
	print(table)