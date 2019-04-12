import logging
import random

class Validator(object):
  def __init__(self, name, faction): # faction: byz/hon
    self.name = name
    self.faction = faction
    # self.view = {}

  def __repr__(self):
    return str(self.name)

class Faction(object):
  def __init__(self, num, name):
    self.num = num
    self.name = name
    self.timings = None
    # should return a list of (validator, slot) pairs
    self.attestation_strat = None
    self.validators = {Validator(str("%s_%d") % (name, k), self) for k in range(num)}

  @classmethod
  def HonestFaction(cls, num, name, aim, error_param, delay_param):
    f = cls(num, name)
    f.timings = timing_with_mean(f, error_param, aim)
    f.attestation_strat = (lambda v, t, f, vts:
                           attestation_honest_majority(v, t, f, vts, delay_param, flipped=False))
    return f
    
  @classmethod #returns a class method for function SmokeFaction
  def SmokeFaction(cls, num, name, aim, error_param, delay_param):
    f = cls(num, name)
    f.timings = timing_with_mean(f, error_param, aim-delay_param)
    f.attestation_strat = (lambda v, t, f, vts:
                           attestation_smokescreen())
    return f
    
def adjusted_random_time(lower, upper):
  timing = random.uniform(lower, upper)
  if timing < 0.0:
    timing = 0.0
  if timing > 0.99999:
    timing = 0.99999
  return timing

def timing_with_mean(faction, error_param, mean=0.5):
  """attests around 0.5 with error bar uniformly distributed within error_param"""
  timings = []
  for v in faction.validators:
    timing = adjusted_random_time(mean-error_param, mean+error_param)
    timings.append((v, timing))
  return timings

def attestation_honest_majority(validator, time_current, factions, votes, delay_param, flipped=False):
  seen_votes = [0, 0]
  for (v, timing, vote) in votes:
    time_received = adjusted_random_time(timing, timing + delay_param)
    logstr = "  %s voted for %s [t=%.3f; t_received=%.3f]" % (v.name, str(vote), timing, time_received)
    if (time_received < time_current):
      logstr += (" (counts)")
      seen_votes[vote] += 1
    logging.info(logstr)
  if seen_votes[0] >= seen_votes[1]:
    vote = 0
  else:
    vote = 1
  if flipped:
    vote = 1 - vote
  return vote # help

def attestation_smokescreen():
  return random.choice([0,1])
  
def play(faction1, faction2):
  factions = (faction1, faction2)
  timings = []
  for f in factions:
    timings += f.timings
  timings.sort(key = lambda x: x[1])
  votes = []
  for t in timings:
    v = t[0]
    time = t[1]
    f = v.faction
    logging.info("%s votes [t=%.3f]" % (v.name, time))
    vote = f.attestation_strat(v, time, factions, votes)
 #    v.vote = vote
 #   v.vote_time = t[1]
    logging.info("%s votes %s" % (v.name, str(vote)))

    votes.append((v, time, vote))    
  return votes

def main():
  #format logging file
  if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG, filename="logfile", filemode="a+",
                        format="%(asctime)-15s %(levelname)-8s %(message)s")
    
  # Run simulation with 20 honest validators attesting at .5, 10 dishonest
  #validators attesting at .5-.3, with network latency .1
  boo = Faction.HonestFaction(20, "Honest", 0.5, 0.1, 0.3)
  poo = Faction.SmokeFaction(10, "Dishonest", 0.5, 0.1, 0.3)
  play(boo, poo)


### Run ###
main()
