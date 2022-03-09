#!/usr/bin/env python3

import numpy as np
import matplotlib.pyplot as plt
import re 
import pandas as pd 
from OutputCycler import * 
import texTools as tex

oc = OutputCycler()
base = 'data/dgvef/mock/'
files = ['usc', 'slu', 'sym1', 'sym3']

d = {}
for file in files:
	f = open(base + file + '.txt', 'r')
	s = f.read()
	Ne = list(map(int, re.findall(r'global NE = ([0-9]*)', s)))
	out = re.findall(r'np =\s*([0-9]*), it = ([0-9]*)', s)
	nproc = [] 
	it = [] 
	for ele in out:
		nproc.append(int(ele[0]))
		it.append(int(ele[1]))
	d[file] = {'Ne': Ne, 'it': it, 'np': nproc}

table = tex.Tabular('Processors', '$N_e$', 'AMG', 'Direct', 'AMG-S', 'AMG-S3')
ele = d[files[0]]['Ne']
nproc = d[files[0]]['np']
for i in range(len(ele)):
	s = [str(nproc[i]), tex.utils.writeNumber(ele[i], '{}')] 
	for f in files:
		it = d[f]['it'][i]
		if (it>=250):
			s.append(r'\textendash')
		else:
			s.append(str(it))
	table.AddRow(*s)

if (oc.Good()):
	table.Write(oc.Get())
else:
	print(table)