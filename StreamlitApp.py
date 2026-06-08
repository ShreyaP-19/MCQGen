import os
import json
import pandas as pd
import traceback
from dotenv import load_dotenv
from src.mcqgenerator.logger import logging
from src.mcqgenerator.utils import read_file, get_table_data

from langchain_community.callbacks import get_openai_callback

from src.mcqgenerator.MCQGenerator import sequential_chain

import streamlit as st 

with open(r'C:\Users\shrey\OneDrive\Desktop\mcqgen\Response.json', 'r') as file:
    RESPONSE_JSON = json.load(file)

st.title("MCQs Creator Application with Langchain")

with st.form("user_inputs"):
    #file upload
    uploaded_file=st.file_uploader("Upload a PDF or txt file")

    #input fields
    mcq_count=st.number_input("No. of MCQs", min_value=3, max_value=50)

    subject=st.text_input("Insert Subject",max_chars=20)

    tone=st.text_input("Complexity Level of Questions",max_chars=20, placeholder="Simple")

    button=st.form_submit_button("Generate MCQs")

    if button and uploaded_file is not None and mcq_count and subject and tone:
        with st.spinner("Generating MCQs..."):
            try:
                text=read_file(uploaded_file)
                with get_openai_callback() as cb:
                    response = sequential_chain.invoke(
                    {
                        "text": text,
                        "number": mcq_count,
                        "subject": subject,
                        "tone": tone,
                        "response_json": json.dumps(RESPONSE_JSON)
                    }
                )

            except Exception as e:
                traceback.print_exception(type(e), e, e.__traceback__)
                st.error(f"An error occurred: {str(e)}")
            else:
                print(f"Total Tokens: {cb.total_tokens}")
                print(f"Prompt Tokens: {cb.prompt_tokens}")
                print(f"Completion Tokens: {cb.completion_tokens}")
                print(f"Total Cost (USD): ${cb.total_cost}")
                if isinstance(response,dict):
                    #extract the quiz data from response
                    quiz=response.get("quiz",None)
                    if quiz is not None:
                        table_data=get_table_data(quiz)
                        if table_data is not None:
                            df=pd.DataFrame(table_data)
                            df.index=df.index+1
                            st.table(df)
                            #display the review in the text box as well
                            st.text_area(label="Review",value=response["review"])
                        else:
                            st.error("Error in table data.")
                else:
                    st.write(response)

