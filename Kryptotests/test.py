import os
filename = os.getcwd() + '/testTest'
print filename
def ensure_dir(f):
    d = os.path.dirname(f)
    print d
    if not os.path.exists(d):
        os.makedirs(d)
# ensure_dir(filename)
help(os.path.exists)
help(os.makedirs)

