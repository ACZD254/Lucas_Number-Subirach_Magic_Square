import time
import matplotlib.pyplot as plt

def lucas(n):
    if n==0:
        return 2
    elif n==1:
        return 1
    else:
        return lucas(n-1)+lucas(n-2)

def main():
    time_list = []
    x_axis=[]
    for i in range (40):
        delta_time = get_lucas_time(i)
        time_list.append(delta_time)
        x_axis.append(i)
        print("n = {a}, time = {b}".format(a=i,b=delta_time))
    ratio=[]
    range
    for j in range(21,(len(time_list)-1)):
        ratio.append(time_list[j]/time_list[j-1])

    print(ratio)

    plt.plot(x_axis,time_list)
    plt.show()

def get_lucas_time(n):
    start=time.time()
    lucas(n)
    end = time.time()
    delta_time = end-start
    return delta_time

main()
