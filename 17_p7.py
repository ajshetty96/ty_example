with open("log.txt")as f:
    content= f.read()
    if ("python"in content):
        print("python is absent 1 2")
    else:
        print("python not present") 