
import gradio as gr

def respond(message):
    return f"AI Response: {message}"

ui = gr.Interface(fn=respond, inputs="text", outputs="text")
ui.launch()
