import math

def entropize_arr(arr):
    arr_ps = list([arr[i]/sum(arr) for i in range(len(arr))])
    coined_enropies = list([entropy_coin(arr_ps[i]) for i in range(len(arr))])
    return coined_enropies

def entropy_coin(p):
   p1 = p
   p2 = 1 - p
   if p1 == 0 or p2 == 0:
      return 0
   entropy = -p1 * math.log(p1) - p2* math.log(p2)
   return entropy

MAX_ENTR_OF_COIN = entropy_coin(0.5)

