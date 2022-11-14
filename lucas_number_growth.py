import time

def lucas(n):
    if n==0:
        return 2
    elif n==1:
        return 1
    else:
        return lucas(n-1)+lucas(n-2)

def main():
    for i in range (40):
        delta_time = get_lucas_time(i)
        print("n = {a}, time = {b}".format(a=i,b=delta_time))
    
def get_lucas_time(n):
    start=time.time()
    lucas(n)
    end = time.time()
    delta_time = end-start
    return delta_time

main()
