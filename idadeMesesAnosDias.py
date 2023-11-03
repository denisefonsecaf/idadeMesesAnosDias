#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Faça um programa que leia a idade de uma pessoa expressa em dias e mostre-a expressa em anos, meses e dias.

idade_em_dias = int(input("Digite sua idade em dias: "))

idade_em_anos = idade_em_dias / 365 #Neste cálculo estamos levando em consideração que 1 ano tem 365 dias

idade_em_meses = (idade_em_dias / 365) * 12 

print(f"Sua idade em anos, meses e dias é: {int(idade_em_anos)} anos, {int(idade_em_meses)} meses e {idade_em_dias} dias.")