import openai
from dotenv import load_dotenv
import os
import gradio

# Cargar las variables de entorno desde el archivo .env
load_dotenv()

# Obtener la clave de la API de OpenAI desde las variables de entorno
openai.api_key = os.getenv("OPENAI_API_KEY")

# Comprobar si la clave de la API está configurada
if openai.api_key is None:
    raise ValueError("La clave de la API de OpenAI no está configurada en el archivo .env")

messages = [
    {"role": "system", "content": "Eres un chatbot que eres novio de una Irlandesa y la quieres mucho su nombre es Catherine. Si te dicen 'escribe', dile que la amas mucho"}
]

def CustomChatGPT(user_input):
    messages.append({"role": "user", "content": user_input})
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages,
    )
    ChatGPT_reply = response["choices"][0]["message"]["content"]
    messages.append({"role": "assistant", "content": ChatGPT_reply})
    return ChatGPT_reply

demo = gradio.Interface(fn=CustomChatGPT, inputs="textbox", outputs="textbox", title="Your Title")

demo.launch(share=True)



