import numpy as np
import matplotlib.pyplot as plt

t = np.linspace(0, 40, 1000)

#Distance travelled by Robber: d = 2.5*t
d_r = 2.5 * t

#Distance travelled by Sherriff when Robber is caught: s = 3*(t-5)
d_s = 3 * (t-5)

fig, ax = plt.subplots()
plt.title('A Bank robber is caught')
plt.xlabel('Time in minutes')
plt.ylabel('Distance in Km')
ax.set_xlim([0, 40])
ax.set_ylim([0, 120])
ax.plot(t, d_r, c='red', label='Robber')
ax.plot(t, d_s, c='blue', label='Sheriff') 

plt.axvline(x=30, color='purple', linestyle='--')
_ = plt.axhline(y=75, color='purple', linestyle='--')
plt.show()