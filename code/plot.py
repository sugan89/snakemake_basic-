import pandas as pd
import plotly.express as px

#reading the dataframe 
file = r'output\new.csv'
output_file = r'output\SecCSV.csv'
print(file)
df = pd.read_csv(file)
df_poscon = df['poscon'].value_counts().rename_axis('Number of poscon').reset_index(name='Number of plates')
df_plot = df_poscon.head(10)
df_plot.to_csv(output_file)

#if not df_plot.empty:
#print('File read and processed')

#Plotting

fig = px.bar(x=df_plot['Number of poscon'], y=df_plot['Number of plates'])
fig.update_xaxes(title='Number of poscon', categoryorder = 'total ascending')
fig.update_yaxes(title='Plate count')
#fig.write_image(output_file)
fig.show()
