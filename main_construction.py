# визуализация тенденций
from slayter import get_virtual_slayter_better_more
from distr import Distr, get_distr_of_min_statistics, get_distr_of_max_statistics

import matplotlib.pyplot as plt
import statistics

def mismatch(old, new):
    mismatches = list([abs(old[i] - new[i]) for i in range(len(old))])
    return sum(mismatches)/len(mismatches)

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

class Situation:
    def __init__(self, vals, val, index, default=None):
        self.vals = vals
        self.val = val
        self.index = index
        self.default = default
        if default is None:
           self.default = statistics.mean(vals)

        self.components = None
        self.indexes_new = None

    def get_w(self):
        components = []
        divider = sum(self.vals)
        errs_val = list([abs(self.vals[i] - self.val) / divider for i in range(len(self.vals))])
        errs_old = list([abs(self.vals[i] - self.default) / divider for i in range(len(self.vals))])

        win_normed = get_E(errs_old, errs_val)
        mu = mismatch(errs_old, errs_val)
        win_slayter, indexes_new = get_virtual_slayter_better_more(win_normed, self.index)
        win_distr = Distr(win_normed)
        #win_distr = Distr(get_combinatoric_win_sample(errs_val, errs_def))
        for i in range(len(win_slayter)):
            slayter_val = win_slayter[i]
            dist = abs(indexes_new[i])
            subsample_len = dist + 1
            statistic_distr = get_distr_of_max_statistics(win_distr, subsample_len)

            component = 0
            if slayter_val > 0:
                component += 1 - statistic_distr.get_p_of_event(slayter_val, statistic_distr.get_max_val())
                component*= mu
            #if slayter_val < 0:
            #    component -= 1 - statistic_distr.get_p_of_event(slayter_val, 0)
            
            components.append(component)


        w = sum(components)

        # для визуализации:
        self.components = components
        self.indexes_new = indexes_new
        return w

def get_combinatoric_win_sample(errs_val, errs_def):
    sample_elements = []
    for err_val in errs_val:
        for err_def in errs_def:
            sample_elements.append(err_def - err_val)
    return sample_elements
