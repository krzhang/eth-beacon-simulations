# Simulation cases for Pessimistic Regim
[All contents can be modified or more simulations can be added.]

## The purpose of this list is to give an idea about how simulations have been created, based on different parameter values.

## Parameters:
1. N(v): The number of validators.
2. Er:   An error rate.
3. R:    A ratio between the number of dishonest and honest validators.
4. T(h): A time for honest validatators to vote.
5. T(d): A time for dishonest validators to vote.
6. Tl:   Time latency.

## A list of tables for simulations with different parameter values
|Parameters | Simulation 0         | Simulation 1         | Simulation 2         | Simulation 3         | Simulation 4       |
|:---------:|:--------------------:|:--------------------:|:--------------------:|:--------------------:|:------------------:|
|N(v)       |      111             |      111             |      111             |      111             |      111           |
|Er         |      0.1             |    (0, 0.2)          |      0.1             |      0.1             |      0.1           |
|R          |      1:2             |      1:2             |      1:2             |      1:2             |      1:2           |
|T(h)       |      0.5             |      0.5             |      0.5             |      0.5             |[0.5, 0.6, ..., 0.9]|
|T(d)       |      0.5             |      0.5             | [0.1, 0.3, ..., 0.9] |      0.5             |      0.5           |
|Tl         |      0.3             |      0.3             |      0.3             |    0.3, 0.4, 0.5     |      0.3           |

1. Tl is a lot bigger than Er.
  - T(d) = T(h)
  - T(d) > T(h)

#### Next Assginment.
Create more simulation based on pessimistic and optimistic cases based on the section 5. The Equivocation Game.
