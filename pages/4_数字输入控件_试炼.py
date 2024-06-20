import streamlit as st

st.header("数字输入控件试炼")
st.caption(" 包含 : st.number_input、st.slider")

st.header("演示①：st.number_input数字输入与展示")

code = st.number_input("请输入：", 
                       min_value=0,value=None, 
                       max_value=100, 
                       step=10,
                       placeholder="请输入100以内的数字")

st.write("你输入的数字是：", code)

st.code("""

# 演示①st.checkbox 源码

import streamlit as st
        
code = st.number_input("请输入：", 
                       min_value=0,value=None, 
                       max_value=100, 
                       step=10,
                       placeholder="请输入100以内的数字")

st.write("你输入的数字是：", code)

""")
st.divider()

st.header("演示②：st.slider 数字滑块")

work_time = st.slider("请选择今日加班时长", 
                      min_value=0, 
                      max_value=10, 
                      value=2, 
                      step=1,
                      format="%d 小时")
if work_time < 2:
    st.write("加班", work_time,"小时,"," 工作当然没有身体重要！")
elif work_time >= 2 and work_time <= 5:
    st.write("加班", work_time, "小时,", "敬你是条汉子！")
elif work_time > 5:
    st.write("加班",work_time, "小时,", "公司是老板的，命是自己的！保重啊！！！")

st.code('''

# 演示②st.slider 源码
import streamlit as st
        
work_time = st.slider("请选择今日加班时长", 
                      min_value=0, 
                      max_value=10, 
                      value=2, 
                      step=1,
                      format="%d 小时")
if work_time < 2:
    st.write("加班", work_time,"小时,"," 工作当然没有身体重要！")
elif work_time >= 2 and work_time <= 5:
    st.write("加班", work_time, "小时,", "敬你是条汉子！")
elif work_time > 5:
    st.write("加班",work_time, "小时,", "公司是老板的，命是自己的！保重啊！！！")

''')

values = st.slider(
    "Select a range of values",
    0.0, 100.0, (25.0, 75.0))
st.write("Values:", values)


from datetime import datetime

start_time = st.slider(
    "When do you start?",
    value=datetime(2020, 1, 1, 9, 30),
    format="MM/DD/YY - hh:mm")
st.write("Start time:", start_time)