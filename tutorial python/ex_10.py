# https://archive.ics.uci.edu/ml/index.php

# pickle
# requests module to download the iris dataset

import requests
import pickle
import re

# Url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/iris/'
url='https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data'
iris = requests.get(url)
data = iris.text
# data = open(data, 'r')

# patt = re.compile(r'\n')

# matches = patt.finditer(data)
# for match in matches:
#     print(match)
#     print(data[0:27])

# print(data)



        
# with open (iris) as data:
#     data_set = data
#     print(data_set)

