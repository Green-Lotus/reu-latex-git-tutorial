# Copyright © 2022 Alexander L. Hayes

"""
Make some plots for the "Chicken Wing Problem"

- https://www.boredpanda.com/chicken-wing-pricing-structure-math-graps-formulas/
"""

import matplotlib.pyplot as plt
import numpy as np

chicken = np.loadtxt("chicken_wings.csv", skiprows=1, delimiter=",", dtype=float).T

per_wing = np.divide(chicken[1], chicken[0]).reshape(-1)
cheapest = np.argmin(per_wing)

_fig = plt.figure(figsize=(15, 4))
_ax1 = _fig.add_subplot(131)
_ax2 = _fig.add_subplot(132)
_ax3 = _fig.add_subplot(133)

font = {
    "family": "serif",
    "color": "darkred",
    "weight": "normal",
    "size": 16,
}

# What is the relationship between (1) Number of Chicken Wings, and (2) Price?
# Is it linear?

_ax1.set_title("Batch Price", fontdict=font)
_ax1.scatter(chicken[0], chicken[1])
_ax1.set_xlabel("Number of Wings")
_ax1.set_ylabel("Total $")

# What is the price per chicken wing at each point?

_ax2.set_title("Price per Chicken Wing", fontdict=font)
_ax2.scatter(chicken[0], per_wing)
_condition = chicken[0][per_wing == 1.112]
_ax2.scatter(_condition, [1.112, 1.112, 1.112])
_ax2.set_xlabel("Number of Wings")
_ax2.set_ylabel("$ per wing")
_ax2.text(
    50,
    1.13,
    "'{0}' is cheapest at {1:.3f} per wing".format(
        int(chicken[0][cheapest]), per_wing[cheapest]
    ),
)

# What is the cheapest way to buy 200 wings?
# We'll make a simplification and only focus on cases that evenly divide 200 (e.g. 200 = 25 * 8),
# otherwise we'll have an instance of a knapsack problem.

_ax3.set_title("Price of 200 Wings at Fixed Price", fontdict=font)

_200_wings = 200 // chicken[0].reshape(-1)
_valid_200 = 200 / chicken[0].reshape(-1) % 1 == 0

x = chicken[0][_valid_200]
y = _200_wings[_valid_200] * chicken[1][_valid_200]

_ax3.scatter(x, y)
_ax3.scatter([x[5], x[7]], [y[5], y[7]])
_ax3.text(
    50,
    223,
    "'{0}' is cheapest at {1:.2f} for 200".format(
        int(x[np.argmin(y)]), y[np.argmin(y)]
    ),
)

_ax3.set_xlabel("Number of Wings (Price fixed by Category)")
_ax3.set_ylabel("Total $ to buy 200 wings at fixed price")

# Save a copy

print("Saving a copy to `chicken_wing_plots.png`")
plt.tight_layout()
plt.savefig("chicken_wing_plots.png")
