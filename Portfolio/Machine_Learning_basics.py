import pandas as pd
import matplotlib.pyplot as plt
import kagglehub
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
print(predict_y)

mse = mean_squared_error(test_Y, predict_y)
print("mse = ", mse)

plt.figure(figsize=(8,6))
plt.scatter(test_Y, predict_y, color='blue', label='Predição')
plt.plot([test_Y.min(), test_Y.max()], [test_Y.min(), test_Y.max()], 'r--', label='Linha Ideal')
plt.xlabel("Happiness Score (Real)")
plt.ylabel("Happiness Score (Predito)")
plt.title("Comparação entre Valores Reais e Preditos")
plt.legend()
plt.show()