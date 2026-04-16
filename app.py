from openai import OpenAI
from gtts import gTTS
import os

# Inicializa cliente OpenAI
client = OpenAI(api_key="SUA_CHAVE_AQUI")

# Pergunta do usuário (simulando voz)
pergunta = input("Faça sua pergunta comercial: ")

# Prompt com foco comercial
prompt_sistema = """
Você é um especialista em vendas e indicadores comerciais.
Responda de forma clara, objetiva e estratégica sobre:
- KPIs
- Conversão
- Churn
- CAC
- Ticket médio
- Performance de vendas
"""

# Gera resposta
resposta = client.responses.create(
    model="gpt-4.1-mini",
    input=[
        {"role": "system", "content": prompt_sistema},
        {"role": "user", "content": pergunta}
    ]
)

texto_resposta = resposta.output_text

print("\nResposta:")
print(texto_resposta)

# Converte resposta em áudio
tts = gTTS(texto_resposta, lang="pt")
tts.save("resposta.mp3")

print("\nÁudio gerado: resposta.mp3")
