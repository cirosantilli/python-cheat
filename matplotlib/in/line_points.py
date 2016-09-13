#!/usr/bin/env python
def plot(plt, params):
    fig, axs = plt.subplots(2, 2)
    axs[0, 0].plot([0, 1], linestyle='-')
    axs[0, 0].set_title('-')
    axs[1, 0].plot([0, 1], linestyle='--')
    axs[1, 0].set_title('--')
