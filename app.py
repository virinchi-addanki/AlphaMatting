import streamlit as st
from PIL import Image 
from rembg import remove

def main():
    st.title("Alpha Matting")
    hide_footer()
    uploaded_files = st.file_uploader("Upload an Image",type=['jpg','png','jpeg'],accept_multiple_files=False)
    if st.button("Execute"):
        if uploaded_files:
            img = Image.open(uploaded_files)
            res = bg_remove(img)
            col1,col2 = st.columns(2,gap='large')
            with col1:
                st.write("## Original Image")
                st.image(img)
            with col2:
                st.write("## Result Image")
                st.image(res)
        else:
            st.error("Please upload an image")

def bg_remove(image):
    return remove(image)

def hide_footer():
    hide_st_style = """
            <style>
            footer {visibility: hidden;}
            </style>
            """
    st.markdown(hide_st_style, unsafe_allow_html=True)

if __name__ == "__main__":
    main()