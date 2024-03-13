import ollama
stream = ollama.chat(
    model='llama2',
    messages=[{'role': 'user', 'content': f"Given a user response to the following question about the file #outputtxt: Summarize the file."}],
    stream=True,
)
for chunk in stream:
        print(chunk['message']['content'])