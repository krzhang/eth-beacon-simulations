import matplotlib.pyplot as plt
from collections import Counter
import logging
import beacon

# logging = 0 # uncomment to turn off logging


def collect_statistics(votes):
    vote_count = []
    for vote in votes:
        vote_count += [vote[2]]

    vote_count = Counter(vote_count)

    return (vote_count[0], vote_count[1])

######
def main(num, honestFac,dishonestFac, aim, error_param, delay_param, n_simulations):
    
    if __name__ == "__main__": # log with the following format
        logging.basicConfig(level=logging.DEBUG, filename="logfile", filemode="a+",
                        format="%(asctime)-15s %(levelname)-8s %(message)s")

    # factions
    faction1 = beacon.Faction.HonestFaction(num, honestFac, aim, error_param, delay_param)
    faction2 = beacon.Faction.SmokeFaction(num, dishonestFac, aim, error_param, delay_param)

    # number of blocks reaching 2/3 consensus
    # to do: more here
    stats = [collect_statistics(beacon.play(faction1, faction2)) for _ in range(n_simulations) ] 
    
    n = 0
    for s in stats:
        if s[0] / s[1] >= 2/3 or s[1] / s[0] >= 2/3:
            n += 1

    
######
main(20, 'honest','smoke', 0.5, 0.1, 0.3, 100) 
