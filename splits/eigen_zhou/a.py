file_train = open('D:/Workspace/Code/Python/MDE/monodepth2/splits/eigen_zhou/val_files.txt',"r")
test = open("D:/Workspace/Code/Python/MDE/monodepth2/splits/eigen_zhou/tmp.txt", "w")
lines = file_train.readlines()

for line in lines:
  if "2011_09_28/2011_09_28" in line:
    test.write(line)