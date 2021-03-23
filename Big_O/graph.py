from math import log
import numpy as np
import matplotlib.pyplot as plt
plt.style.use('bmh')

# Set up runtime comparsions
n = np.linspace(1,10)
labels = ["contant","logarithmic","linear","log linear","Quadratic","cubic","Exponential"]
big_o = [np.ones(n.shape), np.log(n), n,n*np.log(n),n**2,n**3,2**n]

# Plot setup
plt.figure(figsize=(12,10))
plt.ylim(0, 50)

for i in range(len(big_o)):
    plt.plot(n, big_o[i],label = labels[i])

plt.legend(loc =0)
plt.ylabel('Relative Runtime')
plt.xlabel('n')
plt.show()
from math import log
import numpy as np
import matplotlib.pyplot as plt
plt.style.use('bmh')

# Set up runtime comparsions
n = np.linspace(1,10)
# ex> np.linspace(2.0,3.0,num=5)
# array([2, 2.25, 2.5, 2.75, 3. ])
# ex1> np.linsapce(2.0, 3.0, num=5, endpoint=False)
# array([2. , 2.2, 2.4, 2.6, 2.8])
# ex2> np.linsapce(2.0, 3.0, num=5, retstep=True)
# (array([2., 2.25, 2.5, .2.75, 3. ]),0.25)

labels = ["contant","logarithmic","linear","log linear","Quadratic","cubic","Exponential"]
big_o = [np.ones(n.shape), np.log(n), n,n*np.log(n),n**2,n**3,2**n]

# Plot setup
plt.figure(figsize=(12,10))
plt.ylim(0, 50)

for i in range(len(big_o)):
    plt.plot(n, big_o[i],label = labels[i])

plt.legend(loc =0)
plt.ylabel('Relative Runtime')
plt.xlabel('n')
plt.show()

