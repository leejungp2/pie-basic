import streamlit as st
from page import project1 as p1
from page import project2 as p2
from page import intro
from page import intro_development
from page import intro_diagram

st.title("Disney Data Visualization App 🎥")
#one_one_two = r'''$${\vdash}:.(\exists x,y).\alpha=\iota`x.\beta=\iota`y.\supset:\alpha\cup\beta\in2.\equiv.\alpha\cap\beta=\Lambda$$'''
#st.write(one_one_two)

item_list = ['item0','item3', 'item4', 'item1', 'item2']

item_labels = {'item0':'선택하세요', 'item3' : 'Development Environment', 'item4' : 'Architecture Diagram', 'item1':'Data Processing', 'item2':'Visualization'}

FIL = lambda x : item_labels[x]
item = st.sidebar.selectbox('Menu',  item_list, format_func = FIL )


if item == 'item1':
	p1.app()
elif item == 'item2':
	p2.app()
elif item == 'item0':
	intro.app()
elif item == 'item3':
	intro_development.app()
elif item == 'item4':
	intro_diagram.app()