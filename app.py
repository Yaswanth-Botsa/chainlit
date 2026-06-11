import chainlit as cl

from upsc_guard import is_upsc_related
from groq_service import get_groq_response


@cl.on_chat_start
async def start():
    await cl.Message(
        content="# Chat Bot for UPSC"
    ).send()
@cl.on_message
async def main(message: cl.Message):

    user_query = message.content

    if not is_upsc_related(user_query):

        await cl.Message(
            content="Invalid Query. Please ask only UPSC-related questions."
        ).send()

        return

    response = get_groq_response(user_query)

    await cl.Message(
        content=response
    ).send()