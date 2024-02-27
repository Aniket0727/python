try:
    f=open("demofile.txt")
    f.write("Hello World")
except:
    print("Something went wrong when writing to a file")
finally:
    f.close()
    print("File closed")
