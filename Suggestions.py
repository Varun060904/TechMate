from langchain_community.document_loaders import WebBaseLoader
from langchain_community.document_loaders import TextLoader
from langchain_community.vectorstores import Chroma
from langchain_community import embeddings
from langchain_community.chat_models import ChatOllama
from langchain_core.runnables import RunnablePassthrough
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate

def process_prompt(query):
    model_local = ChatOllama(model="mistral")
    loader=TextLoader("output.txt")
    doc_splits = loader.load_and_split()
    vectorstore = Chroma.from_documents(
        documents=doc_splits,
        collection_name="rag-chroma",
        embedding=embeddings.ollama.OllamaEmbeddings(model='nomic-embed-text'),
    )
    retriever = vectorstore.as_retriever()
    rag_template = """Answer the question based only on the following context:
    {context}
    Question: {question}
    """
    rag_prompt = ChatPromptTemplate.from_template(rag_template)
    rag_chain = (
        {"context": retriever, "question": RunnablePassthrough()}
        | rag_prompt
        | model_local
        | StrOutputParser()
    )
    #print(rag_chain.invoke(f"{query}"))
    answer=rag_chain.invoke(f"{query}")
    print(answer)
    

ques1=input("what are you looking for? eg : Phone , Laptop : ")

ques2=input("What is your budget ? : ")

ques3=input("Do you have any preferences as a brand? : ")

ques4=input("What Features do expect from the device ? Write what you feel like : ")

ques5=input("Do u have any specifications? : ")

prompt=f"Act as an proffesional electronic gadget suggestor : from the given context only Search for Devices with users specific needs which are category of gadget (Phone , TV , Laptop):{ques1} phone which has mrp price around : {ques2} and users preferred brand is :{ques3} . Match the Standout features and Strengths of the product with users expectations only :{ques4} and finally the specifications expected by the user : {ques5}"

process_prompt(prompt)

further_ques=input("Do  you have any further questions ? if 'Yes' then type your query if otherwise type 'NO' : ")
if further_ques=="No":
    pass
else:
    process_prompt(further_ques)