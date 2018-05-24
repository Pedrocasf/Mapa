
# coding: utf-8

# In[226]:


import pandas as pd


# In[227]:


from folium import plugins


# In[228]:


from folium.plugins import HeatMap


# In[209]:


brasil = folium.Map(location=[-16.1237611,-59.9219642], zoom_start=4)


# In[210]:


data = [[-19.7952526, -43.9089615],[-19.7937563,-43.9084187]]


# In[211]:


folium.CircleMarker(location=[-19.7947807, -43.9075329],radius='30',color='red').add_to(brasil)


# In[212]:


folium.Marker(location=[-19.7947807, -43.9075329]).add_to(brasil)


# In[213]:


HeatMap(data,radius='100').add_to(brasil)


# In[214]:


brasil

