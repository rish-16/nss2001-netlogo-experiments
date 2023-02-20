import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.DataFrame(pd.read_csv("../data/albedo-vs-temp.csv")).values.tolist()

alb = np.array([r[0] for r in df])
air_temp = np.array([r[1] for r in df])
ground_temp = np.array([r[2] for r in df])
air_temp_std = np.array([r[3] for r in df])
ground_temp_std = np.array([r[4] for r in df])

plt.plot(alb, air_temp, color="green", label="Mean Air Temp")
plt.fill_between(alb, air_temp-air_temp_std, air_temp+air_temp_std, alpha=0.4, color="green")

plt.plot(alb, ground_temp, color="red", label="Mean Ground Temp")
plt.fill_between(alb, ground_temp-ground_temp_std, ground_temp+ground_temp_std, alpha=0.4, color="red")

plt.grid()
plt.xlabel("Albedo")
plt.ylabel("Temperature (deg C)")
plt.legend()
plt.show()