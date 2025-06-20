import gradio as gr
from chat_logic import chat_with_persona

def run_chat(persona_name, user_input, history):
    if not persona_name:
        return "", history  # Require persona selection

    response = chat_with_persona(persona_name, user_input)
    history = history or []
    history.append((user_input, response))
    return "", history, history  # update both chatbot display and internal state

def clear_chat():
    return "", [], []

with gr.Blocks() as demo:
    gr.Markdown("## Evangelism AI — Practice Conversations")

    persona_dropdown = gr.Dropdown(
        choices=["Joe", "Miranda", "Mark", "Cassidy"],
        label="Choose a persona",
        value=None
    )

    chatbot = gr.Chatbot(label="Conversation")

    text_input = gr.Textbox(
        placeholder="Type your message and hit Enter...",
        label="Your Message"
    )

    gr.Markdown("*Hit Enter to submit your message*")

    state = gr.State([])

    # Submit on Enter
    text_input.submit(
        fn=run_chat,
        inputs=[persona_dropdown, text_input, state],
        outputs=[text_input, chatbot, state]
    )

    # Clear button
    gr.Button("Clear").click(
        fn=clear_chat,
        outputs=[text_input, chatbot, state],
        show_progress=False
    )

if __name__ == "__main__":
    demo.launch(server_name="0.0.0.0", server_port=7860)
