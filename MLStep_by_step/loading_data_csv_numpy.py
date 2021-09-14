from numpy import loadtxt

path=r"C:\Akash Files\Machine_Learnings\MLStep_by_step\pima-indians-diabetes.csv"
datapath= open(path, 'r')
data = loadtxt(datapath, delimiter=",")
print(data.shape)
print(data[:3])