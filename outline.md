# Introduction
* very brief goals and approach 
* motivation 
	* introduce predictive modeling 
	* TRT 
	* high order 
	* why VEF (NABC)
* previous work -> gap analysis 
* scope of research
	* limit to grey linear transport in 2D 
* summary of results
* outline of document 

# VEF Algorithm
* linear transport equation 
* derivation of VEF 
* algorithm in operator notation 
* properties of VEF data 

# FEM 
* basic aspects of FEM 
	* weak forms
		* test functions 
		* weak derivatives 
		* examples -> variational forms 
	* galerkin 
		* variational interpretation 
		* weighted residual interpretation 
		* allows weaker requirements on solution 
	* sobolev 
		* example applications 
		* conforming vs non-conforming 
	* fundamental components 
		* mesh
		* local approximation with matching conditions 
		* integration by parts 
		* canonical basis with local support 
			* leads to sparse matrices 
* local polynomial spaces 
* description of mesh 
	* requirements of mesh
	* local gradient 
	* jumps averages
	* boundaries 
* integration transforms 
	* scalar case 
	* vector case 
	* gradient of piola 
* finite element spaces 
	* matching conditions for piecewise 
	* distribution of DOFs 
* assembly 
* preconditioning 

# Transport Discretizations
* SN 
* DG 
* sweep
* discrete VEF algorithm
* fixups 

# DGVEF 
* adaption of unified to vef 
* numerical fluxes 
* derivation of CG VEF 
* description of subspace correction preconditioner 
* results 
	* MMS 
	* TDL 
	* mock problem 
	* crooked pipe 
	* weak scaling 

# RTVEF 
* requirements of spaces 
* H1 
* RT 
* discrete inf-sup condition 
* block solvers 
* hybridization 
* results
	* MMS 
	* TDL 
	* curved solvers failure 
	* bad modes 
	* two material problem 
	* crooked pipe 
	* weak scaling

# SMM
* derivation via lagging 
* connection to VEF via linearization 
* derivation of SMMs 
* results 
	* MMS 
		* all methods phi 
		* RT and HRT J should match RTVEF results 
	* TDL 
	* glancing void 
	* crooked pipe 
	* weak scaling 
		* comparison of minres and bicg for RT 

# Additional Results and Discussion
* additional sweeps on triple point 
* anderson on triple point 
* solution quality on triple point mesh 
* comparison of SMM and VEF 
* recommendations for use in production code 

# Conclusions
* summary of results 
* future work 