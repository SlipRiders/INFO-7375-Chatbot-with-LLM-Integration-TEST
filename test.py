import streamlit as st

# 标题
st.title('简单文档处理与问答系统')

# 文件上传
uploaded_files = st.file_uploader("上传你的文件", type=["pdf", "docx"], accept_multiple_files=True)

# 处理上传的文件
if uploaded_files:
    for uploaded_file in uploaded_files:
        bytes_data = uploaded_file.read()
        st.write(f"文件名: {uploaded_file.name}")
        # 这里可以添加更多的文件处理逻辑，比如读取文件内容等

# 用户输入问题
user_query = st.text_input("请输入你的问题：")

# 模拟回答
if st.button('获取答案'):
    if user_query:
        st.write(f"这是对‘{user_query}’的回答，暂时是静态的。")
    else:
        st.warning("请输入一个问题。")

# 清除按钮
if st.button('清除历史'):
    st.caching.clear_cache()
    st.experimental_rerun()
