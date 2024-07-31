import turtle
import streamlit as st
import pandas as pd
from PIL import Image
import arcade as aa
import _locale
import os
import sys

page = st.sidebar.radio('我的首页',['我的兴趣推荐','我的图片处理工具',
                                '我的智慧词典','我的快捷助手','我的留言区', '小游戏'])
def page_1():
    '我的兴趣推荐'
    st.write(":blue[我的世界]")
    st.text("玩家们可以在游戏中自由选择模式（生存、创造、冒险、旁观、极限），在各种模式中体验不一样的有")
    st.text("趣玩法,在生存模式中享受战斗、冒险等多种乐趣，在创造模式下享受当创世神的乐趣。玩家在游戏中")
    st.text("可以在单人或多人模式中通过摧毁或创造精妙绝伦的建筑物和艺术，或者收集物品探索地图以完成游")
    st.text("戏的主线。")
    st.image("图片1.jpg")
    st.link_button('视频欣赏', ' https://www.bilibili.com/video/BV11S4y127VC/?share_source=copy_web')
def page_2():
    '我的图片处理工具'
    st.write(':100:图片换色小程序:100:')
    uploaded_file = st.file_uploader("上传图片", type=['png','jpg','jpeg'])
    if uploaded_file:
        file_name = uploaded_file.name
        file_type = uploaded_file.type
        file_size = uploaded_file.size
        img = Image.open(uploaded_file)
        #st.image(img)
        #st.image(img_change(img, 0, 2, 1))
        tab1, tab2, tab3, tab4 = st.tabs(["原图", "改色1", "改色2", "改色3"])
        with tab1:
            st.image(img)
        with tab2:
            st.image(img_change(img, 0, 2, 1))
        with tab3:
            st.image(img_change(img, 1, 2, 0))
        with tab4:
            st.image(img_change(img, 1, 0, 2))
def page_3():
    '我的智慧词典'
    st.write('智慧词典')
    with open('words_space1.txt', 'r', encoding = 'utf-8')as f:
        words_list = f.read().split('\n')
    for i in range(len(words_list)):
        words_list[i] = words_list[i].split('#')
    words_dict = {}
    for i in words_list:
        words_dict[i[1]] = [int(i[0]), i[2]]
    # 创建输入框
    with open('check_out_times.txt', 'r', encoding = 'utf-8')as f:
        times_list = f.read().split('\n')
    for i in range(len(times_list)):
        times_list[i] = times_list[i].split('#')
    times_dict = {}
    for i in times_list:
        times_dict[int(i[0])] = int(i[1])
    word = st.text_input('请输入要查询的单词, 如：China')
    if word in words_dict:
        st.write(words_dict[word])
        n = words_dict[word][0]
        if n in times_dict:
            times_dict[n] += 1
        else:
            times_dict[n] = 1
        with open('check_out_times.txt', 'w', encoding='utf-8') as f:
            message = ''
            for k, v in times_dict.items():
                message += str(k) + '#' + str(v) + '\n'
            message = message[:-1]
            f.write(message)
        st.write('查询次数：', times_dict[n])
        if word == 'China':
            st.balloons()
        if word == 'fcs':
            st.snow()
            st.balloons()



def page_4():
    '快捷助手'
    st.write('我的快捷助手')
    st.image("烦村.png")
    st.link_button('烦人的村民点击即看', 'https://www.bilibili.com/video/BV1Zt411X7jt/?p=14&share_source=copy_web')
    st.image("百度.jpg")
    st.link_button('百度首页', 'https://www.baidu.com/')
    st.image("抖音.png")
    st.link_button('点击即看', 'https://www.douyin.com/')
    st.image("爱奇艺.png")
    st.link_button('点击即看', 'https://www.iqiyi.com/')
    st.image("blibli.png")
    st.link_button('点击即看', 'https://www.bilibili.com/')
    st.image("腾讯.png")
    st.link_button('点击即看', 'https://v.qq.com/')
    st.image("造梦.png")
    st.link_button('点击即玩（作者喜欢）', 'http://www.4399.com/flash/210650.htm')
    st.image("ttt.png")
    st.link_button('智能助手，点击即用', 'https://kimi.moonshot.cn/kimiplus/conpga8t7lagcavlq31g?data_source=tracer&data_industry=ocpc_ps_convert&utm_campaign=TR_3xxoYJJo&utm_content=&utm_medium=360&utm_source=360_pc_search&utm_term=&qhclickid=fbe52f6580ac621e')
    st.image("4399.png")
    st.link_button('点击即玩', 'https://www.4399.com/')

def page_5():
    '我的留言区'
    st.write('我的留言区')
    with open('leave_messages.txt', 'r', encoding = 'utf-8')as f:
        messages_list = f.read().split('\n')
    for i in range(len(messages_list)):
        messages_list[i] = messages_list[i].split('#')
    
    for i in messages_list:
        if i[1] == '阿短':
            with st.chat_message('☕'):
                st.write(i[1],':',i[2])
        elif i[1] == '小迪':
            with st.chat_message('💯'):
                st.write(i[1],':',i[2])
        elif i[1] == i[1]:
            with st.chat_message('🌎'):
                st.write(i[1],':',i[2])
    
    name = st.text_input('我的大名是......')
    new_message = st.text_input('想要说的话......')
    
    if st.button('留言'):
        messages_list.append([str(int(messages_list[-1][0])+1), name, new_message])
        with open('leave_messages.txt', 'w', encoding='utf-8') as f:
            message =  ''
            for i in messages_list:
                message += i[0] + '#' + i[1] + '#' + i[2] + '\n'
            message = message[:-1]
            f.write(message)

def page_6():
    '小游戏'
    st.write('小游戏')
    st.text('网页版不支持可能某些功能')
    
    st.link_button('点击即玩', 'https://turtle.codemao.cn/player/h5/216130134')



            
def img_change(img, rc, gc, bc):
    width, height = img.size
    img_array = img.load()
    for x in range(width):
        for y in range(height):
            r = img_array[x, y][rc]
            g = img_array[x, y][gc]
            b = img_array[x, y][bc]
            img_array[x, y] = (r ,g ,b )
    return img


if (page == '我的兴趣推荐'):
    page_1()
elif (page == '我的图片处理工具') :
    page_2()
elif (page == '我的智慧词典') :
    page_3()
elif (page == '我的快捷助手') :
    page_4()
elif (page == '我的留言区') :
    page_5()
elif (page == '小游戏') :
    page_6()
