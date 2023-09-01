import cohere
co = cohere.Client('HtQ64yYsZGHmQPHALKE3y9WhqH7U5iItXSNMzLcW')
# response = co.generate(
#   prompt='',
#   max_tokens=250,
# )
def prompt(question):
    response = co.generate(
            prompt=question,
            max_tokens=550,
            )

    # response[0].prompt, response[0].text
    return response


# print(response)
