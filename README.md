Collatz‑3: Python Implementation and Documentation
--------------------------------------------------
[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.18513310.svg)](https://doi.org/10.5281/zenodo.18513310)
--------------------------------------------------
Overview
--------
This archive provides a clean and minimal Python implementation of the Collatz‑3
dynamical system. The Collatz‑3 map is defined by repeated division by 3 when
possible, and by a 4n ± 1 transformation when n is not divisible by 3.

The system behaves similarly to the classical Collatz map but uses 3-adic
valuation instead of 2-adic valuation. All tested values eventually converge to
1, although some numbers exhibit long transient behavior before reaching the
fixed point.

Definition of the Collatz‑3 Map
-------------------------------
For a positive integer n:

1. If n is divisible by 3:
       n := n / 3

2. If n ≡ 1 (mod 3):
       n := (4n - 1) / 3

3. If n ≡ 2 (mod 3):
       n := (4n + 1) / 3

The process repeats until n reaches 1.

Included Files
--------------
- collatz3.py  
    Python implementation of the Collatz‑3 map, including:
    - trajectory generation
    - step counting ("3‑Resistance")
    - interactive command-line interface

- overview.pdf  
    Mathematical background and explanation of the Collatz‑3 system.

- howto.pdf  
    Instructions for running the code and performing numerical experiments.

- LICENSE  
    CC BY 4.0 license with copyright notice.

Usage
-----
Run the script from the command line:

    python collatz3.py

Enter a positive integer when prompted.  
The program will output:
- the full trajectory
- the number of steps required to reach 1

Example
-------
Input:
    7

Output:
    Path: 7 → 9 → 3 → 1
    Steps (3‑Resistance): 3

Requirements
------------
- Python 3.x  
No external libraries are required.

License
-------
Copyright (c) 2026 Hiroshi Harada  
This work (Collatz‑3 Python Implementation and Documentation) is licensed under
the Creative Commons Attribution 4.0 International License (CC BY 4.0).  
You are free to use, modify, and share this work with attribution.

The full text of the CC BY 4.0 license is available at:
https://creativecommons.org/licenses/by/4.0/legalcode

Citation
--------
If you use this code or dataset in academic work, please cite the Zenodo DOI
associated with this archive.

Author
------
Hiroshi Harada
