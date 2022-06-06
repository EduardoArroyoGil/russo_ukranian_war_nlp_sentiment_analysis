import openai


class GPT3:

    def __init__(self, api_key):
        self.api_key = api_key

    def query(self, prompt, engine="text-davinci-002", temperature=0.1, max_tokens=1000, top_p=1
             , frequency_penalty=0, presence_penalty=0):

        openai.api_key = self.api_key
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