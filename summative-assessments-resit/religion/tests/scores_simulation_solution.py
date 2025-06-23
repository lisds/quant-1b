""" Simulation for very, actives permutation
"""

import numpy as np

n_very = 74
n_actives = 48
n_total = 258

rescuer_scores = np.repeat([3, 2, 1, 0], [65, 79, 41, 25])
active_scores = np.repeat([3, 2, 1, 0], [9, 17, 18, 4])

n_iters = 10000000
fake_mean_diffs = np.zeros(n_iters)
pooled = np.append(rescuer_scores, active_scores)
for i in np.arange(n_iters):
    np.random.shuffle(pooled)
    fake_mean_diffs[i] = np.mean(pooled[:210]) - np.mean(pooled[210:])

simulations = np.reshape(fake_mean_diffs, (-1, 10000))
means = np.mean(simulations, axis=1)
print('Min, max of means', np.min(means), np.max(means))
stds = np.std(simulations, axis=1)
print('Min, max of stds', np.min(stds), np.max(stds))

"""
Example output:

Min, max of means -0.005554166666666677 0.006232440476190469
Min, max of stds 0.1508099396279151 0.15967022424312485
"""
