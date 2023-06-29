
def better_more(val1, val2):
    if val1> val2:
        return True
    return False


def better_less(val1, val2):
    if val1 < val2:
        return True
    return False

def get_virtual_slayter(arr, index, v1_better_val2):
    # больше - лучше
    # перебираем левее на начиная с ближайших индексов
    etalon = arr[index]
    i = index
    lefts_arr = []

    current_best = etalon
    while True:
        new_index_in_arr = i - 1
        if new_index_in_arr < 0:
            break
        new_value = arr[new_index_in_arr]
        if v1_better_val2(new_value, current_best):
            current_best = new_value
        lefts_arr.append(current_best)
        i = new_index_in_arr
    lefts_arr = list(reversed(lefts_arr))
    lefts_coords = list(range(-len(lefts_arr), 0))

    # перебираем левее на начиная с ближайших индексов
    i = index
    rights_arr = []
    current_best = etalon
    while True:
        new_index_in_arr = i + 1
        if new_index_in_arr == len(arr):
            break
        new_value = arr[new_index_in_arr]
        if v1_better_val2(new_value, current_best):
            current_best = new_value
        rights_arr.append(current_best)
        i = new_index_in_arr
    right_coords = list(range(1, len(rights_arr)+1))

    best_errs_left_rigt = lefts_arr + [etalon] + rights_arr
    new_coords = lefts_coords + [0] + right_coords
    return best_errs_left_rigt, new_coords



def get_virtual_slayter_better_more(arr, index):
    v1_better_val2 = better_more
    slayter_vals, new_coords = get_virtual_slayter(arr, index, v1_better_val2)
    return slayter_vals, new_coords

def get_virtual_slayter_better_less(arr, index):
    v1_better_val2 = better_less
    slayter_vals, new_coords = get_virtual_slayter(arr, index, v1_better_val2)
    return slayter_vals, new_coords