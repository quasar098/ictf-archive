import numpy as np
np.random.seed(1337)
v=[*open('flag.txt', 'rb').read()]
save([c.0 for p in [0..len(v)-3] for _ in [1..2000] for c in (np.random.randint(0,128,(3,3))*ZZ@v[p:p+3])], 'out.sobj')