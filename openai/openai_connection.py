import openai
print('dentro de openai')

class query:

    def __init__(self):
        pass

    def gpt3(self, prompt, api_key='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'
             , engine="text-davinci-002", temperature=0.1, max_tokens=1000, top_p=1
             , frequency_penalty=0, presence_penalty=0):

        openai.api_key = api_key
        response = openai.Completion.create(
            engine=engine,
            prompt=prompt,
            temperature=temperature,
            max_tokens=max_tokens,
            top_p=top_p,
            frequency_penalty=frequency_penalty,
            presence_penalty=presence_penalty
        )

        content = response.choices[0].text.split('.')

        return response.choices[0].text