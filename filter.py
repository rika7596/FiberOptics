import numpy as np

class Filter:
    def __init__(self, threshold=0.1):
        self.threshold = threshold

    def apply(self, signal):
        spectrum = np.fft.fft(signal)
        spectrum[abs(spectrum) < self.threshold] = 0
        return np.fft.ifft(spectrum)
