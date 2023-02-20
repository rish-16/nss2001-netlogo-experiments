import pandas as pd
import numpy as np

T = 250
df = pd.DataFrame(pd.read_csv("../data/temperature-3forests.csv")).values.tolist()[T:]

air_temp = np.array([r[1] for r in df])
ground_temp = np.array([r[2] for r in df])
albedo = 0.25

print ("average air temp:", np.mean(air_temp))
print ("stddev air temp:", np.std(air_temp))

print ("average ground temp:", np.mean(ground_temp))
print ("stddev ground temp:", np.std(ground_temp))