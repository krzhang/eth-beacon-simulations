import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
import numpy as np
from collections import Counter
import pickle
# from astropy.table import Table, Column


exec(open('beacon.py').read())
faction1 = Faction.HonestFaction(20, 'honest', 0.5, 0.1, 0.3)
faction2 = Faction.SmokeFaction(20, 'smoke', 0.5, 0.1, 0.3)

filename = 'table'
outfile = open(filename, 'wb')

n_simulations = 100


def collect_statistics(votes):
    vote_count = []
    for vote in votes:
        vote_count += [vote[2]]
    vote_count = Counter(vote_count)
    return (vote_count[0], vote_count[1])


def create_table(stats):
    dat_dtype = {
        'names': ('trial', 'v4zero', 'v4one', 'ratio'),
        'formats': ('i', 'i', 'i', 'd')}
    dat = np.zeros(n_simulations, dat_dtype)
    dat['trial'] = range(n_simulations)

    for i in range(len(stats)):
        dat['v4zero'][i] = stats[i][0]
        dat['v4one'][i] = stats[i][1]
        dat['ratio'][i] = max(stats[i])/sum(stats[i])
    return dat


stats = [collect_statistics(play(faction1, faction2))
         for _ in range(n_simulations)]
table = create_table(stats)

pickle.dump(table, outfile)
outfile.close()

# print(table)
