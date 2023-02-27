import pickle

# prizerv kr ke rkhna
# pickling a python object


# cars= ['Audi', 'BMD','Maruti Suzuki', 'Harryti Tuzuki']

# file = 'Mycar.pkl'
# fileobj = open(file, 'wb')
# pickle.dump(cars,fileobj)
# fileobj.close()

file = 'mycar.pkl'
fileobj = open(file,'rb')
mycar = pickle.load(fileobj)
print(mycar)
print(type(mycar))