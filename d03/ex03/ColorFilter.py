import numpy as np

class ColorFilter:
    def invert(self, array):
        """
        Inverts the color of the image received as a numpy array.
        Args:
        -----
        array: numpy.ndarray corresponding to the image.
        Return:
        -------
        array: numpy.ndarray corresponding to the transformed image.
        None: otherwise.
        Raises:
        -------
        This function should not raise any Exception.
        """
        if isinstance(array, np.ndarray) is False:
            return None
        arr = np.copy(array)
        for row in arr:
            for px in row:
                px[0], px[1], px[2] = 1 - px[0], 1 - px[1], 1 - px[2]
        return arr

    def to_blue(self, array):
        """
        Applies a blue filter to the image received as a numpy array.
        Args:
        -----
        array: numpy.ndarray corresponding to the image.
        Return:
        -------
        array: numpy.ndarray corresponding to the transformed image.
        None: otherwise.
        Raises:
        -------
        This function should not raise any Exception.
        """
        if isinstance(array, np.ndarray) is False:
            return None
        arr = np.copy(array)
        for row in arr:
            for px in row:
                px[0], px[1] = 0, 0
        return arr

    def to_green(self, array):
        """
        Applies a green filter to the image received as a numpy array.
        Args:
        -----
        array: numpy.ndarray corresponding to the image.
        Return:
        -------
        array: numpy.ndarray corresponding to the transformed image.
        None: otherwise.
        Raises:
        -------
        This function should not raise any Exception.
        """
        if isinstance(array, np.ndarray) is False:
            return None
        arr = np.copy(array)
        for row in arr:
            for px in row:
                px[0], px[2] = 0, 0
        return arr

    def to_red(self, array):
        """
        Applies a red filter to the image received as a numpy array.
        Args:
        -----
        array: numpy.ndarray corresponding to the image.
        Return:
        -------
        array: numpy.ndarray corresponding to the transformed image.
        None: otherwise.
        Raises:
        -------
        This function should not raise any Exception.
        """
        if isinstance(array, np.ndarray) is False:
            return None
        arr = np.copy(array)
        for row in arr:
            for px in row:
                px[1], px[2] = 0, 0
        return arr

    # https://www.delftstack.com/fr/howto/python/convert-image-to-grayscale-python/
    def to_grayscale(self, array, filter, **kwargs):
        """
        Applies a grayscale filter to the image received as a numpy array.
        For filter = 'mean'/'m': performs the mean of RBG channels.
        For filter = 'weight'/'w': performs a weighted mean of RBG channels.
        Args:
        -----
        array: numpy.ndarray corresponding to the image.
        filter: string with accepted values in ['m','mean','w','weight']
        weights: [kwargs] list of 3 floats where the sum equals to 1,
        corresponding to the weights of each RBG channels.
        Return:
        -------
        array: numpy.ndarray corresponding to the transformed image.
        None: otherwise.
        Raises:
        -------
        This function should not raise any Exception.
        """
        if isinstance(array, np.ndarray) is False:
            return None
        if filter == 'm' or filter == 'mean':
            R, G, B = array[:,:,0], array[:,:,1], array[:,:,2]
            imgGray = 0.2989 * R + 0.5870 * G + 0.1140 * B
            return imgGray
        elif filter == 'w' or filter == 'weight':
            if len(kwargs.keys()) != 1 or 'weights' not in kwargs.keys():
                return None
            weights = kwargs['weights']
            if isinstance(weights, list) is False:
                return None
            elif len(weights) != 3:
                return None
            for x in weights:
                if isinstance(x, float) is False:
                    return None
            R, G, B = array[:,:,0], array[:,:,1], array[:,:,2]
            imgGray = weights[0] * R + weights[1] * G + weights[2] * B
            return imgGray
        else:
            return None
