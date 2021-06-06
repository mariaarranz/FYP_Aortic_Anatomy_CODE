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
from scipy.stats import ttest_rel
import pingouin as pt

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
# AORTIC ROOT
###########################################################################################################
expectedAo = dfAo['Exp. Ao. Root (mm)']
actualAo = dfAo['Ao. Root (mm)']
errorAo = dfAo['Error Ao. Root']

# Python paired sample t-test:
tTest = pt.ttest(expectedAo, actualAo, paired=True)
print(tTest)
tTest.reset_index(drop=True, inplace=True)

t = tTest.iloc[0]['T']
dof = tTest.iloc[0]['dof']
tail = tTest.iloc[0]['tail']
pval = tTest.iloc[0]['p-val']
ci = tTest.iloc[0]['CI95%']
cohen = tTest.iloc[0]['cohen-d']
bf10 = tTest.iloc[0]['BF10']
power = tTest.iloc[0]['power']

# calculate Pearson's correlation
corrAo, _ = pearsonr(expectedAo, actualAo)
print('Pearsons correlation Ao. Root: %.4f' % corrAo)

with open('comparison_data.txt', 'w') as outfile:
    outfile.write('--------------------------------------------------------------------------------\n')
    outfile.write('  Aortic Root Diameter Comparison between Expected and Model Measurements \n')
    outfile.write('--------------------------------------------------------------------------------\n')
    outfile.write('# PAIRED SAMPLE T-TEST: ')
    outfile.write('\n\nT-value: ' + str(t))
    outfile.write('\nDegrees of Freedom: ' + str(dof))
    outfile.write('\nType of tail: ' + str(tail))
    outfile.write('\np-value: ' + str(pval))
    outfile.write('\n95% Confidence Interval: ' + str(ci))
    outfile.write('\nCohen’s D: ' + str(cohen))
    outfile.write('\nBayes Factor: ' + str(bf10))
    outfile.write('\nPower: ' + str(power))
    outfile.write('\n\n# PEARSONS CORRELATION: '+ str(corrAo) + '\n')

###########################################################################################################
# ASCENDING AORTA
###########################################################################################################
expectedAsc = dfAsc['Exp. Asc. Ao. (mm)']
actualAsc = dfAsc['Asc. Ao. (mm)']
errorAsc = dfAsc['Error Asc. Ao']

# Python paired sample t-test:
tTest = pt.ttest(expectedAsc, actualAsc, paired=True)
print(tTest)
tTest.reset_index(drop=True, inplace=True)

t = tTest.iloc[0]['T']
dof = tTest.iloc[0]['dof']
tail = tTest.iloc[0]['tail']
pval = tTest.iloc[0]['p-val']
ci = tTest.iloc[0]['CI95%']
cohen = tTest.iloc[0]['cohen-d']
bf10 = tTest.iloc[0]['BF10']
power = tTest.iloc[0]['power']

# calculate Pearson's correlation
corrAsc, _ = pearsonr(expectedAsc, actualAsc)
print('Pearsons correlation Asc. Ao.: %.4f' % corrAsc)

with open('comparison_data.txt', 'a') as outfile:
    outfile.write('\n--------------------------------------------------------------------------------\n')
    outfile.write('  Ascending Aorta Diameter Comparison between Expected and Model Measurements \n')
    outfile.write('--------------------------------------------------------------------------------\n')
    outfile.write('# PAIRED SAMPLE T-TEST: ')
    outfile.write('\n\nT-value: ' + str(t))
    outfile.write('\nDegrees of Freedom: ' + str(dof))
    outfile.write('\nType of tail: ' + str(tail))
    outfile.write('\np-value: ' + str(pval))
    outfile.write('\n95% Confidence Interval: ' + str(ci))
    outfile.write('\nCohen’s D: ' + str(cohen))
    outfile.write('\nBayes Factor: ' + str(bf10))
    outfile.write('\nPower: ' + str(power))
    outfile.write('\n\n# PEARSONS CORRELATION: '+ str(corrAsc) + '\n')

###########################################################################################################
# TRANVERSE AORTA
###########################################################################################################
expectedTrsv = dfTrsv['Exp. Transv. Ao. (mm)']
actualTrsv = dfTrsv['Transv. Ao. (mm)']
errorTrsv = dfTrsv['Error Transv. Ao.']

# Python paired sample t-test:
tTest = pt.ttest(expectedTrsv, actualTrsv, paired=True)
print(tTest)
tTest.reset_index(drop=True, inplace=True)

t = tTest.iloc[0]['T']
dof = tTest.iloc[0]['dof']
tail = tTest.iloc[0]['tail']
pval = tTest.iloc[0]['p-val']
ci = tTest.iloc[0]['CI95%']
cohen = tTest.iloc[0]['cohen-d']
bf10 = tTest.iloc[0]['BF10']
power = tTest.iloc[0]['power']

# calculate Pearson's correlation
corrTrsv, _ = pearsonr(expectedTrsv, actualTrsv)
print('Pearsons correlation Asc. Ao.: %.4f' % corrTrsv)

with open('comparison_data.txt', 'a') as outfile:
    outfile.write('\n--------------------------------------------------------------------------------\n')
    outfile.write('  Tranverse Aorta Diameter Comparison between Expected and Model Measurements \n')
    outfile.write('--------------------------------------------------------------------------------\n')
    outfile.write('# PAIRED SAMPLE T-TEST: ')
    outfile.write('\n\nT-value: ' + str(t))
    outfile.write('\nDegrees of Freedom: ' + str(dof))
    outfile.write('\nType of tail: ' + str(tail))
    outfile.write('\np-value: ' + str(pval))
    outfile.write('\n95% Confidence Interval: ' + str(ci))
    outfile.write('\nCohen’s D: ' + str(cohen))
    outfile.write('\nBayes Factor: ' + str(bf10))
    outfile.write('\nPower: ' + str(power))
    outfile.write('\n\n# PEARSONS CORRELATION: '+ str(corrTrsv) + '\n')

#########################################################################################################
# BOXPLOTS 
#########################################################################################################

dfExpAo = dfAo.sort_values(by ='Exp. Ao. Root (mm)', ascending=False).assign(Type='Exp. Root')
dfActAo = dfAo.sort_values(by ='Ao. Root (mm)', ascending=False).assign(Type='Measured Root')
dfao_v = dfAo.drop(columns=['Name', 'Gestational Age (weeks)', 'Condition', 'Error Ao. Root'])
ao_values = list(dfao_v.columns) 

dfExpAsc = dfAsc.sort_values(by ='Exp. Asc. Ao. (mm)', ascending=False).assign(Type='Exp. Asc.')
dfActAsc = dfAsc.sort_values(by ='Asc. Ao. (mm)', ascending=False).assign(Type='Measured Asc.')
dfasc_v = dfAsc.drop(columns=['Name', 'Gestational Age (weeks)', 'Condition', 'Error Asc. Ao'])
asc_values = list(dfasc_v.columns) 

dfExpTrsv = dfTrsv.sort_values(by ='Exp. Transv. Ao. (mm)', ascending=False).assign(Type='Exp. Trsv.')
dfActTrsv = dfTrsv.sort_values(by ='Transv. Ao. (mm)', ascending=False).assign(Type='Measured Trsv.')
dftrsv_v = dfTrsv.drop(columns=['Name', 'Gestational Age (weeks)', 'Condition', 'Error Transv. Ao.'])
trsv_values = list(dftrsv_v.columns) 

cdf = pd.concat([dfExpAo, dfActAo, dfExpAsc, dfActAsc, dfExpTrsv, dfActTrsv])
values = ao_values + asc_values + trsv_values
#print(cdf)    

data = pd.melt(cdf, id_vars=['Type'], value_vars= values)
#print(data)    

plt.figure(1, figsize=(6, 5))
plt.rcParams["font.family"] = "serif"

bplot = sns.boxplot(y='value', x='Type', data=data, width=0.5)
bplot = sns.stripplot(y='value', x='Type', data=data, jitter=True, marker='o', alpha=0.8, size=2, color="black")

types = ['Exp. Root', 'Measured Root', 'Exp. Asc.', 'Measured Asc.', 'Exp. Transv.', 'Measured Transv.']
type_colors=["mediumvioletred","mediumvioletred","deeppink","deeppink","pink","pink"]
color_dict = dict(zip(types, type_colors))

for i in range(0,6):
    mybox = bplot.artists[i]
    mybox.set_facecolor(color_dict[types[i]])

# Set tick font size
for label in (bplot.get_xticklabels() + bplot.get_yticklabels()):
	label.set_fontsize(8)

plt.title('Measurements Comparison Boxplot')
plt.ylabel(("Diameter (mm)"))
bplot.set_yticks(np.arange(2, 8.5, 0.5))  # adjust the y tick frequency

plt.savefig('figures/measurements_boxplot.jpg', bbox_inches='tight')
plt.show()

