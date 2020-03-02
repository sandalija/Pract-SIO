import numpy as np 

DATA = "test.csv"
INVALID_DATA = 100000

# https://docs.scipy.org/doc/numpy/reference/generated/numpy.loadtxt.html#numpy.loadtxt

"""
dades = np.loadtxt(open(DATA, "rb"), delimiter=";", skiprows=1)
dades = np.delete(dades, (0), axis=0)
"""

file_content_aux = [[]]
f = open(DATA, "r")
file_content = f.read().split()
for i in range(0, len(file_content)):
    file_content[i] = file_content[i].split(';')
    file_content[i].pop(0)

dades = np.matrix(file_content)

dades = np.delete(dades, (0), axis = 0)
dades = dades.astype(np.float)

mean = dades.mean()
# mean_clean = dades[dades != 1].mean()

mean_clean = np.nanmean(np.where(dades == INVALID_DATA, np.nan, dades))

print(dades)
print(mean, mean_clean)

f.close()


