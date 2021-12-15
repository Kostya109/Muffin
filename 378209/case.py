#место для твоего кода
import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv('menu.csv')
df.info()
print(df.head)

1.
print('Проверим гипотезу в какой категории больше всего кальция')
result_Item_Breakfast = df[df['Category']=='Egg McMuffin']['Calcium (% Daily Value)'].mean()
result_Item_Breakfast = df[df['Category']=='Sausage McMuffin']['Calcium (% Daily Value)'].mean()
print('Результат Egg McMuffin:', round(result_Item_Breakfast, 2))
print('Результат Sausage McMuffin:', round(result_Item_Breakfast, 2))

print('Кальция в Egg McMuffin: 3%.Кальция в Sausage McMuffin: 15%.')


2.
print('Проверим гипотезу в какой категории больше всего железа')
result_Item_Breakfast = df[df['Category']=='Egg McMuffin']['Iron (% Daily Value)'].mean()
result_Item_Breakfast = df[df['Category']=='Sausage McMuffin']['Iron (% Daily Value)'].mean()
print('Результат Egg McMuffin:', round(result_Item_Breakfast, 2))
print('Результат Sausage McMuffin:', round(result_Item_Breakfast, 2))

print('Железа в Egg McMuffin: 19%.Железа в Sausage McMuffin: 16%.')

3.
print('Проверим гипотезу в какой категории больше всего холестерина')
result_Item_Breakfast = df[df['Category']=='Egg McMuffin']['Iron (% Daily Value)'].mean()
result_Item_Breakfast = df[df['Category']=='Sausage McMuffin']['Iron (% Daily Value)'].mean()
print('Результат Egg McMuffin:', round(result_Item_Breakfast, 2))
print('Результат Sausage McMuffin:', round(result_Item_Breakfast, 2))

print('Холестерина в Egg McMuffin: 70%.Холестерина в Sausage McMuffin: 65%.')


4.
print('Проверим гипотезу в какой категории больше всего натрия')
result_Item_Breakfast = df[df['Category']=='Egg McMuffin']['Iron (% Daily Value)'].mean()
result_Item_Breakfast = df[df['Category']=='Sausage McMuffin']['Iron (% Daily Value)'].mean()
print('Результат Egg McMuffin:', round(result_Item_Breakfast, 2))
print('Результат Sausage McMuffin:', round(result_Item_Breakfast, 2))

print('Натрия в Egg McMuffin:27%.Натрия в Sausage McMuffin:28%.')


df['Category'].value_counts().plot(kind = 'pie')

plt.show()


print('Вывод: категории Coffe & Tea больше всего.Затем идет категория Breakfast.Ну и на 3 месте расположилась категория Smoothies & Shakes.')











