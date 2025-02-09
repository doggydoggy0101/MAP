# :croissant: C++ Example 

This example shows how to use MAP in C++.

```shell
cd examples/cpp
```

## :gear: Build

```shell
mkdir build
cd build
cmake .. 
make
```

## :checkered_flag: Run

```shell
./map_example
```

This main function will generate an AVE problem and solve it with MAP.

```shell
Iterations: 163
Error: 9.54634e-07

Ground Truth:
  0.791527 -0.0492596   0.126551   0.391032  -0.721337   0.208835  0.0796822  -0.593878   0.885707   0.197731

MAP solution:
  0.791528 -0.0492595   0.126551   0.391032  -0.721336   0.208835  0.0796824  -0.593877   0.885707   0.197731
```