import pandas as pd 
import plotly
import plotly.graph_objects as go


def graph_bar(df,nombres_features='category'):

    num_in_category=df[nombres_features].value_counts()[:10]
    
    data=[go.Bar(
        x=num_in_category.index,
        y=num_in_category.values
    )]
    text_div=plotly.offline.plot(
        {
            'data':data,
            'layout':go.Layout(xaxis_tickangle=-45, title='Top 10 de categorias')
        },
        include_plotlyjs=False, 
        output_type='div'
    )
    return text_div