import os

source = "./task2/"
destination = "D:/R_FILES/"

for file in os.listdir(source):
    print(file)
    if(file[0].lower() == "r"):
        if not os.path.exists(destination):
            os.makedirs(destination)
        
        sourceFile = os.path.join(source, file)
        destinationFile = os.path.join(destination, file)
  
        with open(sourceFile, "r") as src:
            with open(destinationFile, "w") as dst:
                dst.write(src.read())
        