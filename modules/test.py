import numpy as np

def readFile(file_name):
    f=open(file_name,"r")
    line=f.readlines()
    return line

def writeFile(create_name,file_name):
    f=open(create_name,"w")
    f.write(str(readFile(file_name)))
    f.close()

# writeFile("write_file","../data/text8")


load_data = np.load("../data/text8.model")
print(load_data)
print("----------------------")
load_data2=np.load('../data/text8.model.trainables.syn1neg.npy')
print(load_data2)