#!/usr/bin/env python
# coding: utf-8

# In[4]:


get_ipython().system('pip install Flask')
get_ipython().system('pip install werkzeug.wrappers')


# In[ ]:


from werkzeug.wrappers import Request, Response
from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return "بسم الله الرحمن الرحيم "

if __name__ == '__main__':
    from werkzeug.serving import run_simple
    run_simple('localhost', 9000, app)


# In[ ]:





# In[ ]:




