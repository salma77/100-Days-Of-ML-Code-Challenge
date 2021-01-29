#!/usr/bin/env python
# coding: utf-8

# In[1]:


import torch
import torch.nn as nn
import numpy as np

def seq_model_to_sim(model):
    params = []
    model_shape = []
    for layer in model:
        if isinstance(layer,nn.Linear):
            params.extend(layer.weight.data.numpy().reshape(-1).tolist())
            params.extend(layer.bias.data.numpy().reshape(-1).tolist())
            model_shape.append(layer.weight.shape[0])
    
    print("Model shape: {}".format(model_shape[:-1]))
    to_print = ""
    for b in params:
        to_print += "{:.4f},".format(b)
    print("Model weights: {}".format(to_print[:-1]))


# In[ ]:




