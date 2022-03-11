#!/usr/bin/env python3

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import LinearSegmentedColormap

from trans2d import * 
from OutputCycler import * 
oc = OutputCycler()

mesh = RectMesh(2,2)
fes = L2Space(mesh, LobattoBasis, 1)
vfes = L2Space(mesh, LobattoBasis, 1, 2)

M = Assemble(vfes, VectorMassIntegrator, lambda x: 1, 3)
MF = FaceAssemble(vfes, VectorJumpJumpIntegrator, 1, 3) + BdrFaceAssemble(vfes, VectorJumpJumpIntegrator, 1, 3)
D = MixAssemble(fes, vfes, MixDivIntegrator, 1, 3)
DF = MixFaceAssemble(fes, vfes, MixJumpVAvgIntegrator, 1, 3)
P = FaceAssemble(fes, PenaltyIntegrator, 1, 3) + BdrFaceAssemble(fes, PenaltyIntegrator, 1, 3)

F = sp.bmat([[M+MF, (D+DF).T], [(D+DF), None]]).todense()
S = sp.bmat([[M, (D+DF).T], [(D+DF), P]]).todense()
schur = (D+DF)*M*(D+DF).T + P 
R = sp.bmat([[M, (D+DF).T], [None, schur]]).todense()

plt.figure()
plt.spy(F, alpha=(np.fabs(F)>0).astype('float'))
plt.axvline(vfes.Nu-.5, color='k', alpha=.1)
plt.axhline(vfes.Nu-.5, color='k', alpha=.1)
plt.axis('off')
if (oc.Good()):
	plt.savefig(oc.Get())

plt.figure()
plt.spy(S, alpha=(np.fabs(S)>0).astype('float'))
plt.axvline(vfes.Nu-.5, color='k', alpha=.1)
plt.axhline(vfes.Nu-.5, color='k', alpha=.1)
plt.axis('off')
if (oc.Good()):
	plt.savefig(oc.Get())

plt.figure()
plt.spy(R, alpha=(np.fabs(R) > 0).astype('float'))
plt.axvline(vfes.Nu-.5, color='k', alpha=.1)
plt.axhline(vfes.Nu-.5, color='k', alpha=.1)
plt.axis('off')
if (oc.Good()):
	plt.savefig(oc.Get())
else:
	plt.show()
