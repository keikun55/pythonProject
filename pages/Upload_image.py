import streamlit as st
import os, glob
def main():
    st.title("Lego image")
    uploaded_image = st.file_uploader("assign file", type=["jpg", "jpeg", "png"])

    if uploaded_image:
        st.image(uploaded_image, caption="アップロードされた画像")
    description = st.text_input("descript about image")
    st.write(f"画像の説明: (image_description)")

    if st.button('保存'):
        save_image_and_description(uploaded_image,description)

def save_image_and_description(image, description):
        print('保存')

if __name__ == "__main__":
    main()