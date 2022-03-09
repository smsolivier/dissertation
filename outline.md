# Introduction
* motivation 
	* HO on HO 
* pare down to simple linear transport problem 
* gap in VEF literature 

# VEF Background
* transport equation introduction 
* derivation of VEF 
	* miften larsen BCs 
* operator notation derivation of VEF algorithm
	* fixed point 
	* anderson 
* properties of VEF data 
	* gateaux derivative -> nullspace 

# FEM 
* description of mesh 
* notation 
* integration transforms 
* finite element spaces 
* assembly 

# Transport Discretizations
* SN 
* DG 
	* upwind discretization 
	* lagging on curved meshes 
	* flux fixup
* could be place to show full matrix, idea of richardson? 

# DGVEF 
## Results 
* MMS 
* TDL 
* mock problem 
* crooked pipe 
* weak scaling 

# RTVEF 
## Results
* MMS 
* TDL 
* curved solvers failure 
* bad modes 
* two material problem 
* crooked pipe 
* weak scaling

# SMM
* MMS 
	* all methods phi 
	* RT and HRT J should match RTVEF results 
* TDL 
* glancing void 
* crooked pipe 
* weak scaling 
	* comparison of minres and bicg for RT 

# Comparison of Methods + Properties of VEF in General 
* solution quality on triple point mesh 
* SMM vs VEF 
	* TTS in inner solve 
* slower convergence on reentrant meshes 
* need for augments 

# Conclusions
* summary of results 
* future work 