import plotly.express as px
import pandas as pd

app = Dash(__name__)

df = pd.read_csv("mockdata.csv")
df['date'] = pd.to_datetime(df.date)
df['year'] = df['date'].dt.year
df = df.reset_index().set_index(['date'],append=True)
df.sort_index(inplace=True, ascending=True)

grouped_data = df.groupby(['year', 'functional_area']).size().reset_index(name='count')

fa = df['functional_area'].unique().tolist()

fig = px.bar(grouped_data, x='year',y='count',color='functional_area',
             title='SIRs by Year and Functional Area',
             labels={'count': 'Count','year':'Year'},
             category_orders={"functional_area": fa})

fig.update_layout(barmode='group')
fig.show()
