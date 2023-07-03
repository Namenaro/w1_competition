from slayter import get_virtual_slayter_better_more, get_virtual_slayter_better_less
from html_logger import HtmlLogger
from distr import Distr ,  get_distr_of_max_statistics , get_distr_of_min_statistics
from enropy_coin import entropize_arr, MAX_ENTR_OF_COIN


import matplotlib.pyplot as plt
import statistics
import random

def float_to_str(num):
   return "{:.2f}".format(num)

def draw_situation(vals, val, index, default, axs):
    axs.set_title('исходная ситуация:')
    axs.plot(vals, 'o-', label='vals', color="black")
    axs.set_xlim(left=0)


    axs.vlines(x=index, ymin=0, ymax=val, colors='orange', lw=4, label='новое предсказание')
    plt.axhline(y=default, color='blue', linestyle='--', label="старое предсказание")
    axs.set_xlabel('index', loc='right')


    errs_val = list([abs(vals[i] - val) for i in range(len(vals))])
    axs.plot(errs_val, '-s', label='ошибка нового предсказания', color='orange')
    axs.set_xlim(left=0)


    errs_def = list([abs(vals[i] - default) for i in range(len(vals))])
    axs.plot(errs_def, '-s', label='ошибка старого предсказания', color='blue')

    win = list([errs_def[i] - errs_val[i] for i in range(len(vals))])
    axs.plot(win, label='выигрыш нового предсказания от-но старого (больше - лучше)', color='red')
    axs.legend(fancybox=True, framealpha=0.5)

if __name__ == '__main__':
    log = HtmlLogger("LOG-compare")


    vals = [3, 3, 3, 3, 3, 5]
    index = 5
    val = 5
    default = statistics.mean(vals)
    log.add_text(
        "бассейн " + str(vals) + ", point = " + str(index) + ", val = " + str(val) + ", const_default: " + str(default))
    fig, axs = plt.subplots()
    draw_situation(vals, val, index, default, axs)
    log.add_fig(fig)


    vals = [3, 3, 3, 3, 3, 50]
    index = 5
    val = 50
    default = statistics.mean(vals)
    log.add_text(
        "бассейн " + str(vals) + ", point = " + str(index) + ", val = " + str(val) + ", const_default: " + str(default))
    fig, axs = plt.subplots()
    draw_situation(vals, val, index, default, axs)
    log.add_fig(fig)


    vals = [3, 3, 3, 3, 3, 50]
    index = 5
    val = 1
    default = statistics.mean(vals)
    log.add_text(
        "бассейн " + str(vals) + ", point = " + str(index) + ", val = " + str(val) + ", const_default: " + str(default))

    fig, axs = plt.subplots()
    draw_situation(vals, val, index, default, axs)
    log.add_fig(fig)


