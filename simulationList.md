# A List of Possible Simulations

## The purpose of this list is to give an idea about how simulations have been created, based on different parameter valeus.

## parameters:
1. N(v): The number of validators.
2. Er:   An error rate.
3. R:    A ratio between the number of dishonest and honest validators.
4. T(h): A time for honest validatators to vote.
5. T(d): A time for dishonest validators to vote.
6. Tl:   Time latency.

## a list of tables for simulations with different parameter values
|Parameters | simulation 1         | simulation 2 |
| --------- |:------------:        |:------------:|
|N(v)       |      111             |      111     |
|Er         |    (0, 0.2)          |      0.1     |
|R          |      1:2             |      1:2     |
|T(h)       |      0.5             |
|t(d)       | [0.1, 0.3, ..., 0.9] |
|Tl         |

What we learned today through simulation 1 [04/18/2019]:
1. We ran the simulations with values of 0.05, 0.1, and 0.15 for error rate that is
  generated based on the uniform distribution.
2. We learned that error rate does not affect to the winning rates.
