from django.shortcuts import render
from django.http import HttpResponse

from .utils import RunGraph
from .utils import DbQuery
import pandas as pd 

def home(request):
    categories = DbQuery.get_categories()
    categories_df = pd.DataFrame(categories)
    graph_div = RunGraph.graph_bar(categories_df)
    categories_count = categories_df['category'].value_counts()
    values_list = categories_count.values.tolist()
    index_list = categories_count.index.tolist()
    context = {
        'graph_div': graph_div,
        'categories_count': [list(x) for x in zip(index_list, values_list)]
    }
    return render(request, 'dashboard/home.html', context)


def about(request):
    return render(request, 'dashboard/about.html')
