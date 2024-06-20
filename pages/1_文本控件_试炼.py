import streamlit as st

st.title("""
Streamlit的文本类控件演示&源码
作者：沐逸@产品江湖
2024.06
""")
st.divider()

st.caption("这是页面标题控件：")
st.title('这是页面标题')
st.title('_Streamlit_ is :blue[简单&易上手] :sunglasses:')

st.code("""
#实例①代码
import streamlit as st
st.title('这是页面标题')
st.title('_Streamlit_ is :blue[简单&易上手] :sunglasses:')
""")

st.divider()
st.caption("这是段落主标题控件：")
st.header('这是段落主标题', divider='rainbow')
st.header('_Streamlit_ is :blue[简单&易上手] :sunglasses:')

st.code('''
#实例②代码
import streamlit as st
st.header('这是段落主标题', divider='rainbow')
st.header('_Streamlit_ is :blue[简单&易上手] :sunglasses:')
''')

st.divider()
st.caption("这是段落副标题控件：")
st.subheader('这是段落副标题', divider='rainbow')
st.subheader('_Streamlit_ is :blue[简单&易上手] :sunglasses:')
st.code('''
        
#实例③代码
import streamlit as st

st.subheader('这是段落副标题', divider='rainbow')
st.subheader('_Streamlit_ is :blue[简单&易上手] :sunglasses:')
'''
)

st.divider()

st.caption("*这是一段Markdown*:")
st.markdown("*Streamlit* 是 **非常非常** ***cool的！***:tulip::cherry_blossom::rose::hibiscus::sunflower::blossom:")
st.code(
    '''
    #实例④代码
    import streamlit as st
    st.markdown("*这是一段Markdown*")
    st.markdown("*Streamlit* 是 **非常非常** ***cool的！***:tulip::cherry_blossom::rose::hibiscus::sunflower::blossom:")
'''
)

st.divider()

st.caption("这是段落注解：")
st.caption('一段注解： _italics_ :blue[colors] and emojis :sunglasses:')
st.code('''
#实例⑤代码
import streamlit as st
st.caption("这是段落注解")
st.caption('一段注解： _italics_ :blue[colors] and emojis :sunglasses:')
'''
)

st.divider()

st.caption("这是一个代码展示控件，并且支持一键复制：")


st.code('''
#实例⑥的代码
import  streamlit as st
st.code(
    st.markdown("""
    # 这是一个标题
    ## 这是一个副标题
    ### 这是一个三级标题
    #### 这是一个四级标题
    ##### 这是一个五级标题
    ###### 这是一个六级标题
    """)
)

,language='python') ''')

st.divider()

st.caption("这是一条分割线：")

st.divider()

st.code(
    # 实例⑦的代码
    '''st.divider()'''
)

st.divider()

st.caption("这是一个公式展示控件：")

st.latex(r'''
a + ar + a r^2 + a r^3 + \cdots + a r^{n-1} =
    \sum_{k=0}^{n-1} ar^k =
    a \left(\frac{1-r^{n}}{1-r}\right)
''')

st.code("""

#实例⑦的代码
import streamlit as st
        
st.latex(r'''
a + ar + a r^2 + a r^3 + \cdots + a r^{n-1} =
    \sum_{k=0}^{n-1} ar^k =
    a \left(\frac{1-r^{n}}{1-r}\right)
''')

"""
)

st.divider()

st.caption("这是一个text输出控件：")

import streamlit as st

st.text('这是一些纯文本.')

st.code('''
#实例⑧的代码
import streamlit as st
st.text('这是一些纯文本.')
''')