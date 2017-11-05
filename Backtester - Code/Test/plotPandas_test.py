import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
plt.style.use('ggplot')
web_stats = {'Day':[1,2,3,4,5,6],
             'Visitors':[43,34,65,56,29,76],
             'Bounce Rate':[65,67,78,65,45,52]}



df = pd.DataFrame(web_stats)
for b in df:
