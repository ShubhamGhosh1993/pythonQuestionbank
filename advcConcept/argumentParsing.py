import sys

def myfunc(*args,**kargs):
    print(args[0])
    print(args[1])
    print(args[2])
    print(args[3])
    print(args[4])
    print(kargs['KEYONE'])
    # print(kargs["Keytwo"])
    # print(kargs["Keythree"])
    # print(kargs["Keyfour"])
    # print(kargs["Keyfive"])
    
    
myfunc("sas",56,3.2,True,'c',KEYONE=56)

print(sys.argv)