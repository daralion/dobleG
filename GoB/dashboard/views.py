from django.shortcuts import render
from django.http import HttpResponse

from .utils import RunGraph
from .utils import DbQuery
import pandas as pd 

def home(request):
    categories = DbQuery.get_categories()
    categories_df = pd.DataFrame(categories)
    graph_cat = RunGraph.graph_bar(categories_df)
    categories_count = categories_df['category'].value_counts()
    values_list = categories_count.values.tolist()
    index_list = categories_count.index.tolist()

    seniority = DbQuery.get_seniority()
    seniority_df = pd.DataFrame(seniority)
    graph_sen = RunGraph.graph_pie(seniority_df)

    category_and_seniority = DbQuery.get_categories_and_seniorities()
    cat_and_sen_df = pd.DataFrame(category_and_seniority)
    graph_cat_and_sen = RunGraph.graph_bar3(cat_and_sen_df)

    context = {
        'data': [
            {
                'graph_div': graph_cat,
                'categories_count': [list(x) for x in zip(index_list, values_list)]
            },
            {
                'graph_div': graph_sen
            },
            {
                'graph_div': graph_cat_and_sen
            },

        ]   
    }
    return render(request, 'dashboard/home.html', context)


def selection(request):
    categories = DbQuery.get_categories()
    data = DbQuery.get_categories_and_seniorities()
    data2 = DbQuery.get_categories_and_tags()
    categories_df = pd.DataFrame(categories)
    top_10_categories = categories_df['category'].value_counts()[:10].index.tolist()


    index = 0
    if request.method == 'POST':
        index = int(request.POST['categories']) - 1

    selected_category = top_10_categories[index]
    graph = RunGraph.graph_pie2(pd.DataFrame(data), selected_category)
    tags_df = RunGraph.data_manipulation(data2, selected_category)
    graph2 = RunGraph.graph_bar2(tags_df, selected_category)

    return render(request, 'dashboard/selection.html', 
                    {
                        'categories': top_10_categories, 
                        'graph': graph, 
                        'graph2': graph2,
                        'selected_category': selected_category
                    })
