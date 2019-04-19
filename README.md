
# A List of Simulations 
[All contents can be modified or more simulations can be added.]

## The purpose of this list is to give an idea about how simulations have been created, based on different parameter valeus.

## Parameters:
1. N(v): The number of validators.
2. Er:   An error rate.
3. R:    A ratio between the number of dishonest and honest validators.
4. T(h): A time for honest validatators to vote.
5. T(d): A time for dishonest validators to vote.
6. Tl:   Time latency.

## A list of tables for simulations with different parameter values
|Parameters | Simulation 1         | Simulation 2         | Simulation 3         | Simulation 4         |
|:---------:|:--------------------:|:--------------------:|:--------------------:|:--------------------:|
|N(v)       |      111             |      111             |      111             |      111             |
|Er         |    (0, 0.2)          |      0.1             |      0.1             |      0.1             |
|R          |      1:2             |      1:2             |      1:2             |      1:2             |
|T(h)       |      0.5             |      0.5             |      0.5             | 0.5,0.6,0.7,0.8,0.9  |
|T(d)       |      0.5             | [0.1, 0.3, ..., 0.9] |      0.5             |      0.5             |
|Tl         |      0.3             |      0.3             |    0.3, 0.4, 0.5     |      0.3             |

What we learned through simulation 1 & 2 [04/18/2019]:
1. We ran the simulations with values of 0.05, 0.1, and 0.15 for error rate that is
  generated based on the uniform distribution.
  We learned that error rate does not affect to the winning rates.
2. We ran the simulations with values of 0.1, 0.3, 0.5, 0.7, 0.9 for T(d).
  We witnessed that 0.1, 0.3, 0.5, and 0.9 gave a reasonable and understandable results.
  Under the values of 0.1 and 0.3, we obtained that 100% winning rate.
  Under the value of 0.5, the winning rate is in between 0.9228331852972921 and 0.931766814702708.
  Under the value of 0.9, the winning rate is 100% since dishonest validators' votes
  coming almost at the end do not affect to the result.
  Under the value of 0.7, we could not interpret the result well since we expected to have 100% winning rate.

Simulation 3 & 4 would be the next assignment.
Other than these simulations, I wonder if we can modify the fixed mean value of 0.5 to another value inside of the function as the following.
 def timing_with_mean(faction, error_param, mean=0.5):
 """attests around 0.5 with error bar uniformly distributed within error_param"""
 
Also, more simualtions would be added more.
