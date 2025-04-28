import pandas as pd
data = pd.read_csv('data\owid-energy-data.csv') 
selected_columns = ['country', 'year','electricity_demand']

data = data[selected_columns]
for column in data.columns[2:]:  
    data[column] = data.groupby('country')[column].transform(lambda x: x.fillna(x.mean()))
data.fillna(0, inplace=True)
data['year'] = data['year'].astype(int)
data.to_csv('data\cleaned_final_data.csv', index=False)
print("Data cleaning complete'.")
