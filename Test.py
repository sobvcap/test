#!/usr/bin/env python
# coding: utf-8

# In[21]:


import plotly.graph_objects as go
import dash
from dash import html
import pandas as pd
import plotly.offline as pyo
from dash import dcc
import numpy as np
#from PIL import Image
import plotly.express as px
import gunicorn


# In[22]:


app = dash.Dash()
#pil_image = Image.open("Velox Symbol.png")
server = app.server
#v_symbol = html.Img(src=pil_image, style={'height':'10%', 'width':'10%', 'padding-left':'42%', 'padding-right':'27%'})
df = px.data.iris()  # iris is a pandas DataFrame
fig = px.scatter(df, x="sepal_width", y="sepal_length")


app.layout = html.Div([
                      
                      html.Div('Percentage Exposure',style= {
                              'color': 'black',
                          "bottom": "0px",
                          'text-align': 'left',
                           "font-size":"50px",
                                }),
                       
                        html.Div('GROSS NET/5D AV NET',style= {
                              'color': 'black',
                             "font-size":"50px",
                          "bottom": "10px",
                          'text-align': 'right'
                                }),
                        #dcc.Slider(0, 20, 2.5,
                         #  value=10,
                          #id='my-slider'
                           # )
                       dcc.Graph(figure=fig)

                      
                      
                      
                      
                      ])

if __name__ == '__main__':
    #serve(app,host='0.0.0.0',port=63349)
    app.run_server()


# In[ ]:




