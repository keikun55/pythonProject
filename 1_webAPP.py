import streamlit as st

agree = st.checkbox('I agree')

if agree == True :
     st.write('Great!')
options = st.multiselect(
    'What are your favorite colors',
    ['Green', 'Yellow', 'Red', 'Blue'],
    default=['Yellow', 'Red'] # デフォルトの設定
)
value = st.slider('Select a value', 0, 100, 50)

# テキスト入力ボックス
text_input = st.text_input('Input', 'Input some text here.')
# テキストエリア
text_area = st.text_area('Text Area', 'Input some text here.')