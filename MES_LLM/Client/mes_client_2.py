import streamlit as st
from dotenv import load_dotenv
import os
import requests



def main():

    st.set_page_config(layout = 'wide', page_title = 'MES Chatbot')

    if "questions" not in st.session_state:
        st.session_state['questions']= []
    
    if "answers" not in st.session_state:
        st.session_state['answers']= []
   
    # Load environment variables
    Cred_path = os.getcwd() + "/Config.env"
    load_dotenv(Cred_path)
    
    style_image1 = """
    width: auto;
    height: auto;
    """
    img_path = os.getenv("IMG_PATH")
    api_path = os.getenv("FLASK_API")

    st.markdown(
        
        f'<img src="{img_path}" style="{style_image1}">',
        unsafe_allow_html=True,
    )

    st.title('MES Chatbot')

    with st.form(key='my_form'):
        text_input = st.text_input(label='Ask a Question:')
        submit_button = st.form_submit_button(label='Submit')

    st.markdown("""<hr style="height:10px;border:none;color:#333;background-color:#333;" /> """, unsafe_allow_html=True)

    response1 = requests.post(api_path, json={
        'input': text_input,
        })
    if submit_button:
        user_input = text_input.strip()
        if user_input:
            
            st.session_state['questions'].append(user_input)
            st.session_state['answers'].append(response1.text)
        
            ###FOR ANSWER AT THE BOTTOM###
            # for x, y in zip(st.session_state['questions'],st.session_state['answers']):
            #     st.write("Question:")
            #     st.write(x)
            #     st.write("Answer:")
            #     st.write(y)
            #     st.markdown("""<hr style="height:10px;border:none;color:#333;background-color:#333;" /> """, unsafe_allow_html=True)


            ###FOR ANSWER ON TOP###
            for i in range(len(st.session_state["questions"]) - 1, -1, -1):
                st.write("Question:")
                st.write(st.session_state["questions"][i])
                st.write("Answer:")
                st.write(st.session_state["answers"][i])
                st.markdown("""<hr style="height:10px;border:none;color:#333;background-color:#333;" /> """, unsafe_allow_html=True)

if __name__ == "__main__":
    main()
