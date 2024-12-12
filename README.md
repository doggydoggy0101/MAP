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
 [ 0.39941427 -0.46826008  0.93835275  0.55750181  0.43378038 -0.101277
 -0.45551688 -0.80721808  0.80520479 -0.08844742]

iterations: 38
error: 0.00000

MAP solution:
 [ 0.39941413 -0.46825992  0.93835284  0.55750177  0.4337806  -0.10127707
 -0.45551665 -0.80721786  0.8052047  -0.0884473 ]
```
