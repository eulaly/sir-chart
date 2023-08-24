import plotly.express as px
import pandas as pd

df = pd.read_csv("mockdata.csv")
df['date'] = pd.to_datetime(df.date)
df['year'] = df['date'].dt.year
df = df.reset_index().set_index(['date'],append=True)
df.sort_index(inplace=True, ascending=True)

def run(df, var:str):
    grouped_data = df.groupby(['year',var]).size().reset_index(name='count')

    cat = df[var].unique().tolist()
    
    fig = px.bar(grouped_data, x='year',y='count',color=var,
             title=f'SIRs by Year and {var.title()}',
             labels={'count': 'Count','year':'Year'},
             category_orders={"status": cat})
    fig.update_layout(barmode='group')
    fig.show()

if __name__ == "__main__":
    run(df, var='functional_area')
    
