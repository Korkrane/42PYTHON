from curses.panel import new_panel
import numpy as np


class ScrapBooker:

    # spb.crop(arr1, (3, 1), (1, 0))
    def crop(self, array, dim, position=(0, 0)):
        """
        Crops the image as a rectangle via dim arguments (being the new height
        and width of the image) from the coordinates given by position arguments.
        Args:
        -----
        array: numpy.ndarray
        dim: tuple of 2 integers.
        position: tuple of 2 integers.
        Return:
        -------
        new_arr: the cropped numpy.ndarray.
        None (if combinaison of parameters not compatible).
        Raise:
        ------
        This function should not raise any Exception.
        """
        if isinstance(dim, tuple)\
            and isinstance(position, tuple)\
            and isinstance(array, np.ndarray)\
            and len(dim) == 2\
            and len(dim) == 2\
            and all(type(i) == int and i >= 0 for i in dim)\
                and all(type(i) == int and i >= 0 for i in position):
            # http://omz-software.com/pythonista/numpy/reference/arrays.indexing.html#:~:text=Negative%20indices%20are%20interpreted%20as,including%20using%20a%20step%20index).
            new_arr = array[position[0]:dim[0] + position[0], position[1]:dim[1] + position[1]]
            return new_arr
        return None

    def thin(self, array, n, axis):
        """
        Deletes every n-th line pixels along the specified axis (0: Horizontal, 1: Vertical)
        Args:
        -----
        array: numpy.ndarray.
        n: non null positive integer lower than the number of row/column of the array
        (depending of axis value).
        axis: positive non null integer.
        Return:
        -------
        new_arr: thined numpy.ndarray.
        None (if combinaison of parameters not compatible).
        Raise:
        ------
        This function should not raise any Exception.
        """
        if isinstance(array, np.ndarray)\
            and isinstance(n, int)\
            and n > 0\
            and isinstance(axis, int)\
                and axis == 1 or axis == 0:
            new_arr = np.delete(array, slice(2, None, 3), axis)
            return new_arr
        return None

    # https://stackoverflow.com/questions/43561622/merge-two-numpy-arrays
    def juxtapose(self, array, n, axis):
        """
        Juxtaposes n copies of the image along the specified axis.
        Args:
        -----
        array: numpy.ndarray.
        n: positive non null integer.
        axis: integer of value 0 or 1.
        Return:
        -------
        new_arr: juxtaposed numpy.ndarray.
        None (combinaison of parameters not compatible).
        Raises:
        -------
        This function should not raise any Exception.
        """
        if isinstance(array, np.ndarray)\
            and isinstance(n, int)\
            and isinstance(axis, int)\
                and axis == 1 or axis == 0:
            if n > 0:
                new_arr = np.concatenate((array, array), axis)
                return new_arr
        return None

    def mosaic(self, array, dim):
        """
        Makes a grid with multiple copies of the array. The dim argument specifies
        the number of repetition along each dimensions.
        Args:
        -----
        array: numpy.ndarray.
        dim: tuple of 2 integers.
        Return:
        -------
        new_arr: mosaic numpy.ndarray.
        None (combinaison of parameters not compatible).
        Raises:
        -------
        This function should not raise any Exception.
        """
        if isinstance(array, np.ndarray)\
            and isinstance(dim, tuple)\
            and all(type(i) == int for i in dim)\
                and len(dim) == 2:
            new_arr = np.tile(array, (dim[0], dim[1], 1))
            return new_arr
        return None


spb = ScrapBooker()

arr1 = np.arange(0,25).reshape(5,5)
print(spb.crop(arr1, (3,1),(1,0)))

arr2 = np.array("A B C D E F G H I".split() * 6).reshape(-1,9)
print(spb.thin(arr2,3,1))

arr3 = np.array([[var] * 10 for var in "ABCDEFG"])
print(spb.thin(arr3,3,0))

arr4 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(spb.juxtapose(arr4, 2, 0))

not_numpy_arr = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(spb.crop(not_numpy_arr, (1, 2)))
print(spb.juxtapose(arr4, -2, 0))
print(spb.mosaic(arr4, (1, 2, 3)))
