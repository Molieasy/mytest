import streamlit as st
import pandas as pd

st.title('学生 小陆-数字档案:sunglasses: :anchor: sixth')
st.header('基础信息:key:')
st.markdown('学生ID: NEO-2023-001')
st.markdown('注册时间: :green[2023-10-01]|精神状态: 正常')
st.markdown('当前教室: :green[实训楼301]|安全等级: :green[绝密]')
st.subheader('技能矩阵:star: :anchor: 技能矩阵')
c1, c2, c3 = st.columns(3)
c1.metric(label="c语言", value="95%", delta="2%")
c2.metric(label="python", value="87%", delta="-1%")
c3.metric(label="java", value="68%", delta="-10%", delta_color="off")

st.write("### Streamlit课程进度")
st.write("*Streamlit课程进度*")
st.progress(25)#Assuming 25% progress
st.markdown('***')

data = {
    '日期':['2023-10-01', '2023-10-05', '2023-10-12'],
    '任务':['学生数字档案', '课程管理系统', '数据图表展示'],
    '状态':['✅ 完成', '⚙️ 进行中', '✖️ 未完成'],
    '难度':['★★☆☆☆', '★☆☆☆☆', '★★★☆☆']
}

index = pd.Series([0,1,2])
df = pd.DataFrame(data, index=index)
st.header('任务日志:mag:')
st.table(df)

st.subheader('最终代码成果:lock:')
python_code = """
def matrix_branch():
    while True:
        if detect_vulnerability():
            exploit()
            return "ACCESS GRANTED"
        else:
            stealth_evade()
...
"""
st.code(python_code, language=None)
st.write("__________")
st.write(">>>SYSTEM MESSAGE:下个任务目标已解锁...")
st.write(">>>TARGET:课程管理系统")
st.write(">>>COUNTDOWN:2025-06-04 16:55:07")
st.write("系统状态:在线 连接状态:已加密")
