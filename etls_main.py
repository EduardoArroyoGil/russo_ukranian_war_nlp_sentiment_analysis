print('dentro de etl')
import openai.openai_connection as openai_connection


response_openai = openai_connection.query.gpt3(prompt='Que dia es hoy?')
print(response_openai)