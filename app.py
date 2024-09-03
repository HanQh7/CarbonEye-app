import streamlit as st

# Set the page configuration to wide mode
st.set_page_config(layout="wide")

# Define the HTML with inline styles for the background
background_html = f"""
<div style="
    background-image: url('mangrov.jpg');
    background-size: cover;
    background-position: center;
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    z-index: -1;
">
</div>
"""

# Render the HTML for the background
st.markdown(background_html, unsafe_allow_html=True)

# Include Font Awesome for icons
st.markdown(
    """
    <link href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0-beta3/css/all.min.css" rel="stylesheet">
    """,
    unsafe_allow_html=True
)

# HTML and CSS for transparent buttons at the top
st.markdown(
    """
 <div style="display: flex; justify-content: flex-start; margin-top: -10px; padding-left: 10px; gap: 50px;">
       <button style="background-color: rgba(255, 255, 255, 0.6); 
                   color: black; 
                   border: 0px solid white; 
                   padding: 10px 20px; 
                   font-size: 20px; 
                   cursor: pointer; 
                   width: 150px;  /* Set a fixed width */
                   height: 50px;">  <!-- Set a fixed height -->
        Home
    </button>
        <button style="background-color: rgba(255, 255, 255, 0.6); 
                   color: black; 
                   border: 0px solid white; 
                   padding: 10px 20px; 
                   font-size: 20px; 
                   cursor: pointer; 
                   width: 150px;  /* Set a fixed width */
                   height: 50px;">  <!-- Set a fixed height -->
        Services
    </button>
    <button style="background-color: rgba(255, 255, 255, 0.6); 
                   color: black; 
                   border: 0px solid white; 
                   padding: 10px 20px; 
                   font-size: 20px; 
                   cursor: pointer; 
                   width: 150px;  /* Set a fixed width */
                   height: 50px;">  <!-- Set a fixed height -->
        Contact Us
    </button>
</div>
    """,
    unsafe_allow_html=True
)

# Centered and larger title with a subtitle in a lighter semi-transparent box
st.markdown(
    """
    <div style="background-color: rgba(255, 255, 255, 0.2); 
                padding: 20px; 
                border-radius: 20px; 
                text-align: center; 
                width: 50%; 
                margin: auto; 
                margin-top: 120px;">
        <h1 style="font-size: 100px; color: white;">
            CarbonEye
        </h1>
        <h2 style="font-size: 30px; color: white;">
            Your Vision for a <i>Greener</i>
 Future!
        </h2>
           <button style="background-color: white;
            display: flex; justify-content: center; margin-top: 20px; 
                           color: black; 
                           border-radius: 5px; 
                           padding: 15px 20px; 
                           font-size: 20px; 
                           cursor: pointer;">
                Click Here
            </button>
    
    </div>
    """,
    unsafe_allow_html=True
)

# Add social media icons at the bottom right corner
st.markdown(
    """
    <div style="position: fixed; 
                bottom: 20px; 
                right: 20px; 
                display: flex; 
                gap: 20px;">
        <a href="https://twitter.com" target="_blank">
            <i class="fas fa-times" style="font-size: 30px; color: white;"></i>
        </a>
        <a href="https://www.linkedin.com" target="_blank">
            <i class="fab fa-linkedin" style="font-size: 30px; color: white;"></i>
        </a>
        <a href="https://www.facebook.com" target="_blank">
            <i class="fab fa-facebook" style="font-size: 30px; color: white;"></i>
        </a>
    </div>
    """,
    unsafe_allow_html=True
)

import base64

def get_base64_of_bin_file(bin_file):
    with open(bin_file, 'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()

def set_background(png_file):
    bin_str = get_base64_of_bin_file(png_file)
    page_bg_img = f'''
    <style>
    .stApp {{
        background-image: url("data:image/png;base64,{bin_str}");
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
        background-attachment: fixed;
    }}
    </style>
    '''
    st.markdown(page_bg_img, unsafe_allow_html=True)

set_background('mangrov.jpg')
