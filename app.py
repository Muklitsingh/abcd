#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().system('pip install flask')


# In[2]:


from flask import Flask 


# In[3]:


box=Flask(__name__)
@box.route('/')
def xyz():
    return 'Hello'
box.run()


# In[9]:


from flask import Flask,render_template
box=Flask(__name__)
@box.route('/')
def xyz():
    return render_template('d:final.html')
box.run()


# In[17]:


from flask import Flask,render_template,request
app=Flask (__name__)
@app.route('/')
def xyz():
    return render_template('d:final.html')
@app.route('/info',methods=['POST'])
def abc():
    if (request.method=='POST'):
        name=request.form['n']
        gen=request.form['g']
        city=request.form['s']
        print(name,gen,city)
        return render_template('d:final.html') 
app.run()


# In[4]:


from flask import Flask,render_template,request
app=Flask (__name__)
@app.route('/')
def xyz():
    return render_template('d:num.html')
@app.route('/info',methods=['POST'])
def abc():
    if (request.method=='POST'):
        num1=int(request.form['a'])
        num2=int(request.form['b'])
        o=num1+num2
        return render_template('d:num.html',total=o) 
app.run()


# In[ ]:




