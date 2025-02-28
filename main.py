import streamlit as st
import numpy as np
import pandas as pd

# Title
st.title('Welcome to my first streamlit app')

# Text
st.text('This is a simple streamlit app')

# Input Slider
number = st.slider('Pick a number: 0 TO 100')

# Print the selected number
st.write(f'You selected: {number}')

# Button
if st.button('Greeting'):
    st.write('Hello')
    st.balloons()  # Show balloons when button is clicked
else:
    st.write('Goodbye')

# ADD RADIO BUTTON
genre = st.radio(
    "What's your favorite movie genre?",
    ('Comedy', 'Drama', 'Documentary')
)

# Print the selected genre
st.write(f'You selected: {genre}')

# Add a dropdown list in the sidebar
option = st.sidebar.selectbox(
    'How would you like to be contacted?',
    ('Email', 'Home phone', 'Mobile phone')
)

# Add your WhatsApp number input
st.sidebar.text('Your WhatsApp number')
st.sidebar.text_input('Enter your number here')

# Add a file uploader
uploaded_file = st.sidebar.file_uploader("Choose a CSV file", type="csv")

# Create a line plot
data = pd.DataFrame({
    "first column": list(range(1, 11)),
    "second column": np.arange(number, number + 10)  # Corrected this line
})
st.line_chart(data)






