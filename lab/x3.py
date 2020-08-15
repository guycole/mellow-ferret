from rtlsdr import RtlSdr

sdr = RtlSdr()

print(sdr.get_device_serial_addresses())
print(sdr.get_gains())

# 5 = RTLSDR_TUNER_R820T
print(sdr.get_tuner_type())

print(sdr.init_device_values())

sdr.sample_rate = 2.048e6
sdr.center_freq = 91e6
sdr_freq_correction = 0
sdr.gain = 'auto'

print(sdr.read_samples())
