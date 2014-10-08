import numpy as np
import pandas as pd
import graphlab

# import urllib
# import matplotlib.pyplot as plt
# from matplotlib import rcParams
# from IPython.display import display
# from IPython.display import Image
# graphlab.canvas.set_target('ipynb')
# %matplotlib inline


def get_data():
    df = pd.read_csv('data/actors.csv')
    return df

def get_sframe():
    print "boobies"
    sf = graphlab.SFrame.read_csv('data/actors.csv')
    condition = sf['actor_name'] != '[]'
    sf = sf[condition]
    sf['weight'] = 0.5
    return sf



def construct_graph():
    sf = get_sframe()
    actors = sf['actor_name'].unique()
    films = sf['film_name'].unique()
    g = graphlab.SGraph()

    # we do this twice has a hack around its default Directed graph
    # this will make it is undirected
    g = g.add_edges(sf, src_field='actor_name', dst_field='film_name')
    g = g.add_edges(sf, src_field='film_name', dst_field='actor_name')

    print "Actor vertex sample:"
    g.get_vertices(ids=actors).tail(5)

    print "Movie graph summary:\n", g.summary(), "\n"
    return g



def select_subgraph(movie1='Point Break', movie2='Shrek'):
    selection = [movie1, movie2]
    subgraph = graphlab.SGraph()
    g = construct_graph()
    extracted = g.get_edges(dst_ids = selection)
    subgraph = subgraph.add_edges(extracted, src_field='__src_id', dst_field='__dst_id')
    return subgraph
