import streamlit as st

st.header("input输入控件演示：st.button")

st.header("演示①:按钮与状态改变")

if st.button("登录",key='login'):
    st.write("登录成功")
else:
    st.write("请登录")
    
st.button("重置登录状态",key='reset', type='primary')

st.code('''

# 演示案例①st.button 源码
        
import streamlit as st
        
if st.button("登录",key='login'):
    st.write("登录成功")
else:
    st.write("请登录")
    
st.button("重置登录状态",key='reset', type='primary')

''')

st.header("演示②：气球放生")

click = st.button("放生气球",key='click_btn', type='primary')

reset = st.button("气球待命",key='reset_btn', type='primary')

if click:
    result = st.write("状态：气球已放生")
    st.balloons()
if reset:
   result = st.write("状态：气球待命")

st.code('''
# 演示案例“气球放生”源码
        
click = st.button("放生气球",key='click_btn', type='primary')

reset = st.button("气球待命",key='reset_btn', type='primary')

if click:
    result = st.write("状态：气球已放生")
    st.balloons()
if reset:
   result = st.write("状态：气球待命")
        
''')
