#
# from rtlsdr examples
#
from pylab import *
from rtlsdr import *

sdr = RtlSdr()

sdr.sample_rate = 2.4e6
sdr.center_freq = 91e6
sdr.gain = 4

samples = sdr.read_samples(256*1024)
sdr.close()

psd(samples, NFFT=1024, Fs=sdr.sample_rate/1e6, Fc=sdr.center_freq/1e6)
xlabel('Frequency (MHz)')
ylabel('Relative power (db)')

show()
