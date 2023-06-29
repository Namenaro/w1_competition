# визуализация тенденций
from slayter import get_virtual_slayter_better_more
from distr import Distr, get_distr_of_min_statistics, get_distr_of_max_statistics

import matplotlib.pyplot as plt
import statistics

class Situation:
    def __init__(self, vals, val, index, default=None):
        self.vals = vals
        self.val = val
        self.index = index
        self.default = default
        if default is None:
           self.default = statistics.mean(vals)

    def get_w(self):
        components = []
        errs_val = list([abs(self.vals[i] - self.val) for i in range(len(self.vals))])
        errs_def = list([abs(self.vals[i] - self.default) for i in range(len(self.vals))])
        win = list([errs_def[i] - errs_val[i] for i in range(len(self.vals))])

        win_slayter, indexes_new = get_virtual_slayter_better_more(win, self.index)
        win_distr = Distr(win)
        for i in range(len(win_slayter)):
            slayter_val = win_slayter[i]
            dist = abs(indexes_new[i])
            subsample_len = dist + 1
            statistic_distr = get_distr_of_max_statistics(win_distr, subsample_len)
            if slayter_val >= 0:
                profit = statistic_distr.get_p_of_event(left=0, right=slayter_val)
                components.append(profit)
            else:
                defeat = -statistic_distr.get_p_of_event(left=slayter_val, right=0)
                components.append(defeat)

        w = sum(components)
        return w


