import numpy as np

def prison(prisoners):
    turn_on = [False] * prisoners
    monitor = prisoners - 1
    num = 1
    lamp = False
    while num < prisoners:
        lamp,num = selct(prisoners,monitor,turn_on,lamp,num)
    print("all prisoners turned on")

def selct(prisoners, monitor, turn_on, lamp, num):
    luck = np.random.randint(0, prisoners)
    print("luck:", luck)
    if luck == monitor:
        if lamp:
            lamp = False
            num += 1
    else:
        if not lamp:
            if not turn_on[luck]:
                lamp = True
                turn_on[luck] = True
    print("num:", num, "lamp:", lamp)
    return lamp,num



if __name__ == "__main__":
    prison(4)