import numpy as np

# implement the function strange pattern

def strange_pattern(tuple):
    n, m = tuple
    array = np.full((n,m),False)
    array[0::3, 0::3] = True
    array[2::3, 1::3] = True
    array[1::3, 2::3] = True

    return array

if __name__ == "__main__":
    # use this for your own testing!
    print(strange_pattern((8,8)))
    