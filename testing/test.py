import cohere

co = cohere.Client('HtQ64yYsZGHmQPHALKE3y9WhqH7U5iItXSNMzLcW')

response = co.generate(
  prompt='hello',
  max_tokens=250,
)

"""
[cohere.Generation {
    id: 7f5942f6-dfb2-4521-a4f7-d7a8f83052c1
    prompt: hello
    text:  Hello, how can I help you today?
    likelihood: None
    finish_reason: None
    token_likelihoods: None
}]
"""


print(response[0].prompt, response[0].text)
