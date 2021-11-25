import numpy as np

cpath = '/opt/shared/PyCharmProjects/STSGCN/data/PEMS03/'
file = cpath + 'PEMS03.npz'
data = np.load(file)
print(data.files)
print(data['data'].shape)
print(data['data'][0])
