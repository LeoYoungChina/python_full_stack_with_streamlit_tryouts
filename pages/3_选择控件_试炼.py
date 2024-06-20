import streamlit as st

st.header("SELECTIONS选择器演示：st.checkbox、st.color_picker、st.multiselect")

st.header("st.checkbox演示：选中状态改变")

if st.checkbox("选中/未选中"):
    st.write("状态：选中")
else:
    st.write("状态：未选中")

st.code('''
# 演示案例②st.checkbox 源码
import streamlit as st
        
if st.checkbox("选中/未选中"):
    st.write("状态：选中")
else:
    st.write("状态：未选中")
''')

st.divider()

st.header("st.color_picker演示：颜色选择器")

color = st.color_picker('选择颜色', '#00f900')

st.write(f"颜色：{color}")

st.code('''
# 演示案例③st.color_picker 源码
import streamlit as st
        
color = st.color_picker('选择颜色', '#00f900')

st.write(f"颜色：{color}")
''')

st.divider()

st.header("st.multiselect演示：多选控件")

options = st.multiselect(
    "你曾经去过哪些地方？",
    ["故宫", "长城", "南锣鼓巷", "牛街","白洋淀","草堂"],
    ["故宫", "长城"],placeholder="请选择")

st.write("我曾经跨过的山和大海:", options)\

st.code('''
# 演示案例④st.multiselect 源码
import streamlit as st
        
options = st.multiselect(
    "你曾经去过哪些地方？",
    ["故宫", "长城", "南锣鼓巷", "牛街","白洋淀","草堂"],
    ["故宫", "长城"],placeholder="请选择")

st.write("我曾经跨过的山和大海:", options)
''')

st.divider()

st.header("st.radio 演示：单选控件")

your_option = st.radio(
    "你喜欢吃什么？",
    ["胡辣汤", "北京烤鸭", "钵钵鸡","没胃口，什么也不想吃"],captions=["麻辣可口", "满口留香", "成都特色"],index= None)

if your_option == "胡辣汤":
    st.write("你喜欢吃胡辣汤")
elif your_option == "北京烤鸭":
    st.write("你喜欢吃北京烤鸭")
elif your_option == "钵钵鸡":
    st.write("你喜欢吃钵钵鸡")
elif your_option == "没胃口，什么也不想吃":
    st.write("那就是还不饿呗！")
else:
    st.caption("你究竟喜欢吃什么？")

st.code('''
# 演示案例⑤ st.radio 源码
import streamlit as st
        
your_option = st.radio(
    "你喜欢吃什么？",
    ["胡辣汤", "北京烤鸭", "钵钵鸡","没胃口，什么也不想吃"],captions=["麻辣可口", "满口留香", "成都特色"],index= None)

if your_option == "胡辣汤":
    st.write("你喜欢吃胡辣汤")
elif your_option == "北京烤鸭":
    st.write("你喜欢吃北京烤鸭")
elif your_option == "钵钵鸡":
    st.write("你喜欢吃钵钵鸡")
elif your_option == "没胃口，什么也不想吃":
    st.write("那就是还不饿呗！")
else:
    st.caption("你究竟喜欢吃什么？")
        
    ''')

st.divider()

st.header("st.selectbox 演示：下拉选择框")

your_option = st.selectbox(
    "你喜欢吃什么？",
    ["胡辣汤", "北京烤鸭", "钵钵鸡","没胃口，什么也不想吃"], index= None,placeholder="请根据个人口味选择")

if your_option == "胡辣汤":
    st.write("你喜欢吃胡辣汤")
elif your_option == "北京烤鸭":
    st.write("你喜欢吃北京烤鸭")
elif your_option == "钵钵鸡":
    st.write("你喜欢吃钵钵鸡")
elif your_option == "没胃口，什么也不想吃":
    st.write("那就是还不饿呗！")
else:
    st.caption("你究竟喜欢吃什么？")

st.code('''
# 演示案例⑥ st.selectbox 源码        

import streamlit as st

your_option = st.selectbox(
    "你喜欢吃什么？",
    ["胡辣汤", "北京烤鸭", "钵钵鸡","没胃口，什么也不想吃"], index= None,placeholder="请根据个人口味选择")

if your_option == "胡辣汤":
    st.write("你喜欢吃胡辣汤")
elif your_option == "北京烤鸭":
    st.write("你喜欢吃北京烤鸭")
elif your_option == "钵钵鸡":
    st.write("你喜欢吃钵钵鸡")
elif your_option == "没胃口，什么也不想吃":
    st.write("那就是还不饿呗！")
else:
    st.caption("你究竟喜欢吃什么？")

''')

st.divider()

st.header("st.select_slider 演示：滑动选择器")

options = range(1,11)

my_option = st.select_slider(
    "请选择一个数字",
    options,
    value=5)

st.write("你选择的数字是：", my_option)

st.code('''
# 演示案例⑦ st.select_slider 源码
import streamlit as st

options = range(1,11)

my_option = st.select_slider(
    "请选择一个数字",
    options,
    value=5)

st.write("你选择的数字是：", my_option)
''')

st.divider()

st.header("st.toggle演示：开关")

wheather = st.toggle ("天晴开关")

if wheather:
    st.write("晴天 :sun_with_face:")
else:
    st.write("雨天 :rain_cloud:")

st.code('''
# 演示案例⑧ st.toggle 源码
import streamlit as st

wheather = st.toggle ("天晴开关")

if wheather:
    st.write("晴天 :sun_with_face:")
else:
    st.write("雨天 :rain_cloud:")
''')