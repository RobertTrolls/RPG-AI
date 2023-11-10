import os
import time
import openai
import apikey
import speech_recognition as sr
from gtts import gTTS
import pyaudio
import tempfile
import wave

r = sr.Recognizer()

openai.api_key = "#########################" # <--- Put your API KEY here

cont = "S"

print(5 * "-", "Bem vindo a UnderWorld!", 5 * "-")
time.sleep(4)
print(34 * "-")
time.sleep(0.5)
print('Você deverá falar pelo seu microfone todas as características do seu personagem: ')
time.sleep(3)
print(34 * "-")
time.sleep(3)
with sr.Microphone() as source:
    name = print('Qual é o seu nome? : ')
    audio_text = r.listen(source)
    print('Feito!')
    name = r.recognize_google(audio_text, language='pt-BR')
time.sleep(0.5)
print(34 * "-")
with sr.Microphone() as source:
    work = print('Qual é o seu trabalho? : ')
    audio_text = r.listen(source)
    print('Feito!')
    work = r.recognize_google(audio_text, language='pt-BR')
time.sleep(0.5)
print(34 * "-")
with sr.Microphone() as source:
    wish = print('Qual é o seu desejo? : ')
    audio_text = r.listen(source)
    print('Feito!')
    wish = r.recognize_google(audio_text, language='pt-BR')
time.sleep(0.5)
print(34 * "-")
time.sleep(2)
print("Aguarde alguns instantes...")
print(34 * "-")
lista = []
saida = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=[{"role": "user", "content": f'ChatGPT, crie um mundo imaginário de RPG de mesa. O personagem principal se chama {name}, sendo um {work} que está em busca de {wish}. Você terá que simular o RPG sendo o mestre e comunicara comigo sendo o jogador. Use d&d como inspiração. Faça uma apresentação e espere a minha ação'}])
print(saida.choices[0].message.content)
lista.append(saida.choices[0].message.content)


def play_audio(text):
    tts = gTTS(text=text, lang='pt')
    filename = tempfile.mktemp('.mp3')
    tts.save(filename)
    chunk = 1024
    sample_format = pyaudio.paInt16
    channels = 2
    fs = 44100
    p = pyaudio.PyAudio()
    wf = wave.open(filename, 'rb')
    stream = p.open(format=p.get_format_from_width(wf.getsampwidth()),
                    channels=wf.getnchannels(),
                    rate=wf.getframerate(),
                    output=True)
    data = wf.readframes(chunk)
    while data != '':
        stream.write(data)
        data = wf.readframes(chunk)
    stream.stop_stream()
    stream.close()
    p.terminate()


while cont.upper() == 'S' or cont.upper() == 'SIM':
    time.sleep(0.5)
    print(34 * "-")
    comm = input(f'Qual será a próxima ação do(a) personagem {name}? (escreva) : ')
    print(34 * "-")
    time.sleep(2)
    print('Aguarde alguns instantes...')
    print(34 * "-")
    saida2 = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=[{"role": "user","content": f'{lista} minha ação foi {comm}. Continue a historia se baseando no texto acima'}])
    print(saida2.choices[0].message.content)
    lista.pop(0)
    lista.append(saida2)
    cont = input("\nDeseja visualizar mais informações? (escreva S - sim / N - não): ")
    time.sleep(0.2)
else:
    print("Opção inválida.")

print("Fim do Programa.")
