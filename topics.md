# Introduction 
* TRT and applications
	* show phase diagram to motivate expense 
* need for high order and curved meshes  
	* triple point mesh 
	* LOR diagrams 
* why VEF 
	* mention beneficial ideas enabled by VEF 
	* mention Ben Yee results + nonlinear elimination 
* limit scope
	* linear steady state transport 
	* 2D quadrilateral elements 
* gap analysis 
	* previous work 
* thesis statement 
* summary of results
* outline of document 

# Radiation Transport Theory
* derivation of intensity 
	* track length density 
* cross sections (reaction rate experiment)
* useful angular identities 
* TRT to linear 
* f vs psi v I 
* derive transport equation 
	* equation, BCs, coefficients 
	* units
	* assumptions
	* Omega diagram 
	* simplification to 2D 
	* connection to distribution function 
	* derivation of diffusion + Marshak BCs
* VEF assumptions 
	* positive psi
* level symmetric quadrature 

# VEF 
* derivation of VEF equations 
	* drift-diffusion form 
* derivation of Miften Larsen BCs 
* connection to diffusion w/ Marshak
* VEF algorithm in operator notation 
	* fixed point and Anderson solution strategies 
	* algorithm diagram 
	* leverage sweep 
* properties of VEF data 
	* Gateaux of Eddington tensor 
	* bounds 
	* asymptotic limits
* properties of VEF equations 
	* diffusion advection reaction structure 
	* div(E) -> advection 
	* definition of elliptic PDE 
* independent vs consistent methods 
	* discretization commuting diagram 

# FEM 
* overview of methods 
	* least squares 
	* weighted residuals 
	* galerkin 
* motivations 
	* meshing 
		* handles irregular geometry 
		* piecewise handles less regularity better 
		* local support -> sparse matrix 
		* can do any boundary condition
	* sparse matrix key to efficient solution via iterative methods 
	* nodal basis allows easy enforcement of continuity 
	* galerkin provides best solution (in energy norm) 
	* seeking in sobolev space is natural 
* local polynomial spaces 
	* used to describe mesh and solution on each element 
	* polynomial spaces in general 
	* plots 
		* shape functions: 1D, 2D, Legendre, Lobatto 
		* node locations in 2D 
	* vandermonde 
	* tensor product 
	* horner's method 
	* change of basis
* sobolev spaces 
	* L2 product is L2 
* description of mesh 
	* mesh as H1 FES 
* integration transforms 
	* scalar and vector 
	* gradient of Piola 
	* **face transformations**
		* normal as rotation of Jacobian matrix/Nanson's formula 
	* examples 
	* inverse transformations
* finite element spaces 
	* sharing of DOFs for strong conditions
	* proof of [v.n] = 0 for RT 
* DG notation 
	* jumps and averages diagram 
* primal vs mixed vs dual etc 
* Galerkin and Petrov-Galerkin
	* best approximation 
	* notion of for all in test space
	* principle of minimum potential energy
* assembly (local support) 
	* apply to generic operator
	* linear algebra operations 
	* how to assemble VEF gradient term via flattening 
* high level idea of local approximations -> sparse systems 
* idea of weak forms
* quadrature 
* iterative solution of linear systems + preconditioning
	* motivate by expense of direct 
	* classical iterative methods 
		* richardson, Jacobi, GS 
	* brief note on AMG 

# Transport Discretizations 
* discrete ordinates 
* DG in space 
	* upwind diagram 
* computation of VEF data + derivatives 
* need for fixup 
* effect of S2
* discrete algorithm 
	* define mixed space scattering mass matrix 
	* computation of source moments 
* SI as Richardson via sparsity plot 
* lagging on curved meshes 
* computing face matrices on reentrant faces 
* need for HO?

# DGVEF 
* adaption of unified to vef 
* numerical fluxes 
* derivation of CG VEF 
* description of subspace correction preconditioner 
	* assembly diagram 

# RTVEF 
* weak form 
	* prove need [v.En] = 0 
	* motivate use of non-conforming space 
	* mention petrov galerkin approach 
* discrete inf sup condition 
* block solvers 
* hybridization 

# SMM 
* introduce SMM 
	* cite LM paper, Cefus and Larsen 
	* goal is to have SPD LHS 
* derive equations + BCs as additive closure (instead of VEF's multiplicative)
	* connect to radiation diffusion with extra sources  
* connect to a linearization of VEF 
	* point out correction terms are derivatives of VEF data => TSE 
	* provides systematic path to convert VEF to SMM 
* linearize IP, CG, RT, HRT 
* do VEF and SMM differ with second order accuracy in TDL? 

# Additional Results 
* effect of initial guess from outer iteration 
* additional sweeps on triple point 
* anderson on triple point 
* comparison of methods 
	* solution quality on triple point mesh 
	* big summmary tables 
		* thick diffusion limit 
		* crooked pipe 
* recommendations for use in production code 

# Conclusions 
* restate thesis 
* future work 
	* extend to TRT, multi-group, rad hydro 
	* test CGVEF in multiphysics context 
	* petrov galerkin MFEM VEF 
	* hybridization without Piola 
	* fix for loss of current accuracy? 
	* extend RTVEF to 3D 
	* consistent SMM by lagging 