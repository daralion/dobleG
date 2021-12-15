import pandas as pd 
import plotly
import plotly.graph_objects as go
from collections import Counter


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

def data_manipulation(list_features,name_category):
    #Creamos un diccionario con las categorias como llave y una lista vacia como valor
    dict_new={}
    for category in list_features:
        dict_new[category['category']]=[]

    #Llenamos las listas vacias con los tags que pertenecen a cada categoria
    for category in list_features:
        dict_new[category['category']]+=[info['attributes']['name'] for info in category['tags']]

    #Esto hara un recuento de los tags para una categoria en especifico
    dict_count_tags=dict(Counter(dict_new[name_category]))

    #Creacion del dataframe con los recuentos de los tags
    df_tags=pd.DataFrame([dict_count_tags], index=['Count']).transpose()
    return df_tags

def graph_bar2(df,name_category):
    sort_tags=df.sort_values('Count',ascending=False)[:15]
    
    sort_tags.values.tolist()
    list_=[]
    
    for l in sort_tags.values.tolist():
        list_+=l
        
    data=[go.Bar(
        x=sort_tags.index,
        y=list_
    )]
    text_div=plotly.offline.plot(
        {'data':data,'layout':go.Layout(xaxis_tickangle=-45, title=f'Top 15 de tags para la categoría {name_category}')},
        include_plotlyjs=False, output_type='div'
    )
    return text_div
