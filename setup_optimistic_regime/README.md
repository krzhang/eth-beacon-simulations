# Simulation cases for Optimistic Regime
[All contents can be modified or more simulations can be added.]

## The purpose of this list is to give an idea about how simulations have been created, based on different parameter values.

## Parameters:
1. N(v): The number of validators.
2. Er:   An error rate.
3. R:    A ratio between the number of dishonest and honest validators.
4. T(h): A time for honest validatators to vote.
5. T(d): A time for dishonest validators to vote.
6. Tl:   Time latency.

## A list of tables of simulations with different parameter values for optimistic cases
|Parameters | Simulation 1         | Simulation 2         | Simulation 3         | Simulation 4         | Simulation 5       |
|:---------:|:--------------------:|:--------------------:|:--------------------:|:--------------------:|:------------------:|
|N(v)       |      111             |         111          |                  |                      |                    |
|Er         |       0              |          0           |                  |                      |                    |
|R          |      1:2             |         1:2          |                  |                      |                    |
|T(h)       |      0.5             |         0.5          |                  |                      |                    |
|T(d)       |      0.5             | [0.6, 0.7, 0.8, 0.9] |                  |                      |                    |
|Tl         |       0              |          0           |                  |                      |                    |

1. Delay (=time latency) = error rate = 0
  - Tl = Er = 0 --> Simulation 1

2. Simulation 2
  - [aim - delay_param] - error_param > 0
  - This setup is designed after we obtained some delightful insight through the simulation 2 under the Pessimistic Regime.
  
#### Next Assginment.
1. simulate one case, analyze, and interpret data.
2. create more simulations if needed.
