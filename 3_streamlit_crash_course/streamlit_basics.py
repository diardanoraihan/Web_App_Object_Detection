# Full documentation: streamlit.io
import streamlit as st
import pandas as pd


# Display text
st.write("Hello World")

# Display dataframe
df = pd.DataFrame(data={'name':['diar', 'dano'], 'email': ['aaa@gmail.com', 'bbb@gmail.com']})
st.write(df)

# Text Formatting
st.title("This is Title")
st.header("This is Header")
st.subheader("This is subheader")
st.caption('This is caption')
st.text("This is plain text")

# Markdown
# https://www.markdownguide.org/cheat-sheet/
st.markdown("""
# This is Title
## This is Header
### This is subheader - 1
#### This is subheader - 2

This is plain text


For *italic* use single asterisk


For **bold** use double asterisks             
            """)

# Status elements
# Success
st.success("This message displays text in green background")
# Warning
st.warning("This message displays text in yellow background")
# Error
st.error("This message displays text in red background")

# Display Image
img = 'media/cat.jpg'
st.image(image=img, caption='Cat', width=300)

video_file = open('media/star.mp4', mode='rb').read()
st.video(video_file)