import numpy as np
import pandas as pd
txt = np.loadtxt('Hydrate_Info.txt')
txtDF = pd.DataFrame(txt)
txtDF.to_csv('Hydrate_Info.csv', header=0, index=False)