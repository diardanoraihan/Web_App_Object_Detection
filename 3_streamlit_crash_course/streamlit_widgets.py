import streamlit as st
import os

st.title('Input Widgets')

# Button
st.header('Button')
myButton = st.button('Button') # return true or false
st.write(myButton)
if myButton:
  st.write("You pressed on Button")

# Checkbox (Toggle Button)
st.header("Checkbox")
myCheckbox = st.checkbox("Do you want to agree?") # return true/false
if myCheckbox:
  st.write("You checked the box")
else:
  st.write("You unchecked")

# Radio Button
# From list of value, radio button gives user to select one value
st.header("Radio Button")
options = ["India", "USA", "UK", "Australia"]
myRadio = st.radio("What is your favourite country?",
                   options=options,
                   index=1) # set the default chosen value, None for not any chosen
st.write('You favourite country is ', myRadio)

# Select Box
# From list of value, select box gives user to select multiple values
st.header("Select Box")
options2 = ['Email', 'Phone', 'WhatsApp']
mySelect = st.selectbox("How would you like to contact?",
                        options=options2,
                        index=None)
st.write("Your prefered communication is ", mySelect)

# Slider
st.header("Slider")
slider_range = st.slider("How old are you?",
                         min_value=1,
                         max_value=100,
                         step=1,
                         value=20) # Default value
st.write("Your age is ", slider_range, ' years old')

# Text Inputs
st.header("Text Input")
name = st.text_input("Enter your name:")
st.write('Your name is ', name)

age = st.number_input("Enter your age:",
                      min_value=1,
                      max_value=100,
                      step=1,
                      value=25)
st.write('Your age is ', age, ' years old')

# Upload File
# You can upload anykind of file with different format
st.header("Upload File")
uploaded_file = st.file_uploader('Choose a File: ') # Upload a file 'media/mountains.webp'
if uploaded_file:
  st.success('File is uploaded successfully')
  details = {'filename': uploaded_file.name,
             'filetype': uploaded_file.type,
             'filesize (bytes)': uploaded_file.size}
  st.json(details)

  # save the file
  path = os.path.join('./upload', uploaded_file.name)
  with open(path, mode = 'wb') as f:
    f.write(uploaded_file.getbuffer()) # get all the file information in the bytes and save it in 'media/'
    st.success("File is saved successfully")