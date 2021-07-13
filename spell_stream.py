#!/usr/bin/env python
# coding: utf-8

# In[1]:


from gingerit.gingerit import GingerIt
import streamlit as st


# In[3]:


st.title('Spell Checker')
text = st.text_area("Enter Text : ", value = '', height = None, max_chars=None, key = None)


# In[4]:


parser = GingerIt()


# In[5]:


if st.button('Correct Sentence'):
    if text == '':
        st.write('Enter text for checking ')
        
        
    else:
        result_dict = parser.parse(text)
        st.markdown('Corrected Sentence : '+str(result_dict["result"]))

else: 
    pass 


# In[ ]:




