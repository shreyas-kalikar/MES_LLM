from langchain.agents import create_sql_agent
from langchain.agents.agent_types import AgentType
from langchain.sql_database import SQLDatabase
from langchain_community.agent_toolkits import SQLDatabaseToolkit
from langchain_openai import AzureChatOpenAI
from langchain.prompts.chat import ChatPromptTemplate
from dotenv import load_dotenv
import os
import json
import sqlite3
from datetime import datetime

def get_mes_schema(db_path):
    Flag = True
    #Finding schema and saving
    db = SQLDatabase.from_uri(db_path, sample_rows_in_table_info=8)
    tables = db.get_usable_table_names()
    schema = db.get_table_info_no_throw(tables)
    return schema
def setup(user_input,Flag):

    with open('prompt.json', 'r') as file:
        credentials = json.load(file)
    prompt1 = credentials['p1']
    prompt2 = credentials['p2']
    prompt3 = credentials['p3']
    

    # Load environment variables
    Cred_path = os.getcwd() + "/Config.env"
    load_dotenv(Cred_path)
    db_path = os.getenv("DB_PATH")

    if Flag :
        schema = get_mes_schema(db_path)
        print("schema is generates")
        Flag=False
    else:
        print("schema is reused")
        print(schema)

    # Retrieve environment variables
    
    deployment_name = os.getenv("AZURE_DEPLOYMENT_NAME")
    model_name = os.getenv("AZURE_MODEL_NAME")
    temperature = float(os.getenv("AZURE_TEMPERATURE"))  # Assuming temperature needs to be a float
    api_key = os.getenv("AZURE_API_KEY")
    api_version = os.getenv("AZURE_API_VERSION")
    azure_endpoint = os.getenv("AZURE_ENDPOINT")
    db = SQLDatabase.from_uri(db_path, sample_rows_in_table_info=8)
    llm = AzureChatOpenAI(
    deployment_name=deployment_name,
    model_name=model_name,
    temperature=temperature,
    api_key=api_key,
    api_version=api_version,
    azure_endpoint=azure_endpoint
    )

    toolkit = SQLDatabaseToolkit(db=db, llm=llm)

    db_agent = create_sql_agent(
        llm=llm,
        toolkit=toolkit,
        verbose=False,
        agent_type=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
        handle_parsing_errors=True
    )

    
    final_prompt = prompt1 + schema + prompt2 + prompt3

    prompt_template = ChatPromptTemplate.from_messages(
        [
            ("system", final_prompt),

            ("user", "{query}\n Question: "),

        ]
    )
    try:
        result = db_agent.invoke(prompt_template.format(query=user_input))
        return result['output']
                
    except ValueError as e:
        response = str(e)
        response = response.removeprefix("An output parsing error occurred.")

        return response
    # result = db_agent.invoke(prompt_template.format(query=user_input))
    # print("**************************")
    # print("now in setup section with an output generated")
    # print("**************************")
    # result = result['output']
    # # conn = sqlite3.connect('prompt.db')
    # # cursor = conn.cursor()
    # # current_date = datetime.now().strftime("%Y-%m-%d")
    # # cursor.execute("INSERT INTO UserPrompt (Date, UserInput) VALUES (?, ?)", (current_date, user_input))
    # # conn.commit() 
    # # conn.close() 
    # return result
    
# def main():
#         prompt ="Name all the products that have quantity less than 50"
#         print("**************************")
#         print("now in main section going to setup")
#         print("**************************")
#         print(setup(prompt,True))
# if __name__ == "__main__":
#     main()

    

    
