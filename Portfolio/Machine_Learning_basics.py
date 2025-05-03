import pandas as pd
import matplotlib.pyplot as plt
import kagglehub
import numpy as np
from kagglehub import KaggleDatasetAdapter
import sklearn as sk
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

df2015 = kagglehub.dataset_load(
    KaggleDatasetAdapter.PANDAS,
    "unsdsn/world-happiness/versions/1",
    "2015.csv",
)
df2016 = kagglehub.dataset_load(
    KaggleDatasetAdapter.PANDAS,
    "unsdsn/world-happiness/versions/1",
    "2016.csv",
)

#x = 2016
#y = 2015
df_merge = df2016.merge(df2015, on='Country')
df_training = df_merge.drop(columns=['Happiness Rank_x', 'Happiness Rank_y', 'Standard Error', 'Region_x', 'Region_y', 'Lower Confidence Interval', 'Upper Confidence Interval'])
df_format = df_merge[['Country','Happiness Rank_y','Happiness Rank_x']]


df_training['Happiness Score'] = df_training[['Happiness Score_x', 'Happiness Score_y']].mean(axis=1)
df_training = df_training.drop(columns=['Happiness Score_x', 'Happiness Score_y'])

df_training['Economy (GDP per Capita)'] = df_training[['Economy (GDP per Capita)_x', 'Economy (GDP per Capita)_y']].mean(axis=1)
df_training = df_training.drop(columns=['Economy (GDP per Capita)_x', 'Economy (GDP per Capita)_y'])

df_training['Family'] = df_training[['Family_x', 'Family_y']].mean(axis=1)
df_training = df_training.drop(columns=['Family_x', 'Family_y'])

df_training['Health (Life Expectancy)'] = df_training[['Health (Life Expectancy)_x', 'Health (Life Expectancy)_y']].mean(axis=1)
df_training = df_training.drop(columns=['Health (Life Expectancy)_x', 'Health (Life Expectancy)_y'])

df_training['Freedom'] = df_training[['Freedom_x', 'Freedom_y']].mean(axis=1)
df_training = df_training.drop(columns=['Freedom_x', 'Freedom_y'])

df_training['Trust (Government Corruption)'] = df_training[['Trust (Government Corruption)_x', 'Trust (Government Corruption)_y']].mean(axis=1)
df_training = df_training.drop(columns=['Trust (Government Corruption)_x', 'Trust (Government Corruption)_y'])

df_training['Generosity'] = df_training[['Generosity_x', 'Generosity_y']].mean(axis=1)
df_training = df_training.drop(columns=['Generosity_x', 'Generosity_y'])

df_training['Dystopia Residual'] = df_training[['Dystopia Residual_x', 'Dystopia Residual_y']].mean(axis=1)
df_training = df_training.drop(columns=['Dystopia Residual_x', 'Dystopia Residual_y'])

df_format['Happiness Rank'] = df_format[['Happiness Rank_y', 'Happiness Rank_x']].mean(axis=1)
df_format = df_format.drop(columns=['Happiness Rank_y', 'Happiness Rank_x'])
#print(df_format)
#print(df_training.info())
abcis = [
    'Economy (GDP per Capita)',
    'Family',
    'Health (Life Expectancy)',
    'Freedom',
    'Trust (Government Corruption)',
    'Generosity', 
    'Dystopia Residual'
]
orden = [
    'Happiness Score'
]
X = df_training[abcis]
Y = df_training[orden]
train_X, test_X, train_Y, test_Y = train_test_split(X, Y, test_size=0.25, random_state=42)
modelo = LinearRegression()
modelo.fit(train_X, train_Y)

predict_y = modelo.predict(test_X)

mse = mean_squared_error(test_Y, predict_y)
print("mse = ", mse)

'''plt.figure(figsize=(8,6))

plt.show()'''
'''plt.style.use('ggplot')
plt.figure(figsize=(10,6))
plt.plot(df_training["Economy (GDP per Capita)"], Y, color='b', marker='*')
plt.xlabel("Economy (GDP per Capita)")
plt.ylabel("Happiness Score")
plt.title("Happiness Score X Economy (GDP per Capita)")
plt.yticks(np.arange(2.5,8,0.50))
plt.xticks(np.arange(0,2,0.125))'''
plt.style.use('ggplot')
fig, ([ax1,ax2,ax3,ax4], [ax5,ax6,ax7,ax8]) = plt.subplots(2,4, figsize=(15,10))
plt.subplots_adjust(
    left=0.065,
    bottom=0.106,
    right=0.965,
    top=0.935,
    wspace=0.38,
    hspace=0.335
)
ax1.plot(df_training["Economy (GDP per Capita)"], Y, color='b', marker='o')
ax1.set_xlabel("Economy (GDP per Capita)")
ax1.set_ylabel("Happiness Score")
ax1.set_title("Happiness Score X Economy (GDP per Capita)", fontsize=10)
ax1.text(0.10,6.5,"It looks linear.")

ax2.plot(df_training["Family"], Y, color='r', marker='o')
ax2.set_xlabel("Family")
ax2.set_ylabel("Happiness Score")
ax2.set_title("Happiness Score X Family", fontsize=10)
ax2.text(0.25,6.5,"It looks linear.")

ax3.plot(df_training["Health (Life Expectancy)"], Y, color='g', marker='o')
ax3.set_xlabel("Health (Life Expectancy)")
ax3.set_ylabel("Happiness Score")
ax3.set_title("Happiness Score X Health (Life Expectancy)", fontsize=10)
ax3.text(0,6.5,"It looks linear.")

ax4.plot(df_training["Freedom"], Y, color='y', marker='o')
ax4.set_xlabel("Freedom")
ax4.set_ylabel("Happiness Score")
ax4.set_title("Happiness Score X Freedom", fontsize=10)
ax4.text(0.1,7,"It looks linear.")

ax5.plot(df_training["Trust (Government Corruption)"], Y, color='c', marker='o')
ax5.set_xlabel("Trust (Government Corruption)")
ax5.set_ylabel("Happiness Score")
ax5.set_title("Happiness Score X Trust", fontsize=10)

ax6.plot(df_training["Generosity"], Y, color='m', marker='o')
ax6.set_xlabel("Generosity")
ax6.set_ylabel("Happiness Score")
ax6.set_title("Happiness Score X Generosity", fontsize=10)

ax7.plot(df_training["Dystopia Residual"], Y, color='k', marker='o')
ax7.set_xlabel("Dystopia Residual")
ax7.set_ylabel("Happiness Score")
ax7.set_title("Happiness Score X Dystopia Residual", fontsize=10)

ax8.scatter(test_Y, predict_y, color='blue', label='Predictions')
ax8.plot([test_Y.min(), test_Y.max()], [test_Y.min(), test_Y.max()], 'r--', label='Ideal line')
ax8.set_xlabel("Happiness Score (Real)")
ax8.set_ylabel("Happiness Score (Predict)")
ax8.set_title("Testing Linear Regression on Dataset", fontsize=10)
ax8.text(5,4, f"mse ~= {mse:.6f}", fontsize=10)
plt.legend()


plt.show()