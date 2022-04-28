\NeedsTeXFormat{LaTeX2e}
\ProvidesClass{dissertation}[extends the ucbthesis class]
% --- setup options for dissertation class ---
\newif\iftodo
\newif\ifcheck
\newif\ifmycounter
\mycountertrue
\DeclareOption{todo}{\todotrue}
\DeclareOption{check}{\checktrue}
\DeclareOption{nocounter}{\mycounterfalse}
% pass everything else to ucbthesis package 
\DeclareOption*{\PassOptionsToClass{\CurrentOption}{ucbthesis}}
\ProcessOptions\relax
\LoadClass{ucbthesis}

% --- interdependence table environment --- 
\newenvironment{preamble}[1]{%
	\phantomsection
	\addcontentsline{toc}{chapter}{#1}%
	\begin{center}%
	{\large \bfseries #1}%
	\end{center}%
}{
	\clearpage
}

% --- packages to use --- 
\RequirePackage{amsmath}
\RequirePackage{amsthm}
\RequirePackage{amssymb}
\RequirePackage{bbm}
\RequirePackage[implicit=true, hidelinks]{hyperref}
\RequirePackage{graphicx}
\RequirePackage{mathtools}
\RequirePackage{multirow}
\RequirePackage{booktabs}
\RequirePackage{cancel}
\RequirePackage[noend]{algpseudocode}
\RequirePackage{siunitx}
\DeclareSIUnit\str{str}
\sisetup{per-mode=fraction, inter-unit-product={}\cdot{}}
\RequirePackage{enumerate}
\RequirePackage{tikz}
\usetikzlibrary{calc}
\RequirePackage{stmaryrd}
\RequirePackage{subcaption}
\RequirePackage[backend=bibtex,sorting=none,style=ieee,citestyle=numeric-comp]{biblatex}
\RequirePackage{subfiles}
\RequirePackage{adjustbox}
% \RequirePackage[section]{placeins}
\usepackage[acronym,nomain,nonumberlist,nogroupskip,nopostdot]{glossaries}
\newglossarystyle{april_gloss_style}{%
  \glossarystyle{long}%
  \renewenvironment{theglossary}%
     {\begin{longtable}{p{2.5cm}p{\linewidth}}}%
     {\end{longtable}}%
}
\renewcommand{\glsnamefont}[1]{\textbf{#1}}

% set to display subsections in TOC 
\setcounter{tocdepth}{2}
\setcounter{secnumdepth}{4}

% rename bib auxiliary file names
\renewcommand{\blxauxsuffix}{}

% copied from April's thesis 
\addtolength{\abovecaptionskip}{\baselineskip} 

% --- custom commands --- 
\newcommand{\mat}[1]{\boldsymbol{\mathrm{#1}}}
\newcommand{\hmat}[1]{\hat{\mat{#1}}}
\newcommand{\tmat}[1]{\tilde{\mat{#1}}}
\renewcommand{\vec}[1]{\boldsymbol{#1}}
\newcommand{\bvec}[1]{\boldsymbol{\mathrm{#1}}}
\newcommand{\twovec}[2]{\begin{pmatrix} #1 \\ #2 \end{pmatrix}}
\newcommand{\hvec}[1]{\hat{\vec{#1}}}
\newcommand{\fevec}[1]{\,\underline{\!#1\!}\,}
\newcommand{\ud}{\mathop{}\!\mathrm{d}} % upright derivative symbol
\newcommand{\pderiv}[2]{\frac{\partial #1}{\partial #2}}
\newcommand{\dderiv}[2]{\frac{\ud #1}{\ud #2}}
\newcommand{\dmderiv}[2]{\frac{\ud_M #1}{\ud #2}}
\newcommand{\secondderiv}[2]{\frac{\ud^2 #1}{\ud #2^2}}
\newcommand{\secondpderiv}[2]{\frac{\partial^2 #1}{\partial #2^2}}
\newcommand{\bracket}[1]{\!\left[ #1 \right]}
\newcommand{\bracet}[1]{\!\left\{ #1 \right\}}
\newcommand{\paren}[1]{\left( #1 \right)}
\newcommand{\iso}[2]{\ce{^{#2}#1}\xspace}
\newcommand{\R}{\mathbb{R}}
\newcommand{\C}{\mathbb{C}}
\renewcommand{\H}{\vec{\mathrm{H}}}
\newcommand{\Hone}{[H^1(\D)]^2}
% \newcommand{\Hone}{\H^1(\D)}
\newcommand{\tphi}{\varphi}
\renewcommand{\P}{\boldsymbol{\mathrm{P}}}
\newcommand{\E}{\boldsymbol{\mathrm{E}}}
\newcommand{\F}{\boldsymbol{\mathrm{F}}}
\newcommand{\I}{\boldsymbol{\mathrm{I}}}
\newcommand{\D}{\mathcal{D}}
\newcommand{\meshT}{\mathcal{T}}
\newcommand{\T}{\mat{T}}
\newcommand{\M}{\mat{M}}
\newcommand{\x}{\boldsymbol{\mathrm{x}}}
\newcommand{\y}{\boldsymbol{\mathrm{y}}}
\newcommand{\avg}[1]{\left\{\!\!\left\{#1\right\}\!\!\right\}}
\newcommand{\jump}[1]{\left\llbracket#1 \right\rrbracket}
\renewcommand{\vector}[1]{\begin{bmatrix} #1 \end{bmatrix}^T}
\newcommand{\Omegahat}{\vec{\Omega}}
\newcommand{\Omegahatn}{\Omegahat\cdot\n}
\newcommand{\nablah}{\nabla_h}
\newcommand{\hnabla}{\hat{\nabla}}
\renewcommand{\ang}[1]{\langle #1 \rangle}
\newcommand{\Sn}{S$_N$\xspace}
\newcommand{\Qone}{\vec{Q}_1}
\newcommand{\Qcal}[1]{\mathcal{Q}_{#1}(\hat{K})}
\newcommand{\Pcal}[1]{\mathcal{P}_{#1}(\hat{K})}
\newcommand{\Qbb}[1]{\mathbb{Q}_{#1}}
\newcommand{\RT}{\mathit{RT}}
\newcommand{\hRT}{\hat{\RT}}
\newcommand{\vDG}{X_p}
\newcommand{\e}{\boldsymbol{\mathrm{e}}}
\newcommand{\n}{\boldsymbol{\mathrm{n}}}
\newcommand{\tang}{\boldsymbol{\mathrm{\tau}}}
\newcommand{\Jin}{J_\text{in}}
\newcommand\Q{\mathcal{Q}}

% --- text highlighting --- 
% highlights text to remind me to do look at it again
% turning todo off at the top returns all text to original color
\iftodo
\newcommand{\todo}[1]{\textcolor{red}{[#1]}}
\else
\newcommand{\todo}[1]{}
\fi

% recheck commands
% highlights to remind me to look at it again
% turning recheck off at the top reverts back to normal colors
\ifcheck
\newcommand{\checkover}[1]{\textcolor{blue}{#1}}
\else
\newcommand{\checkover}[1]{#1}
\fi

% --- custom math operators --- 
\DeclareMathOperator{\sign}{sign}
% \DeclareMathOperator{\Div}{Div}
\let\div\relax
\DeclareMathOperator{\div}{div}
% \DeclareMathOperator{\ran}{ran}
% \DeclareMathOperator{\range}{range}
\DeclareMathOperator{\tr}{trace}
% \DeclareMathOperator{\diag}{diag}
\DeclareMathOperator{\spn}{span}
\DeclareMathOperator\supp{supp}
\DeclareMathOperator\diag{diag}

% --- math environments --- 
\newtheorem{cor}{Corollary}
\newtheorem{prop}{Proposition}
\newtheorem{thm}{Theorem}
\newtheorem{lem}{Lemma}
\newtheorem{rem}{Remark}
\newtheorem*{rem*}{Remark}
