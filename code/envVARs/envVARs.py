
import os
def get(getAll=False,**kwargs):
    reCx = {}
    for arg in kwargs:
        reCx[arg] = os.environ.get(arg,kwargs[arg])
    if getAll:
        for arg in os.environ:
            if arg not in reCx:
                reCx[arg] = os.environ.get(arg)
    
    return reCx
