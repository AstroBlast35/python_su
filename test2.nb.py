# coding: utf-8
import matplotlib.pyplot as plt
from astropy import units as u
plt.ion()
b = [23, 45, 88] * u.second
c = [1, 1, 1] * u.meter
c = [3, 7, 10] * u.meter
plt.figure()
plt.plot(b, c, 'og', ls='')
plt.xlabel('seconds')
plt.ylabel('distance')
plt.savefig('test.png')
print("Done; figure saved")
