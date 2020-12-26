import matplotlib.pyplot as plt
import numpy as np
import math
import signal

def main():
    buffer = []
    sample_len = 128
    osc = signal.Oscillator(1200, 48000)
    for n in range(0, sample_len):
        buffer.append(osc.next_sample())
        print(buffer[n])
    #plt.plot(buffer, label='1200Hz')
    out = np.fft.rfft(buffer)
    psd = []
    psd.append(out[0].real)
    half = int(len(out))
    for k in range(1, half):
        psd.append(math.sqrt(out[k].real*out[k].real + out[k].imag*out[k].imag))
    psd[half-1] = math.sqrt(out[0].imag*out[0].imag + out[half-1].imag*out[half-1].imag)
    plt.plot(psd, label='FFT')
    plt.show()
main()
