# import pandas
import pandas as pd
# import matplotlib
import matplotlib.pyplot as plt
from matplotlib.ticker import (MultipleLocator, AutoMinorLocator)
# import seaborn
import seaborn as sns
#import numpy
import numpy as np

df = pd.read_excel('Data-Results.xlsx', sheet_name='All Data')
df = df.drop(columns=['Modeled?', 'Unnamed: 8', 'Name Select', 'Scale'])
#print(df)

dfAo = pd.read_excel('Data-Results.xlsx', sheet_name='Aortic Root')
dfAo = dfAo.drop(columns=['Unnamed: 6', 'Name Select'])
#print(dfAo)

dfAsc = pd.read_excel('Data-Results.xlsx', sheet_name='Ascending Aorta')
dfAsc = dfAsc.drop(columns=['Unnamed: 6', 'Name Select'])
#print(dfAsc)

dfTrsv = pd.read_excel('Data-Results.xlsx', sheet_name='Tranverse Aorta')
dfTrsv = dfTrsv.drop(columns=['Unnamed: 6', 'Name Select'])
#print(dfTrsv)

###########################################################################################################
# AORTIC ROOT RESULTS
###########################################################################################################
x = dfAo['Gestational Age (weeks)']
y = dfAo['Ao. Root (mm)']

plt.figure(1, figsize=(6, 5))

ax = sns.scatterplot(x=x, y= y, data=dfAo, color=".2", style="Condition", s=20)
plt.rcParams["font.family"] = "serif"

plt.legend(loc='upper left')
plt.legend(markerscale=0.7)
plt.setp(ax.get_legend().get_texts(), fontsize='8') # for legend text
plt.setp(ax.get_legend().get_title(), fontsize='8') # for legend title

plt.title('Gestational Age vs. Aortic Root Diameter')
plt.ylabel("Aortic Root Model Diameter (mm)")
plt.xlabel("Gestational Age (weeks)")

# Set up grid, legend, and limits
ax.grid(linestyle='--', linewidth=0.2)
ax.set_xticks(np.arange(21, 34, 1))  # adjust the x tick frequency
ax.set_yticks(np.arange(2, 8.5, 0.5))  # adjust the y tick frequency
ax.xaxis.set_minor_locator(MultipleLocator(0.5))
ax.yaxis.set_minor_locator(MultipleLocator(0.25))

# Set tick font size
for label in (ax.get_xticklabels() + ax.get_yticklabels()):
	label.set_fontsize(8)

m, b = np.polyfit(x, y, 1)
line = m*x + b
ci = 1.96 * np.std(y)/np.mean(y)
plt.plot(x, line-ci, 'k--', linewidth=0.5)
plt.plot(x, line, color='black', linewidth=0.5)
plt.plot(x, line+ci, 'k--', linewidth=0.5, )

plt.savefig('figures/GA-Ao.jpg', bbox_inches='tight')
plt.show()

###########################################################################################################
# ASCENDING AORTA RESULTS
###########################################################################################################
x = dfAsc['Gestational Age (weeks)']
y = dfAsc['Asc. Ao. (mm)']

plt.figure(2, figsize=(6, 5))
ax = sns.scatterplot(x=x, y= y, data=dfAsc, color=".2", style="Condition", s=20)
plt.rcParams["font.family"] = "serif"

plt.legend(loc='upper left')
plt.legend(markerscale=0.7)
plt.setp(ax.get_legend().get_texts(), fontsize='8') # for legend text
plt.setp(ax.get_legend().get_title(), fontsize='8') # for legend title

plt.title('Gestational Age vs. Ascending Aorta Diameter')
plt.ylabel("Ascending Aorta Model Diameter (mm)")
plt.xlabel("Gestational Age (weeks)")

# Set up grid, legend, and limits
ax.grid(linestyle='--', linewidth=0.2)
ax.set_xticks(np.arange(21, 34, 1))  # adjust the x tick frequency
ax.set_yticks(np.arange(2, 8.5, 0.5))  # adjust the y tick frequency
ax.xaxis.set_minor_locator(MultipleLocator(0.5))
ax.yaxis.set_minor_locator(MultipleLocator(0.25))

# Set tick font size
for label in (ax.get_xticklabels() + ax.get_yticklabels()):
	label.set_fontsize(8)

m, b = np.polyfit(x, y, 1)
line = m*x + b
ci = 1.96 * np.std(y)/np.mean(y)
plt.plot(x, line-ci, 'k--', linewidth=0.5)
plt.plot(x, line, color='black', linewidth=0.5)
plt.plot(x, line+ci, 'k--', linewidth=0.5, )

plt.savefig('figures/GA-Asc.jpg', bbox_inches='tight')
plt.show()

###########################################################################################################
# TRANVERSE AORTA RESULTS
###########################################################################################################
x = dfTrsv['Gestational Age (weeks)']
y = dfTrsv['Transv. Ao. (mm)']

plt.figure(3, figsize=(6, 5))
ax = sns.scatterplot(x=x, y= y, data=dfTrsv, color=".2", style="Condition", s=20)
plt.rcParams["font.family"] = "serif"

plt.legend(loc='upper left')
plt.legend(markerscale=0.7)
plt.setp(ax.get_legend().get_texts(), fontsize='8') # for legend text
plt.setp(ax.get_legend().get_title(), fontsize='8') # for legend title

plt.title('Gestational Age vs. Tranverse Aorta Diameter')
plt.ylabel("Tranverse Aorta Model Diameter (mm)")
plt.xlabel("Gestational Age (weeks)")

# Set up grid, legend, and limits
ax.grid(linestyle='--', linewidth=0.2)
ax.set_xticks(np.arange(21, 34, 1))  # adjust the x tick frequency
ax.set_yticks(np.arange(2, 8.5, 0.5))  # adjust the y tick frequency
ax.xaxis.set_minor_locator(MultipleLocator(0.5))
ax.yaxis.set_minor_locator(MultipleLocator(0.25))

# Set tick font size
for label in (ax.get_xticklabels() + ax.get_yticklabels()):
	label.set_fontsize(8)

m, b = np.polyfit(x, y, 1)
line = m*x + b
ci = 1.96 * np.std(y)/np.mean(y)
plt.plot(x, line-ci, 'k--', linewidth=0.5)
plt.plot(x, line, color='black', linewidth=0.5)
plt.plot(x, line+ci, 'k--', linewidth=0.5, )

plt.savefig('figures/GA-Trsv.jpg', bbox_inches='tight')
plt.show()