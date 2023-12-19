import sys
import getopt

filename = ''
message = ''
opts, args = getopt.getopt(sys.argv[1:], "f:m:", ['filename', 'message'])

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


print(opts)
print(args)
for opt, arg in opts:
    if opt == '-f':
        filename = arg
    elif opt == '-m':
        message = arg
  
print(filename)      
print(message)      
    
    
    
# myfunc("sas",56,3.2,True,'c',KEYONE=56)

print(sys.argv)