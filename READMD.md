# Method of Alternating Projections

[![C++ Formatter](https://img.shields.io/badge/C++_Formatter-clang--format_18.1.8-blue?style=flat-square)](https://github.com/llvm/llvm-project/releases/tag/llvmorg-18.1.8)
[![Python Formatter](https://img.shields.io/badge/Python_Formatter-ruff-red?style=flat-square)](https://github.com/astral-sh/ruff)

Unofficial implementation of "Method of alternating projections for the general absolute value equation". This library is written in **C++** and we support **Python** interface. 

## :gear: Setup

The following setup is tested in Ubuntu 22.04.

### Prerequisites
```shell
sudo apt update
sudo apt install -y g++ build-essential cmake
sudo apt install -y libeigen3-dev
# python (optional)
sudo apt install -y python3 python3-dev python3-venv

git clone --recurse-submodules -j8 https://github.com/doggydoggy0101/MAP.git
cd MAP

# If you did not clone the repository with --recurse-submodules option,
# you may need to run the following command.
git submodule update --init
```

### Build

```shell
mkdir build
cd build
cmake .. 
make
```

### (optional) Build with Python binding
```shell
python3 -m venv .venv
source .venv/bin/activate
python3 -m pip install --upgrade pip
python3 -m pip install numpy

mkdir build
cd build
cmake .. -DBUILD_PYTHON=ON
make

cd python && pip install .
```

## :books: Example usages

- [:croissant: C++](examples/cpp)
- [:snake: Python](examples/python)

## :card_file_box: Reference

- [Alcantara, J. H.](https://jhalcantara.github.io/), [Chen, J. S.](https://math.ntnu.edu.tw/~jschen/), & [Tam, M. K.](https://matthewktam.com/) (2023). *Method of alternating projections for the general absolute value equation*. Journal of Fixed Point Theory and Applications, 25(1), 39.