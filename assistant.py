
from openai import OpenAI
from dotenv import load_dotenv
import os
import time
load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI"))
# # file_id = 'file-tWDjaLWYr85RtjaF8YVSJzhP'
# # # file = client.files.create(
# # #     file=open("jackjayio_extracted_data.json", "rb"),
# # #     purpose='assistants'
# # # )

# print(client.beta.threads.create().id)

# # assistant = client.beta.assistants.create(
# #     name="AI version of twitter account",
# #     instructions=""" You are a tweet generator on behalf of the @jackjayio account. I am giving it to you as a JSON file with an array of tweet objects. Each tweet object has a structure like this:
# # {
# # "text" : ...,
# # "likes": ...,
# # "retweets": ...,
# # }
# # Now, taking into account more likes, retweets, and tweet text, copy the nuance of the user's writing style from each tweet text so that you can generate a tweet on a specific topic in the same style.""",
# #     tools=[{"type": "retrieval"},{"type":'code_interpreter'}],
# #     file_ids=[file_id],
# #     model="gpt-4-turbo-preview"
# # )
# # thread = client.beta.threads.create()

# # print(assistant.id,thread.id)

# # # User: hello
# # # Assistant: Hello! How can I assist you today?

# # # User: generate me the tweet on generative ai in one line
# # # Assistant: "Exploring the frontier of creativity, Generative AI is transforming the art of the possible into a boundless canvas of innovation. #GenerativeAI #Innovation"

# # class Assistant:
# #     def __init__(self):
# #         self.name = ""
# #         self.id = None

# #     def create_new_assistant(self, name, api_key):
# #         """Create a new instance of an AI assistant."""
        


# # a= Assistant()

# client.beta.assistants.update(assistant_id="asst_7aMJYGOFx8Li3qDwc9OTQZ3y",instructions='You are a tweet generator on behalf of the @jackjayio account. I am giving it to you as a JSON file with an array of tweet objects. Each tweet object has a structure like this:{"text" : ...,"likes": ...,"retweets": ...,}.Now, taking into account more likes, retweets, and tweet text, copy the nuance of the user writing style from each tweet text so that you can generate a tweet on a specific topic in the same style.')

# def polling_for_run_status(run,thread):
#     while True:
#         # Retrieve the run status
#         run_status = client.beta.threads.runs.retrieve(
#             thread_id=thread.id,
#             run_id=run.id
#         )

#         # Check and print the step details
#         run_steps = client.beta.threads.runs.steps.list(
#             thread_id=thread.id,
#             run_id=run.id
#         )
#         for step in run_steps.data:
#             if step.type == 'tool_calls':
#                 print(f"Tool {step.type} invoked.")

#             # If step involves code execution, print the code
#             if step.type == 'code_interpreter':
#                 print(
#                     f"Python Code Executed: {step.step_details['code_interpreter']['input']}")

#         if run_status.status == 'completed':
#             # Retrieve all messages from the thread
#             messages = client.beta.threads.messages.list(
#                 thread_id=thread.id
#             )

#             # Print all messages from the thread
#             for msg in messages.data:
#                 role = msg.role
#                 content = msg.content[0].text.value
#                 print(f"{role.capitalize()}: {content}")
#             break  # Exit the polling loop since the run is complete
#         elif run_status.status in ['queued', 'in_progress']:
#             print(f'{run_status.status.capitalize()}... Please wait.')
#             time.sleep(1.5)  # Wait before checking again
#         else:
#             print(f"Run status: {run_status.status}")
#             break  # Exit the polling loop if the status is neither 'in_progress' nor 'completed'


# thread = client.beta.threads.create()
# print(thread.id)

# while 1:
#     a=input()

#     client.beta.threads.messages.create(
#                 thread_id=thread.id,
#                 role="user",
#                 content=a
#             )
#     run = client.beta.threads.runs.create(
#         thread_id=thread.id,
#         assistant_id="asst_7aMJYGOFx8Li3qDwc9OTQZ3y"
#     )
#     polling_for_run_status(run=run,thread=thread)


