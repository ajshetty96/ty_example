with open("log.txt")as f:
    content= f.read()
    if ("python"in content):
        print("python is absent")
    else:
        print("python not present") 