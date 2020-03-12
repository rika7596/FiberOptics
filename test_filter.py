import numpy as np

from filter import Filter


def test_filter():
    time = 2*np.pi*(2*np.arange(1000)/1000 - 1)
    signal = np.exp(-(2*time)**2)
    noisy_signal = signal + 0.05*np.random.normal(size=1000)
    filtered_signal = Filter(threshold=5).apply(noisy_signal)
    diff = np.sum(np.abs(signal - np.real(filtered_signal)))/(time[-1] - time[0])
    assert diff < 1.0
