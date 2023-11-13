import streamlit as st

# Add title in the tab page and main page while setting the layout page to be wide
st.set_page_config(page_title='Layouts', layout='wide') 
st.title("Streamlit Layout")

# Sidebar
sidebar = st.sidebar
sidebar.write('This is my sidebar')
sidebar.header('Header in Sidebar')

# Columns
# Display the images in the column format
cat_img = 'media/cat.jpg'
dog_img = 'media/dog.jpg'
owl_img = 'media/owl.jpg'
col1, col2, col3  = st.columns(3)
with col1:
  st.write('This is column 1')
  st.image(cat_img)
with col2:
  st.write('This is column 2')
  st.image(dog_img)
with col3:
  st.write('This is column 3')
  st.image(owl_img)

# The below codes are the same as the above
# col1.write('This is is column 1')
# col1.image(cat_img)
# col2.write('This is is column 2')
# col2.image(dog_img)
# col3.write('This is is column 3')
# col3.image(owl_img)

# Tabs
st.header('Display in Tabs')
tab1, tab2, tab3 = st.tabs(['Cat', 'Dog', 'Owl'])
with tab1: 
  st.write("You are in Cat Tab")
  st.image(cat_img)
with tab2: 
  st.write("You are in Dog Tab")
  st.image(dog_img)
with tab3: 
  st.write("You are in Owl Tab")
  st.image(owl_img)
