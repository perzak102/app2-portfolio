import streamlit as st
import pandas

st.set_page_config(layout="wide")
col1, col2 = st.columns(2)
with col1:
    st.image("images/1-perz.JPG")

with col2:
    st.title("Piotr Perz")
    content = """
    As a dedicated Python developer, I specialize in writing clean, efficient, and maintainable code that drives innovative software solutions. 
    My expertise in Python is complemented by a strong foundation in data structures, algorithms, and object-oriented programming, enabling me to tackle complex problems with confidence. 
    I am passionate about leveraging Python's powerful libraries and frameworks, such as Django and Flask, to create scalable web applications and services. 
    With a keen eye for detail, I consistently deliver high-quality code and am committed to continuous learning and staying abreast of the latest industry trends and best practices. 
    My collaborative approach to software development, along with my problem-solving skills, makes me a valuable asset to any team seeking to build impactful Python-based projects.
    """
    st.info(content)

content2= """
Below you can find some of the apps I have built in Python. Feel free to contact me!
"""
st.write(content2)

col3, empty_col, col4 = st.columns([3, 1, 3])

df = pandas.read_csv("data.csv", sep=";")
with col3:
    for index, row in df[:10].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("images/" + row["image"])
        st.write(f"[{row['title']}]({row['url']})")

with col4:
    for index, row in df[10:].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("images/" + row["image"])
        st.write(f"[{row['title']}]({row['url']})")