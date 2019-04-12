import matplotlib.pyplot as plt
from collections import Counter

exec(open('beacon.py').read())
faction1 = Faction.HonestFaction(20, 'honest', 0.5, 0.1, 0.3)
faction2 = Faction.SmokeFaction(20, 'smoke', 0.5, 0.1, 0.3)

n_simulations = 100

stats = [collect_statistics(play(faction1, faction2)) for _ in range(n_simulations)]

n = 0
for s in stats:
    if s[0] / s[1] >= 2/3 or s[1] / s[0] >= 2/3:
        n += 1
print(n)


def collect_statistics(votes):
    vote_count = []
    for vote in votes:
        vote_count += [vote[2]]

    vote_count = Counter(vote_count)

    return (vote_count[0], vote_count[1])


