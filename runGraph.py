from pymongo import MongoClient
import pandas as pd 

client = MongoClient("localhost", 27017)
gobDb = client["GoBDB"]
jobCollection = gobDb["Jobs"]

features = jobCollection.aggregate([
    {
        '$project': {
            'category': '$attributes.category_name',
            'title': '$attributes.title',
            'tags': '$attributes.tags.data',
            'seniority': '$attributes.seniority.data.attributes.name'
        }
    }
])

list_features=[*features]
df=pd.DataFrame(list_features)

def graph_bar(df,nombres_features=['category']):
    import pandas as pd 
    import plotly
    import plotly.graph_objects as go

    num_in_category=df[nombres_features].value_counts()[:10]
    
    data=[go.Bar(
        x=num_in_category.index,
        y=num_in_category.values
    )]
    text_div=plotly.offline.plot(
        {'data':data,'layout':go.Layout(xaxis_tickangle=-45)},
        include_plotlyjs=False, output_type='div'
    )
    return text_div