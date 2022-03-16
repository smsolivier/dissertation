#!/usr/bin/env python3

import numpy as np
import matplotlib.pyplot as plt
import glob
import os.path
from OutputCycler import *
import texTools as tex 
import re 

oc = OutputCycler()
files = [
	{'base': 'data/rtvef/cp/', 'types': ['h1', 'rtgs', 'hrt'], 'ext': 'rtvef', 
		'labels': ['H1', 'RT', 'HRT'], 'ikeys': ['max', 'min', 'avg']}, 
	{'base': 'data/dgvef/cp/', 'types': ['ip', 'br2', 'cg', 'mdldg'], 'ext': 'dgvef', 
		'labels': ['IP', 'BR2', 'CG', 'MDLDG'], 'ikeys': ['max', 'min', 'avg']}, 
	{'base': 'data/smm/cp/', 'types': ['ip', 'cg', 'rt_bicg', 'hrt'], 'ext': 'smm', 
		'labels': ['IP', 'CG', 'RT', 'HRT'], 'ikeys': ['max', 'min', 'avg']}, 
	{'base': 'data/disc/iguess/', 'types': ['outer_true', 'outer_false'], 'ext': 'iguess', 
		'labels': ['Previous', 'Zero'], 'ikeys': ['max', 'min', 'inner']}
]
for file in files:
	d = {}
	for t in file['types']:
		f = open(file['base'] + t + '.txt', 'r')
		for line in f: 
			if ('elements' in line):
				Ne = int(re.findall(r'([0-9]*) elements', line)[0])
			if ('fe order = ' in line):
				p = int(re.findall(r'fe order = ([0-9]*)', line)[0])

			if ('outer = ' in line):
				outer = int(re.findall(r'outer = ([0-9]*),', line)[0])
				inner = int(re.findall(r', inner = ([0-9]*),', line)[0])
				mn = int(re.findall(r'min = ([0-9]*)', line)[0])
				mx = int(re.findall(r'max = ([0-9]*)', line)[0])
				avg = float(re.findall(r'avg = (.*),', line)[0])
				mxnorm = float(re.findall(r'max norm = (.*)', line)[0])
				converged = mxnorm<1e-8

			if ('solve time = ' in line):
				solve_time = float(re.findall(r'solve time = (.*) s', line)[0])
				if not(t in d):
					d[t] = {}
				if not(p in d[t]):
					d[t][p] = {}

				data = {'outer': outer, 'inner': inner, 'min': mn, 'max': mx, 'avg': avg, 'solve time': solve_time, 'converged': converged}
				d[t][p][Ne] = data 

		f.close()	

	types = list(d.keys())
	l = len(types)
	ele = list(d[types[0]][1].keys())
	table = tex.Tabular()
	keys = file['ikeys']
	table.SetHeader('$N_e$', *(file['labels']*(len(keys)+1)))
	fmt = {'max': '{}', 'min': '{}', 'inner': '{}', 'avg': '{:.2f}'}
	titles = {'outer': 'Outer', 'max': 'Max Inner', 'min': 'Min Inner', 'avg': 'Avg. Inner', 'inner': 'Total Inner'}
	for p in [1,2,3]:
		for n in ele:
			si = [str(n)] 
			for i,t in enumerate(types):
				df = d[t][p][n] 
				converged = df['converged']
				si.append(str(df['outer']) + (r'\,' if converged else '$^*$'))

			for key in keys:
				for i,t in enumerate(types):
					df = d[t][p][n]
					si.append((df[key], fmt[key]))

			table.AddRow(*si) 
			table.AddRowGroup('$p='+str(p)+'$', (p-1)*len(ele), len(ele))
	for i,t in enumerate(['outer'] + keys):
		table.AddColumnGroup(titles[t], 1+i*l, l)
	table.AddColumnBreak(0)
	if (oc.Good()):
		table.Write(oc.Get(0, file['ext']))
	else:
		print(table)