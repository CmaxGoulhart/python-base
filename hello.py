#!/usr/bin/env python3
"""Hello World Multi Linguas.

Dependendo da lingua configrada no ambiente
o programa exibe a mensagem correspondente.

Como usar:

Tenha a vari'avel lang devidamente configurada exemplo:

    export LANG=pt_BR

Execuçao:

    python3 hello.py
    ou
    ./hello.py  
"""
__verion__ = "0.0.1"
__author__="Claudio Max"
__license__="Unlicense"

# A palavra Dunder no começo substitui o pronunciamento de falar  2x underline
import os

current_language = os.getenv("LANG", "en_US")[:5]

msg = "Hello, World!"

if current_language == "pt_BR":
    msg = "Ola, Mundo!"
elif current_language == "it_IT":
    msg = "Ciao, Mondo!"    

print(msg)
