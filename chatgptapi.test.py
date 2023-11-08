#Matheus Antonio

import os
import time
import openai
import apikey

import RPG

openai.api_key = RPG.apikey

cont = "S"

print(5 * "-", "Bem vindo a UnderWorld", 5 * "-")
print(34 * "-")
time.sleep(0.5)
name = input("Digite o Nome do Personagem: ")
time.sleep(0.5)
print(34 * "-")
work = input("1-Mercenário\n2-Guerreiro\n3-Nobre\n4-Bárbaro\n5-Mago\n6-Ladino\nEscolha seu trabalho: ")
time.sleep(0.5)
print(34 * "-")
wish = input("Seu maior desejo (uma palavra): ")
time.sleep(0.5)
print(34 * "-")
lista=[]
saida = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=[{"role": "user","content": f'ChatGPT, crie um mundo imaginário de RPG de mesa. O personagem principal se chama {name}, sendo um {work} que está em busca de {wish}. Você terá que simular o RPG sendo o mestre e comunicara comigo sendo o jogador. Use d&d como inspiração. Faça uma apresentação e espere a minha ação'}])
print(saida.choices[0].message.content)
lista.append(saida.choices[0].message.content)
while cont.upper() == 'S' or cont.upper() == 'SIM':
    time.sleep(0.5)
    print(34 * "-")
    comm = input("Ação do Jogador: ")
    saida2 = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=[{"role": "user","content": f'{lista} minha ação foi {comm}. Continue a historia se baseando no texto acima'}])
    print(34 * "-")
    print(saida2.choices[0].message.content)
    lista.pop(0)
    lista.append(saida2)
    cont = input("\nDeseja visualizar mais informações? (S - sim / N - não): ")
    time.sleep(0.2)
else:
    print("Opção inválida.")

print("Fim do Programa.")
