def mnk_val(x,y):
    x = np.array(x)
    y = np.array(y)
    t = (x*y).mean() - x.mean()*y.mean()
    b = (x*x).mean() - x.mean()**2
    t = float(t)
    b = float(b)
    return t/b

def err(x,y,k):
    x = np.array(x)
    y = np.array(y)
    t = (y*y).mean() - y.mean()**2
    b = (x*x).mean() - x.mean()**2
    t = float(t)
    b = float(b)
    return sqrt((t/b - k*k)/len(x))

def mnk_b(x,y,k):
    x = np.array(x)
    y = np.array(y)
    return y.mean() - k*x.mean()