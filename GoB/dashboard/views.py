from django.shortcuts import render
from django.http import HttpResponse

from .utils import RunGraph
from .utils import DbQuery
import pandas as pd 

def home(request):
    categories = DbQuery.get_categories()
    categories_df = pd.DataFrame(categories)
    graph_div = RunGraph.graph_bar(categories_df)
    context = {'graph_div': graph_div}
    return render(request, 'dashboard/home.html', context)


def about(request):
    return render(request, 'dashboard/about.html')
