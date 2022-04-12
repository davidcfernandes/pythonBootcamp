#one.py

def func():
    print("FUNC() IN ONE.PY")

print("TOP LEVEL IN ONE.PY")

def func1():
    pass
def func1():
    pass

if __name__=="__main__":
#    print("ONE.PY is being run directly!")
#else:
#    print("ONE.PY has been importated!")
    #RUN THE SCRIPT
    func1()
    func2()