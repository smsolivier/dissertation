# Introduction 
* TRT and applications
* need for high order and curved meshes  
* limit scope
	* linear steady state transport 
	* 2D quadrilateral elements 
* why VEF 
	* mention beneficial ideas enabled by VEF 
* gap analysis 
	* previous work 
* thesis statement 
* summary of results
* outline of document 

# VEF 
* derivation of VEF equations 
* definition of elliptic PDE 
* connection to diffusion 
* VEF algorithm in operator notation 
	* fixed point and Anderson solution strategies 
* properties of VEF data 
	* Gateaux of Eddington tensor 

# FEM 
* description of mesh 
* integration transforms 
	* scalar and vector 
	* gradient of Piola 
	* face transformations
* basis types/shape functions (Legendre vs Lobatto)
* finite element spaces 
	* sharing of DOFs for strong conditions
	* proof of [v.n] = 0 for RT 
* DG notation 
* primal vs mixed vs dual etc 
* Galerkin and Petrov-Galerkin
	* best approximation 
* assembly (local support) 
	* apply to generic operator

# Transport Discretizations 
* discrete ordinates 
* DG in space 
* computation of VEF data + derivatives 
* need for fixup 
* effect of S2
* discrete algorithm (define scattering mass matrix)
* SI as Richardson via sparsity plot 

# DGVEF 
* adaption of unified to vef 
* numerical fluxes 
* derivation of CG VEF 
* description of subspace correction preconditioner 

# RTVEF 
* weak form 
	* prove need [v.En] = 0 
	* motivate use of non-conforming space 
	* mention petrov galerkin approach 
* discrete inf sup condition 
* block solvers 
* hybridization 

# SMM 
* derivation via lagging 
* derivation via linearizing
* connect to radiation diffusion with extra sources  
* linearize IP, CG, RT, HRT 

# Additional Results 
* additional sweeps on triple point 
* anderson on triple point 
* solution quality on triple point mesh 
* comparison of SMM and VEF 
* recommendations for use in production code 

# Conclusions 
* restate thesis 
* future work 
	* extend to TRT, multi-group, rad hydro 
	* test CGVEF in multiphysics context 
	* petrov galerkin MFEM VEF 
	* hybridization without Piola 
	* fix for loss of current accuracy? 