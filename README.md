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
 [ 0.81005809 -0.77100042  0.68213848 -0.18953776 -0.61816125 -0.57135878
 -0.56756155 -0.05847529  0.71471428  0.70013865]

iterations: 27
error: 0.00000

MAP solution:
 [ 0.8100581  -0.77100037  0.68213846 -0.18953777 -0.6181612  -0.57135876
 -0.56756155 -0.05847524  0.71471431  0.70013858]
```
