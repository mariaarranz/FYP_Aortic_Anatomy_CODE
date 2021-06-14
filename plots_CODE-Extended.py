# import pandas
import pandas as pd
# import matplotlib
import matplotlib.pyplot as plt
from matplotlib.ticker import (MultipleLocator, AutoMinorLocator)
# import seaborn
import seaborn as sns
#import numpy
import numpy as np
from scipy.stats import pearsonr

df = pd.read_excel('Data-Results.xlsx', sheet_name='All Data')
df = df.drop(columns=['Modeled?', 'Unnamed: 8', 'Name Select', 'Scale'])
#print(df)

dfAo = pd.read_excel('Data-Results.xlsx', sheet_name='Aortic Root')
dfAo = dfAo.drop(columns=['Name Select'])
#print(dfAo)

dfAsc = pd.read_excel('Data-Results.xlsx', sheet_name='Ascending Aorta')
dfAsc = dfAsc.drop(columns=['Name Select'])
#print(dfAsc)

dfTrsv = pd.read_excel('Data-Results.xlsx', sheet_name='Tranverse Aorta')
dfTrsv = dfTrsv.drop(columns=['Name Select'])
#print(dfTrsv)

###########################################################################################################
# AORTIC ROOT RESULTS
###########################################################################################################
x = dfAo['Gestational Age (weeks)']
y = dfAo['Ao. Root (mm)']

plt.figure(1, figsize=(6, 5))

# include error bars
# example variable error bar values
dy = dfAo['Uncertainty']		

#plt.errorbar(x, y, yerr=dy, fmt='.k', capsize=5, elinewidth=0.6, markeredgewidth=0.2, linestyle="None", mfc='black', markevery=30)

ax = sns.scatterplot(x=x, y= y, data=dfAo, color="k", hue="Condition", s=25, style="Condition", palette=dict(Healthy="black", Diseased="#dd1c77"))
plt.rcParams["font.family"] = "serif"

plt.legend(loc='upper left', markerscale=0.7)
plt.setp(ax.get_legend().get_texts(), fontsize='8') # for legend text
plt.setp(ax.get_legend().get_title(), fontsize='8') # for legend title

plt.title('Gestational Age vs. Aortic Root Diameter')
plt.ylabel("Aortic Root Model Diameter (mm)")
plt.xlabel("Gestational Age (weeks)")

# Set up grid, legend, and limits
ax.grid(linestyle='--', linewidth=0.2)
ax.set_xticks(np.arange(7, 42, 2))  # adjust the x tick frequency
ax.set_yticks(np.arange(0, 9, 0.5))  # adjust the y tick frequency
ax.xaxis.set_minor_locator(MultipleLocator(0.5))
ax.yaxis.set_minor_locator(MultipleLocator(0.25))

# Set tick font size
for label in (ax.get_xticklabels() + ax.get_yticklabels()):
	label.set_fontsize(8)

plt.xlim(7,41)
plt.ylim(0,8.5)

m, b = np.polyfit(x, y, 1)
lx = pd.Series(np.array(list(range(7,42)), np.float64))
line = m*lx + b
ci = 1.96 * np.std(y)/np.mean(y)
plt.plot(lx, line-ci, 'k--', linewidth=0.5)
plt.plot(lx, line, color='black', linewidth=0.5)
plt.plot(lx, line+ci, 'k--', linewidth=0.5)
plt.fill_between(lx, line-ci, line+ci, alpha=0.1)

b = round(b, 3)
m = round(m, 3)
b = abs(b)
plt.text(22,6.25,('y = '+ str(m)+'*x - ' +str(b)), fontsize=8)

# calculate Pearson's correlation
corr, _ = pearsonr(x, y)
corr = round(corr, 3)
plt.text(22,6,('r='+ str(corr)), fontsize=8)
print('Pearsons correlation: %.3f' % corr)

plt.savefig('figures/GA-Ao2.jpg', bbox_inches='tight')
plt.show()

###########################################################################################################
# ASCENDING AORTA RESULTS
###########################################################################################################
x2 = dfAsc['Gestational Age (weeks)']
y2 = dfAsc['Asc. Ao. (mm)']

plt.figure(2, figsize=(6, 5))

# include error bars
# example variable error bar values
dy2 = dfAsc['Uncertainty']
#plt.errorbar(x2, y2, yerr=dy2, fmt='.k', capsize=5, elinewidth=0.6, markeredgewidth=0.2, linestyle="None", mfc='black', markevery=30)

ax = sns.scatterplot(x=x2, y= y2, data=dfAsc, color="k", hue="Condition", s=25, style="Condition", palette=dict(Healthy="black", Diseased="#dd1c77"))
plt.rcParams["font.family"] = "serif"

plt.legend(loc='upper left', markerscale=0.7)
plt.setp(ax.get_legend().get_texts(), fontsize='8') # for legend text
plt.setp(ax.get_legend().get_title(), fontsize='8') # for legend title

plt.title('Gestational Age vs. Ascending Aorta Diameter')
plt.ylabel("Ascending Aorta Model Diameter (mm)")
plt.xlabel("Gestational Age (weeks)")

# Set up grid, legend, and limits
ax.grid(linestyle='--', linewidth=0.2)
ax.set_xticks(np.arange(7, 42, 2))  # adjust the x tick frequency
ax.set_yticks(np.arange(0, 9, 0.5))  # adjust the y tick frequency
ax.xaxis.set_minor_locator(MultipleLocator(0.5))
ax.yaxis.set_minor_locator(MultipleLocator(0.25))

# Set tick font size
for label in (ax.get_xticklabels() + ax.get_yticklabels()):
	label.set_fontsize(8)

plt.xlim(7,41)
plt.ylim(0,8.5)

m2, b2 = np.polyfit(x2, y2, 1)
lx2 = pd.Series(np.array(list(range(7,42)), np.float64))
line = m2*lx2 + b2
ci = 1.96 * np.std(y2)/np.mean(y2)
plt.plot(lx2, line-ci, 'k--', linewidth=0.5)
plt.plot(lx2, line, color='black', linewidth=0.5)
plt.plot(lx2, line+ci, 'k--', linewidth=0.5)
plt.fill_between(lx2, line-ci, line+ci, alpha=0.1)

b2 = round(b2, 3)
m2 = round(m2, 3)
b2 = abs(b2)
plt.text(21,6.5,('y = '+ str(m2)+'*x - ' +str(b2)), fontsize=8)

# calculate Pearson's correlation
corr2, _ = pearsonr(x2, y2)
corr2 = round(corr2, 3)
plt.text(21,6.2,('r='+ str(corr2)), fontsize=8)
print('Pearsons correlation: %.3f' % corr2)

plt.savefig('figures/GA-Asc2.jpg', bbox_inches='tight')
plt.show()

###########################################################################################################
# TRANVERSE AORTA RESULTS
###########################################################################################################
x3 = dfTrsv['Gestational Age (weeks)']
y3 = dfTrsv['Transv. Ao. (mm)']

plt.figure(3, figsize=(6, 5))

# include error bars
# example variable error bar values
dy3 = dfTrsv['Uncertainty']
#plt.errorbar(x3, y3, yerr=dy3, fmt='.k', capsize=5, elinewidth=0.6, markeredgewidth=0.2, linestyle="None", mfc='black', markevery=30)

ax = sns.scatterplot(x=x3, y= y3, data=dfTrsv, color="k", hue="Condition", s=25, style="Condition", palette=dict(Healthy="black", Diseased="#dd1c77"))
plt.rcParams["font.family"] = "serif"

plt.legend(loc='upper left', markerscale=0.7)
plt.setp(ax.get_legend().get_texts(), fontsize='8') # for legend text
plt.setp(ax.get_legend().get_title(), fontsize='8') # for legend title

plt.title('Gestational Age vs. Transverse Aorta Diameter')
plt.ylabel("Transverse Aorta Model Diameter (mm)")
plt.xlabel("Gestational Age (weeks)")

# Set up grid, legend, and limits
ax.grid(linestyle='--', linewidth=0.2)
ax.set_xticks(np.arange(7, 42, 2))  # adjust the x tick frequency
ax.set_yticks(np.arange(0, 9, 0.5))  # adjust the y tick frequency
ax.xaxis.set_minor_locator(MultipleLocator(0.5))
ax.yaxis.set_minor_locator(MultipleLocator(0.25))

# Set tick font size
for label in (ax.get_xticklabels() + ax.get_yticklabels()):
	label.set_fontsize(8)

plt.xlim(7,41)
plt.ylim(0,8.5)

m3, b3 = np.polyfit(x3, y3, 1)
lx3 = pd.Series(np.array(list(range(7,42)), np.float64))
line = m3*lx3 + b3
ci = 1.96 * np.std(y3)/np.mean(y3)
plt.plot(lx3, line-ci, 'k--', linewidth=0.5)
plt.plot(lx3, line, color='black', linewidth=0.5)
plt.plot(lx3, line+ci, 'k--', linewidth=0.5)
plt.fill_between(lx3, line-ci, line+ci, alpha=0.1)

b3 = round(b3, 3)
m3 = round(m3, 3)
b3 = abs(b3)
plt.text(22,5.5,('y = '+ str(m3)+'*x - ' +str(b3)), fontsize=8)

# calculate Pearson's correlation
corr3, _ = pearsonr(x3, y3)
corr3 = round(corr3, 3)
plt.text(22,5.25,('r='+ str(corr3)), fontsize=8)
print('Pearsons correlation: %.3f' % corr3)

plt.savefig('figures/GA-Trsv2.jpg', bbox_inches='tight')
plt.show()

