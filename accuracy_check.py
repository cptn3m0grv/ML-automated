import os

f = open("/root/cats and dogs/output.txt", "r")
acc = int(f.read(3))
f.close()

if(acc <= 85):
    os.system("python3 /root/cats\ and\ dogs/tweak.py")
else:
    print("Accuracy is good enough")




