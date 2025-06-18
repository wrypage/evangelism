import gradio as gr
from persona_profiles import PERSONAS
from chat_logic import chat_with_persona
from tts import speak_text

def run_chat(persona_name, user_input, audio_file):
    response = chat_with_persona(persona_name, user_input, audio_file)
    return response

with gr.Blocks() as demo:
    gr.Markdown("## Evangelism AI — Practice Conversations")

    persona_dropdown = gr.Dropdown(
        choices=list(PERSONAS.keys()),
        label="Choose a persona"
    )

    with gr.Row():
        text_input = gr.Textbox(
            placeholder="Type your message here...",
            label="Text Input"
        )
        audio_input = gr.Audio(
            sources=["microphone"],
            type="filepath",
            label="Or speak your message"
        )

    submit_btn = gr.Button("Submit")
    output_text = gr.Textbox(label="AI Response")

    submit_btn.click(
        fn=run_chat,
        inputs=[persona_dropdown, text_input, audio_input],
        outputs=output_text
    )

if __name__ == "__main__":
    demo.launch(server_name="0.0.0.0", server_port=7860)


