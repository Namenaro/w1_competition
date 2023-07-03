from slayter import get_virtual_slayter_better_more, get_virtual_slayter_better_less
from html_logger import HtmlLogger
from distr import Distr ,  get_distr_of_max_statistics , get_distr_of_min_statistics
from enropy_coin import entropize_arr, MAX_ENTR_OF_COIN
from main_construction import Situation


import matplotlib.pyplot as plt
import statistics
import random

def float_to_str(num):
   return "{:.2f}".format(num)

def draw_situation(vals, val, index, default, axs):
    axs.set_title('исходная ситуация:')
    axs.plot(vals, 'o-', label='vals', color="black")
    axs.set_xlim(left=0)
    y_min = min([0, min(vals)] )
    axs.set_ylim(bottom=y_min, top=max(vals) + 1)
    axs.vlines(x=index, ymin=0, ymax=val, colors='orange', lw=4, label='предсказание')
    plt.axhline(y=default, color='blue', linestyle='--', label="предсказание из-вне")
    axs.set_xlabel('index', loc='right')
    axs.legend(fancybox=True, framealpha=0.5)

def draw_errors(vals, val, index, default, axs):
    errs_val = list([abs(vals[i]-val) for i in range(len(vals))])
    axs.plot(errs_val, '-s', label='abs ошибка предсказания', color='orange')
    axs.set_xlim(left=0)

    #axs.vlines(x=index, ymin=0, ymax=val, colors='orange', lw=4, label='предсказание')

    errs_def = list([abs(vals[i] - default) for i in range(len(vals))])
    axs.plot(errs_def, '-s',label='abs ошибка внешнего предсказания', color='blue')
    y_min = min([0, min(vals), min(errs_val), min(errs_def)])
    #axs.set_ylim(bottom=y_min)#, top=max(vals) + 1)
    #plt.legend(fontsize=8, loc='upper center', bbox_to_anchor=(0.5, 1.2))
    axs.set_xlabel('index', loc='right')
    axs.plot(vals, 'o-', label='vals', color="black")

    axs.legend(fancybox=True, framealpha=0.5)

def draw_win(vals, val, index, default, axs):
    errs_val = list([abs(vals[i] - val) for i in range(len(vals))])
    errs_def = list([abs(vals[i] - default) for i in range(len(vals))])
    win = list([errs_def[i] - errs_val[i] for i in range(len(vals))])
    axs.plot(win, label='выигрыш нового предсказания от-но старого (больше - лучше)', color='red')
    axs.scatter(index, 0, color='orange', lw=4, label='предсказание')
    axs.legend(fancybox=True, framealpha=0.5)
    axs.grid(which='major', axis='both', linestyle='--', alpha=0.75)

def draw_combinatoric_distr_of_win(vals, val, index, default, axs):
    errs_val = list([abs(vals[i] - val) for i in range(len(vals))])
    errs_def = list([abs(vals[i] - default) for i in range(len(vals))])
    sample_elements = []
    for err_val in errs_val:
        for err_def in errs_def:
            sample_elements.append(err_def - err_val)

    axs.hist(sample_elements, label="комбинаторная гистограмма выигрыша", alpha=0.5, color='red')
    axs.legend(fancybox=True, framealpha=0.5)
    axs.grid(which='major', axis='both', linestyle='--', alpha=0.75)
    axs.set_xlabel('значение выигрыша (больше лучше)', loc='right')

def draw_hists_of_def_val_errs(vals, val, index, default, axs):
    errs_val = list([abs(vals[i] - val) for i in range(len(vals))])
    errs_def = list([abs(vals[i] - default) for i in range(len(vals))])
    axs.hist(errs_def, label="гистограмма ошибки старого предсказания", color='blue', alpha=0.3)
    axs.hist(errs_val, label="гистограмма ошибки НОВГО предсказания", color='orange', alpha=0.3)
    axs.set_xlabel('значение ошибки (меньше лучше)', loc='right')
    axs.legend(fancybox=True, framealpha=0.5)
    axs.grid(which='major', axis='both', linestyle='--', alpha=0.75)


def draw_slayter(vals, val, index, default, axs):
    errs_val = list([abs(vals[i] - val) for i in range(len(vals))])
    errs_def = list([abs(vals[i] - default) for i in range(len(vals))])
    win = list([errs_def[i] - errs_val[i] for i in range(len(vals))])

    win_slayter, indexes_new = get_virtual_slayter_better_more(win, index)
    axs.plot(indexes_new, win_slayter, label='вирт.Слейтер фронт выигрыша (больше - лучше)', color='red')
    axs.grid(which='major', axis='both', linestyle='--', alpha=0.75)
    axs.legend(fancybox=True, framealpha=0.5)
    axs.set_xlabel('новый индекс (0 - точка предсказания)', loc='right')

def draw_entropised_win(vals, val, index, default, axs):
    errs_val = list([abs(vals[i] - val) for i in range(len(vals))])
    errs_def = list([abs(vals[i] - default) for i in range(len(vals))])
    win = list([errs_def[i] - errs_val[i] for i in range(len(vals))])
    entropised_win = entropize_arr(win)

    axs.plot(entropised_win, label='ошибка как список энтропий монет', color='grin')

    axs.set_ylim(bottom=-0.05, top=1.05)
    axs.set_xlabel('index', loc='right')
    axs.legend(fancybox=True, framealpha=0.5)


def draw_w_components(vals, val, index, default, axs):
    situation = Situation(vals, val, index)
    w = situation.get_w()
    print("w= " + str(w))

    axs.plot(situation.components, label="компоненты w для каждой точки")
    axs.grid(which='major', axis='both', linestyle='--', alpha=0.75)
    axs.set_xlabel('новый индекс (0 - точка предсказания)', loc='right')
    axs.legend(fancybox=True, framealpha=0.5)



def visualise(vals, val, index, default, name="LOG изуализация на одном экземпляре"):
    log = HtmlLogger(name)
    log.add_text("бассейн " + str(vals) + ", point = " + str(index) + ", val = "+ str(val) + ", const_default: " +  str(default))

    fig, axs = plt.subplots()
    draw_situation(vals, val, index, default, axs)
    log.add_fig(fig)

    fig, axs = plt.subplots()
    draw_errors(vals, val, index, default, axs)
    log.add_fig(fig)

    fig, axs = plt.subplots()
    draw_win(vals, val, index, default, axs)
    log.add_fig(fig)

    fig, axs = plt.subplots()
    draw_hists_of_def_val_errs(vals, val, index, default, axs)
    log.add_fig(fig)

    fig, axs = plt.subplots()
    draw_combinatoric_distr_of_win(vals, val, index, default, axs)
    log.add_fig(fig)

    fig, axs = plt.subplots()
    draw_slayter(vals, val, index, default, axs)
    log.add_fig(fig)

    fig, axs = plt.subplots()
    #draw_entropised_win(vals, val, index, default, axs)
    draw_w_components(vals, val, index, default, axs)
    log.add_fig(fig)




if __name__ == '__main__':
    vals = [3, 3, 3, 3, 3, 5]

    index = 5
    val = 5

    default = statistics.mean(vals)

    visualise(vals, val, index, default, name='5')

    vals = [3, 3, 3, 3, 3, 50]

    index = 5
    val = 50

    default = statistics.mean(vals)
    visualise(vals, val, index, default, name='50')
