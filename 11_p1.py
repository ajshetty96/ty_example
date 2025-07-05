with open("poem.txt")as f:
    content= f.read()
    if ("twinkle" in content):
        print("Contains twinkle")
    else:
        print("Does not contain twinkle")
        