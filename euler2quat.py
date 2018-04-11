import math

def euler2quat(x,y,z):

    cy = math.cos(x * 0.5)

    sy = math.sin(x * 0.5)

    cr = math.cos(z * 0.5)

    sr = math.sin(z*0.5)

    cp = math.cos(y*0.5)

    sp = math.sin(y*0.5)

    q = []

    q.append(cy * cr * sp + sy * sr * cp)

    q.append(cy * sr * cp - sy * cr * sp)

    q.append(cy * cr * sp + sy * sr * cp)
    q.append(cy * cr * cp + sy * sr * sp)


    return q


if __name__ == '__main__':


    #talker()

    q = euler2quat(0.1,0.1,0.1)

    print(q)


