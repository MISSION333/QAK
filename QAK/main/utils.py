import os 
import cohere
import replicate

os.environ["REPLICATE_API_TOKEN"] = 'r8_Iw1wpExr9YGs2s9TNdCKxr98ROt1pac2BxE6G'
co = cohere.Client('HtQ64yYsZGHmQPHALKE3y9WhqH7U5iItXSNMzLcW')

# response = co.generate(
#   prompt='',
#   max_tokens=250,
# )


def prompt_cohere(question):
    response = co.generate(
            prompt = f"{question}. make it simple , more understandable, easy to read ,and as sections.",
            max_tokens = 800,
            )

    # response[0].prompt, response[0].text
    return response

"""
Introdction: asdasdasd asdasd
Section 1: asdadasdasdd
Section 2: asdasdasd
Section 3: asdasdasd
Concluacion: asdasd
""
Introdction: asdasdasd asdasd
Section 1: asdadasdasdd
Section 2: asdasdasd
Section 3: asdasdasd
Concluacion: asdasd
""
Introdction: asdasdasd asdasd
Section 1: asdadasdasdd
Section 2: asdasdasd
Section 3: asdasdasd
Concluacion: asdasd
""
Introdction: asdasdasd asdasd
Section 1: asdadasdasdd
Section 2: asdasdasd
Section 3: asdasdasd
Concluacion: asdasd
""

"""


# print(prompt("mole"))


# Open AI GPT
# import openai
# OPENAI_API_KEY = "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"
# openai.api_key = OPENAI_API_KEY
# response = openai.Completion.create(
#         engine="gpt-3.5-turbo",
#         # model="text-davinci-003",
#         prompt="Write a tagline for an ice cream shop."
#         )
# print(response)


# openai.ChatCompletion.create(
#   model="gpt-3.5-turbo",
#   messages=[
#         {"role": "system", "content": "You are a helpful assistant."},
#         {"role": "user", "content": "Who won the world series in 2020?"},
#         {"role": "assistant", "content": "The Los Angeles Dodgers won the World Series in 2020."},
#         {"role": "user", "content": "Where was it played?"}
#     ]
# )



# replicate API

# import os;os.system("export REPLICATE_API_TOKEN=r8_Iw1wpExr9YGs2s9TNdCKxr98ROt1pac2BxE6G")

# REPLICATE_API_TOKEN ="r8_Iw1wpExr9YGs2s9TNdCKxr98ROt1pac2BxE6G"

def prompt_llama2(question):
    output = replicate.run(
            "replicate/llama-2-70b-chat:2796ee9483c3fd7aa2e171d38f4ca12251a30609463dcfd4cd76703f22e96cdf",
            input={"prompt": f"{question}. make it simple , more understandable, easy to read ,and as sections, make it as short article." },
            max_new_tokens=8000,
            # temperature=0.1,
            # top_p=0.7
            )
    return "".join(list(output))

# def prompt_llama2(question):
#     output = replicate.run(
#             "replicate/llama-2-70b-chat:2796ee9483c3fd7aa2e171d38f4ca12251a30609463dcfd4cd76703f22e96cdf",
#             input={"prompt": f"{question}. make it simple , more understandable, easy to read ,and as sections, make it as short article." },
#             max_new_tokens=8000,
#             temperature=0.1,
#             top_p=0.7
#             )
#     return "".join(list(output))



# question = "mole"
# # print("Cohere: \n\n\n")
# print(prompt_cohere(question)[0].text)


# print("LLAMA2: \n\n\n")
# print(prompt_llama2("c=mv^2"))
# The replicate/llama-2-70b-chat model can stream output as it's running.
# The predict method returns an iterator, and you can iterate over that output.
# for item in output:
    # https://replicate.com/replicate/llama-2-70b-chat/versions/2796ee9483c3fd7aa2e171d38f4ca12251a30609463dcfd4cd76703f22e96cdf/api#output-schema
    # print(item)
# breakpoint()
# print(output)
# print()


