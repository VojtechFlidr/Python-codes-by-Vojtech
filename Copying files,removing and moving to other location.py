import os, shutil



#shutil.copytree('C:\\Users\\fildr\\Documents\\Python\\Today\\P01','C:\\Users\\fildr\\Documents\\Python\\Today\\P01_backup')

path01 = "C:\\Users\\fildr\\Documents\\Python\\Today\\P01"
path02 = "C:\\Users\\fildr\\Documents\\Python\\Today\\Select"
shutil. rmtree(path01)
shutil. rmtree(path02)
print("file has been deleted.")

directory = "P01"
parent_dir = "C:\\Users\\fildr\\Documents\\Python\\Today\\"
path = os.path.join(parent_dir, directory)
os.mkdir(path)
print("Directory '% s' created" % directory)

directory = "Select"
parent_dir = "C:\\Users\\fildr\\Documents\\Python\\Today\\"
path = os.path.join(parent_dir, directory)
os.mkdir(path)
print("Directory '% s' created" % directory)
