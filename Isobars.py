import matplotlib as mpl
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

inf = 10**100
CN40 = np.linspace(12, 22, num = 11, dtype=int) #isobars withe the mass number 40
HT40 = np.array([170*10**-9, 260*10**-9, 33*10**-3, 150*10**-3, 8.8, 1.35*60, 10**100, 1.25*2.7**9*365*24*3600, 10**100, 182.3*10**-3, 53.3*10**-3]) #Times of the Half descend for the isobars with the mass number 40
CN36 = np.linspace(16, 25, num = 10, dtype=int) #isobars withe the mass number 36
HT36 = np.array([180*10**-9, 3.9*10**-3, 90*10**-3, 450*10**-3, 5.6, 10**100, 3.01*2.7**5*365*24*3600, 10**100, 341*10**-3, 101.2*10**-3]) #Times of the Half descend for the isobars with the mass number 36

IsobarMass40 = [['Mg', 'Al', 'Si', 'P', 'S', 'Cl', 'Ar', 'K', 'Ca', 'Sc', 'Ti'], CN40, HT40]
IsobarMass36 = [['Na', 'Mg', 'Al', 'Si', 'P', 'S', 'Cl', 'Ar', 'K', 'Ca'], CN36, HT36]

df40 = pd.DataFrame(IsobarMass40, index=['Isobar', 'MassNumber', 'TimeOfHalfDescence'])
df36 = pd.DataFrame(IsobarMass36, index=['Isobar', 'MassNumber', 'TimeOfHalfDescence'])



#fig = plt.figure()


plt.plot(CN40, HT40, linestyle='-', marker='o', label = u'A = 40', color='r')
plt.plot(CN36, HT36, linestyle='-', marker='o', label = u'A = 36', color='b')
#plt.title('Dependence ')
plt.yscale('log')
plt.grid(True)
plt.legend(loc='upper left')
gridsize=(10,10)

plt.xlabel('Charge numbers of the isobars with the mass number 40')
plt.ylabel('Time of the hals descence, s')
#save('pic_12_1_1', fmt='png')
#save('pic_12_1_1', fmt='pdf')

plt.vlines(18, 0, 10**14, linestyle=':', colors='r')
plt.vlines(20, 0, 10**14, linestyle=':', colors='r')
plt.vlines(21, 0, 10**14, linestyle=':', colors='b')
plt.vlines(23, 0, 10**14, linestyle=':', colors='b')

plt.show()