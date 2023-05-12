import numpy as np 

# implement your function to combine two numpy arrays 

def combination(array1, array2, axis=0):
    array1, array2 = array1.squeeze(), array2.squeeze()
    try:
        return np.concatenate((array1, array2),axis=axis)
    except ValueError as e:
        raise ValueError(f"Cannot combine arrays. Array1 shape: {array1.shape} Array2 shape: {array2.shape}, Axis: {axis}. Original error: {str(e)}") from None

if __name__ == "__main__":
    # use this for your own testing!
    a = combination(np.array([22,3]),np.arange(5))
    print(a)