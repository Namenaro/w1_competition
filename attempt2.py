from slayter import get_virtual_slayter_better_more, get_virtual_slayter_better_less
from html_logger import HtmlLogger
from distr import Distr, get_distr_of_max_statistics, get_distr_of_min_statistics
from enropy_coin import entropize_arr, MAX_ENTR_OF_COIN

import matplotlib.pyplot as plt
from mpl_toolkits.axisartist.axislines import SubplotZero
import statistics
import random


def fstr(num):
    return "{:.2f}".format(num)

def make_arrows(axs2):
    axs2.xaxis.set_ticks_position('bottom')
    axs2.yaxis.set_ticks_position('left')

    # make arrows
    axs2.spines['left'].set_position('zero')
    axs2.spines['right'].set_visible(False)
    axs2.spines['bottom'].set_position('zero')
    axs2.spines['top'].set_visible(False)
    axs2.xaxis.set_ticks_position('bottom')
    axs2.yaxis.set_ticks_position('left')
    axs2.plot((1), (0), ls="", marker=">", ms=10, color="k",
              transform=axs2.get_yaxis_transform(), clip_on=False)
    axs2.plot((0), (1), ls="", marker="^", ms=10, color="k",
              transform=axs2.get_xaxis_transform(), clip_on=False)

def mismatch(old, new):
    mismatches = list([abs(old[i] - new[i]) for i in range(len(old))])
    return sum(mismatches)

def get_e(old, new):
    e = abs(old - new)
    if old < new:
        return -e
    return e

def get_E(errs_old, errs_val):
    E = []
    for i in range(len(errs_old)):
        old, new = errs_old[i], errs_val[i]
        E.append(get_e(old, new))
    return E

def visualise(vals, val, index, log):

    divider = sum(vals)
    normed_vals = list([vals[i] / divider for i in range(len(vals))])
    fig, (axs, axs2) = plt.subplots(1, 2)
    #axs.plot(normed_vals, label="normed vals", color='black')

    axs.set_xlabel('index', loc='right')
    axs.set_ylim(bottom=-0.03, top=1.03)

    errs_val = list([abs(vals[i] - val) / divider for i in range(len(vals))])
    axs.plot(errs_val, label='abs ошибка предсказания', color='orange')

    default = statistics.mean(vals)
    errs_old = list([abs(vals[i] - default) / divider for i in range(len(vals))])
    axs.plot(errs_old, '--', label='старая ошибка', color='blue')

    axs.legend(fancybox=True, framealpha=0.5)

    axs2.plot(get_E(errs_old, errs_val))
    axs2.set_ylim(bottom=-1.03, top=1.03)
    make_arrows(axs2)
    log.add_fig(fig)

    log.add_text("mu = " + fstr(mismatch(errs_old, errs_val)))


def seria1():
    log = HtmlLogger("att2_log")
    vals = [3, 3, 3, 3, 3, 5]

    index = 5
    val = 5
    visualise(vals, val, index, log)

    vals = [3, 3, 3, 3, 3, 50]

    index = 5
    val = 50
    visualise(vals, val, index, log)


if __name__ == '__main__':
    seria1()
