import streamlit as st
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
import pandas as pd
import pickle
penguin_df=pd.read_csv('penguins-chinese.csv',encoding='gbk')
penguin_df.dropna(inplace=True)
output = penguin_df['企鹅的种类']
features = penguin_df[['企鹅栖息的岛屿', '喙的长度', '喙的深度', '翅膀的长度', '身体质量', '性别']]
features = pd.get_dummies(features)
output_codes, output_uniques = pd.factorize(output)
x_train, x_test, y_train, y_test = train_test_split(features, output_codes, train_size=0.8)
# 构建一个随机森林分类器
rfc = RandomForestClassifier()
rfc.fit(x_train, y_train)
y_pred = rfc.predict(x_test)
score = accuracy_score (y_test, y_pred)
with open ('rfc_model.pkl', 'wb') as f:
    pickle.dump (rfc, f)
with open ('output_uniques.pkl', 'wb') as f:
    pickle.dump (output_uniques, f)
print (' 保存成功，已生成相关文件。')


st.set_page_config(page_title="企鹅分类器", #页面标题
page_icon=":penguin:", #页面图标
layout='wide')
with st.sidebar:
    st.image ('rigth_logo.png', width=100)
    st.title (' 请选择页面 ')
    page = st.selectbox ("请选择页面", ["简介页面", "预测分类页面"], label_visibility='collapsed')
if page == "简介页面":
    st.title ("企鹅分类器:penguin:")
    st.header (' 数据集介绍 ')
    st.markdown (""" 帕尔默群岛企鹅数据集是用于数据探索和数据可视化的一个出色的也可以作为机器学习入门练习。
该数据集是由 Gorman 等收集，并发布在一个名为 palmerpenguins 的 R 语以对南极企鹅种类进行分类和研究。
该数据集记录了 344 行观测数据，包含 3 个不同物种的企鹅：阿德利企鹅、巴鹅和帽带企鹅的各种信息。""")
    st.header (' 三种企鹅的卡通图像 ')
    st.image ('penguins.png')
elif page == "预测分类页面":
    st.header ("预测企鹅分类")
    st.markdown ("这个 Web 应用是基于帕尔默群岛企鹅数据集构建的模型。只需输入 6 就可以预测企鹅的物种，使用下面的表单开始预测吧！")
col_form,col, col_logo = st.columns ([3, 1, 2])
with col_form:
    with st.form ('user_inputs'):
        island = st.selectbox (' 企鹅栖息的岛屿 ', options=[' 托尔森岛 ', ' 比斯科 岛 ', ' 德里姆岛 '])
        sex = st.selectbox (' 性别 ', options=[' 雄性 ', ' 雌性 '])
        bill_length = st.number_input (' 喙的长度（毫米）', min_value=0.0)
        bill_depth = st.number_input (' 喙的深度（毫米）', min_value=0.0)
        flipper_length = st.number_input (' 翅膀的长度（毫米）', min_value=0.0)
        body_mass = st.number_input (' 身体质量（克）', min_value=0.0)
        submitted = st.form_submit_button (' 预测分类 ')
island_biscoe, island_dream, island_torgerson = 0, 0, 0

if island == ' 比斯科群岛 ':
    island_biscoe = 1
elif island == ' 德里姆岛 ':
    island_dream = 1
elif island == ' 托尔森岛 ':
    island_torgerson = 1
sex_female, sex_male = 0, 0
if sex == ' 雌性 ':
    sex_female = 1
elif sex == ' 雄性 ':
    sex_male = 1

format_data = [bill_length, bill_depth, flipper_length, body_mass,island_dream, island_torgerson, island_biscoe, sex_male,sex_female]
if ((bill_length < 32.1 or bill_length > 60) or(bill_depth < 13.1 or bill_depth > 21.5) or(flipper_length < 172 or flipper_length > 231) or(body_mass < 2700 or body_mass > 6300)):
    st.error("输入的特征值超出正常企鹅特征范围，请重新输入！")
with open('rfc_model.pkl', 'rb') as f:
    rfc_model = pickle.load(f)
with open('output_uniques.pkl', 'rb') as f:
    output_uniques_map = pickle.load(f)
if submitted:
    format_data_df = pd.DataFrame (data=[format_data], columns=rfc_model.feature_names_in_)
# 使用模型对格式化后的数据 format_data 进行预测，返回预测的类别代码
    predict_result_code = rfc_model.predict (format_data_df)
# 将类别代码映射到具体的类别名称
    predict_result_species = output_uniques_map [predict_result_code][0]
    st.write (f' 根据您输入的数据，预测该企鹅的物种名称是：{predict_result_species}')
with col_logo:
    if not submitted:
        st.image('rigth_logo.png', width=300)
    else:
        st.image(f'{predict_result_species}.png', width=300)
    
