from euriai.langchain import create_chat_model

def get_chat_model(api_key: str):
    """
    Returns a chat model via EuriAI's LangChain wrapper.
    Adjust model/temperature as needed.
    """
    return create_chat_model(api_key=api_key, model="gpt-5-nano-2025-08-07", temperature=0.7)

def ask_chat_model(chat_model, prompt: str) -> str:
    """
    Sends a single-turn prompt to the model and returns string content.
    """
    resp = chat_model.invoke(prompt)
    # Some LangChain models return an object with .content
    return getattr(resp, "content", str(resp))
