import streamlit as st
# 页面配置（可选，美化标题/图标）
st.set_page_config(page_title='个人简历生成器',page_icon='👧',layout='wide')
st.title('🙆‍♀️个人简历生成器')
st.text('使用Steamlit创建你的个性化简历')
col_left, col_right = st.columns(2)
with col_left:
# 左侧表单：用 st.text_input/st.selectbox 等组件  
    st.header('个人信息表单')
    st.write('***')
    xm=st.text_input('姓名')
    job=st.text_input('职业')
    phone=st.text_input('电话号码')
    email=st.text_input('邮箱')
    birthday=st.text_input('出生日期')
    xb=st.radio(
        '性别',
        ['男','女','其他'],
        horizontal=True
        )
    education = st.selectbox("学历",['小学', '初中', '高中','大专','本科','研究生'])

    def my_format_func(option):
        return f'{option}'
    st.multiselect(
        '语言能力(可多选)',
        ['Chinese', 'English', 'Japnese','French','Spanish','Arbic'],
        format_func=my_format_func,)
    
    jn=st.multiselect(
        '技能(可多选)',
        ['SQL', 'python', 'C语言','Java','数据库'],
        
        format_func=my_format_func,)
    time = st.selectbox(
        "每日最佳联系时间段",
        ['9:30-11:00', '14:30-17:30', '19:00-20:00','21:00-22:00'],
        )
    
    my_range = range(0, 21)
    jy = st.select_slider('工作经验（年）', options=my_range)
    st.write(jy)
    xz= st.select_slider(
    '期望薪资范围（元）',
    options=range(5000,50001),
    value=(10000, 20000))
    jl=st.text_area(label='个人简介：', placeholder='请简要介绍您的专业背景、职业目标和个人特点...')
    uploaded_photo = st.file_uploader("上传个人照片", type=["jpg", "jpeg", "png", "gif"])
    if uploaded_photo is not None:
        # 显示上传的照片
            st.session_state['photo'] = uploaded_photo
            st.image(uploaded_photo, caption="您上传的照片")
    else:
            st.session_state['photo'] = None
    

with col_right:
# 右侧实时预览：用 st.write/st.header 渲染内容
    st.header("简历实时预览")
    st.write('***')
    info_col1,info_col2=st.columns(2)
    with info_col1:
        st.write(f"职位：{job}")
        st.write(f"电话：{phone}")
        st.write(f"邮箱：{email}")
        st.write(f"出生日期：{birthday.strftime('%Y/%m/%d') if birthday else ''}")
    
    with info_col2:
   
# 基础信息
        st.write(f"性别：{xb}")
        st.write(f"学历：{education}")
        st.write(f"工作经验：{jy}")
        st.write(f"期望薪资：{xz}")
        st.write(f"最佳联系时间：{time}")
     
    st.write('***')
# 个人简介
    st.header("个人简介")
    st.write(jl)
    st.write('***')
    st.header("专业技能")
    st.write(jn)
