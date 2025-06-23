""" Simulation for very, actives permutation
"""

import numpy as np

n_very = 74
n_actives = 48
n_total = 258

very_not = np.repeat([1, 0], [n_very, n_total - n_very])

n_iters = 1000000
very_actives = np.zeros(n_iters)
for i in range(n_iters):
    some_verys = np.random.choice(very_not, n_actives, replace=False)
    very_actives[i] = np.sum(some_verys)

simulations = np.reshape(very_actives, (-1, 1000))
means = np.mean(simulations, axis=1)
print('Min, max of means', np.min(means), np.max(means))
stds = np.std(simulations, axis=1)
print('Min, max of stds', np.min(stds), np.max(stds))

"""
Example output:

Min, max of means 13.488 14.048
Min, max of stds 2.624957142507283 3.0425482740623857
"""
