# If, Elif, Else Challenge

"""
Create a program that, depending on the temperature (in Celsius) of the steak,
returns the cooking point in Portuguese. The user must provide the temperature.

Temperatures - Cooking
< 120° or 48°C - Cook for a few more minutes (Cozinhar por mais alguns minutos)
120°F or 48°C - Rare (Selada)
130°F or 54°C - Medium rare (Ao ponto para o mal)
140°F or 60°C - Medium (Ao ponto)
150°F or 65°C - Medium well (Ao ponto para o bem)
>= 160°F or 71°C - Well done (Bem passada)
"""

temperature = int(input('Qual a temperatura da carne (em Celsius)? '))
message = ''

if temperature < 48:
    message = 'Cozinhar por mais alguns minutos'
elif 54 > temperature >= 48:
    message = 'Selada'
elif 60 > temperature >= 54:
    message = 'Ao ponto para o mal'
elif 65 > temperature >= 60:
    message = 'Ao ponto'
elif 71 > temperature >= 65:
    message = 'Ao ponto para o bem'
else:
    message = 'Bem passada'

print(message)
