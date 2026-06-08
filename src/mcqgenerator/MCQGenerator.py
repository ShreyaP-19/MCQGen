import os
import json
import pandas as pd
import traceback
from dotenv import load_dotenv
from src.mcqgenerator.logger import logging
from src.mcqgenerator.utils import read_file, get_table_data

from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableParallel


#load environment variables from .env file
load_dotenv()

#access the environment variable
KEY=os.getenv("OPENAI_API_KEY")

llm=ChatOpenAI(openai_api_key=KEY,model_name="gpt-3.5-turbo",temperature=0.7)

TEMPLATE="""
Text:{text}
You are an expert MCQ maker. Given the above text, it is your job to create a quiz of {number} multiple choice questions for the subject of {subject} in {tone} tone. Make sure the questions are not repeated and check all the questions to be conforming the text as well. Make sure to format your response like RESPONSE_JSON below and use it as a guide.\
Ensure to make {number} MCQs
###RESPONSE_JSON
{response_json}
"""

quiz_generation_prompt=PromptTemplate(
    input_variables=["text","number","subject","tone","response_json"],
    template=TEMPLATE
)

modern_chain = prompt=quiz_generation_prompt | llm | RunnableParallel(quiz=StrOutputParser())

TEMPLATE2="""
You are an expert english grammarian and writer.given a mcq for {subject} subject\
You need to evaluate the complexity of the question and give a complete analysis of the quiz. Only use at max 50 words for complexity.If the quiz is not at per with the cognitive and analytical abilities of the students,\
update the quiz questions which need to be changed and change the tone such that it perfectly fits the student abilities.
Quiz_MCQs:
{quiz}
Check from an expert English writer of the above quiz:
"""

quiz_evaluation_prompt=PromptTemplate(
    input_variables=["subject","quiz"],
    template=TEMPLATE2
)

quiz_evaluation_chain=prompt=quiz_evaluation_prompt|llm|RunnableParallel(review=StrOutputParser())

#run both chains in sequence
sequential_chain=modern_chain|quiz_evaluation_chain

