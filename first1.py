import streamlit as st

st.set_page_config(page_title='音乐播放器', page_icon='🐒')
st.title('🎵简易音乐播放器')
st.text('使用streamlit制作的简单音乐播放器，支持切歌和基本播放控制')

# 判断内存中（session_state中）有没有a
if 'a' not in st.session_state:
    st.session_state['a'] = 0

image_arr = [{
        '图片':'https://p1.music.126.net/lt4R_XbCZsT-yzRfWs9VfQ==/3434874331529456.jpg?',
        'title':'后来的我们',
        '歌手':'歌手：五月天',
        '时长':'时长：3;07',
        'audio_file':'https://music.163.com/#/song?id=422104138'
    },{
        '图片':'https://p1.music.126.net/PEGvmO3OqgGOkx4m9qxAJA==/109951163478499713.jpg?',
        'title': '于是',
        '歌手':'歌手：郑润泽',
        '时长':'时长：3:52',
        'audio_file':'https://music.163.com/#/song?id=1303464858'
    },{
        '图片':'https://p2.music.126.net/5zAv9nKlwj80OearK5Vrjw==/109951169686963932.jpg?',
        'title': '小孩',
        '歌手':'歌手：罗森涛',
        '时长':'时长：3:39',
        'audio_file':'https://music.163.com/#/song?id=2166584564'
    }]

st.image(image_arr[st.session_state['a']]['图片'], caption=image_arr[st.session_state['a']]['title'])
st.write((image_arr[st.session_state['a']]['歌手']))
st.write((image_arr[st.session_state['a']]['时长']))
st.audio(image_arr[st.session_state['a']]['audio_file'])

def next():
    # 声明a使用的是外面的全局变量a
    global a
    # 做什么事？？   = a + 1
    st.session_state['a'] = (st.session_state['a'] + 1) % len(image_arr)
def prv():
    st.session_state['a'] = (st.session_state['a'] -1) % len(image_arr)

c1, c2 = st.columns(2)
with c1:
    st.button('上一首', on_click=prv, use_container_width=True)

with c2:
    st.button('下一首', on_click=next, use_container_width=True)
with st.expander("使用说明", expanded=True):
    st.markdown("""
    #### 音乐播放器功能说明：
    1. 播放/暂停：点击中间的播放/暂停按钮控制音乐播放
    2. 切歌功能：使用左右箭头按钮切换上一首/下一首
    3. 歌曲列表：从列表中选择任意歌曲播放（示例暂未实现，可扩展）
    #### 课堂练习任务：
    1. 实现基本的播放控制功能（真实音频播放）
    2. 添加专辑封面显示（已演示，可优化样式）
    3. 实现切歌功能（上一首/下一首，需扩展歌曲列表）
    4. 显示歌曲基本信息（标题、歌手、时长，已演示）
    #### 扩展练习（可选）：
     - 添加随机播放功能
     - 实现音量控制
     - 添加播放进度显示（真实关联音频时长）
    """)
# ------ 底部标识（可选） ------
st.markdown("---")
st.markdown("Streamlit 音乐播放器 | 课堂练习示例 | 使用 Python+Streamlit 构建")
