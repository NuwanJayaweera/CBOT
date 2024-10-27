# chatbot.py

import openai
import gradio as gr

# Set up your OpenAI API key here
openai.api_key = "Your OpenAI API'


# Function to interact with the OpenAI LLM
def chat_with_llm(user_input, chat_history=[]):
    # Append the user input to the chat history
    chat_history.append({"role": "user", "content": user_input})

    # Make API call to OpenAI's LLM
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",  # or "gpt-4" if available
        messages=chat_history
    )

    # Extract and format the assistant's response
    assistant_response = response["choices"][0]["message"]["content"]
    chat_history.append({"role": "assistant", "content": assistant_response})

    # Return assistant response and updated history
    return assistant_response, chat_history


# Wrapper function for Gradio UI
def gradio_chatbot(user_input, chat_history):
    response, chat_history = chat_with_llm(user_input, chat_history)
    return response, chat_history


# Set up Gradio interface
with gr.Blocks() as demo:
    gr.Markdown("## Chatbot powered by OpenAI's GPT")

    chatbot = gr.Chatbot()
    msg = gr.Textbox(label="Enter your message:")
    state = gr.State([])

    # When the user submits, update chat history and display response
    msg.submit(gradio_chatbot, inputs=[msg, state], outputs=[chatbot, state])

# Launch the Gradio app
if __name__ == "__main__":
    demo.launch(share=True)


