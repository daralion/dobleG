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


def graph_pie(df,nombres_features='seniority'):
    num_in_features=df[nombres_features].value_counts()[:10]
    
    data=[go.Pie(
        labels = num_in_features.index,
        values = num_in_features.values, textinfo='label+percent',
                insidetextorientation='radial'
    )]

    text_div=plotly.offline.plot(
        {
            'data':data,
            'layout':go.Layout(title='Porcentaje de seniority')
        }, 
        include_plotlyjs=False, output_type='div'
    )
    return text_div

    
def graph_pie2(df,name_category,nombres_features=['category','seniority']):
    elim=df['category'].value_counts()[-4:].index.tolist()
    df_new=df[~df['category'].isin(elim)]
    df_groupby=df_new.groupby(nombres_features).size()
    count_seniority=df_groupby[name_category]
    data=[go.Pie(
        labels = count_seniority.index,
        values = count_seniority.values, textinfo='label+percent',
                insidetextorientation='radial'
    )]

    text_div=plotly.offline.plot(
        {'data':data,'layout':go.Layout(title=f'Porcentaje de Seniority por {name_category}')},
        include_plotlyjs=False, output_type='div'
    )
    return text_div

