# DESAFIO 021 - Faça um programa em Python que abra e reproduza o áudio de um sistema MP3.

import pygame
pygame.mixer.init()
pygame.mixer.music.load('wavamostra.wav')
pygame.mixer.music.play()
input()
pygame.event.wait()

#fela da puta, a linguagem atualizou e o exercício ficou defasado, vá dar o cu