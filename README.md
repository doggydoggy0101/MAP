# Method of Alternating Projections
[![Python Formatter](https://img.shields.io/badge/Python_Formatter-ruff-black?style=flat-square)](https://github.com/astral-sh/ruff)

Unofficial implementation of "Method of alternating projections for the general absolute value equation". Please refer to the paper:

[Alcantara, J. H.](https://jhalcantara.github.io/), [Chen, J. S.](https://math.ntnu.edu.tw/~jschen/), & [Tam, M. K.](https://matthewktam.com/) (2023). *Method of alternating projections for the general absolute value equation*. Journal of Fixed Point Theory and Applications, 25(1), 39.


```bibtex
@article{Alcantara23MAP,
  author={Alcantara, Jan Harold and Chen, Jein-Shan and Tam, Matthew K},
  title={Method of alternating projections for the general absolute value equation},
  journal={Journal of Fixed Point Theory and Applications},
  volume={25},
  number={1},
  pages={39},
  year={2023},
}
```

## :gear: Setup
Install [Python](https://www.python.org/downloads/).
```shell
pip install numpy scipy
```

## :books: Example Usage
```shell
python main.py
```
This main funciton reads an AVE (absolute value equation) problem and solves it by MAP (methods of alternating projections).

```shell
Ground truth solution:
 [ 0.79232154 -0.71950182  0.10807229 -0.78284852  0.34448019 -0.43753243
  0.31884527  0.45398923  0.53729498 -0.78451811]

iterations: 45
error: 0.00000

MAP solution:
 [ 0.79232121 -0.7195018   0.10807212 -0.78284837  0.34448028 -0.43753253
  0.31884508  0.45398945  0.53729485 -0.78451809]
```
