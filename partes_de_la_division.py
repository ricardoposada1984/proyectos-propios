
print('============  Bienvenido (a) ====================')
print('============  Hoy vamos a aprender ==============')
print('============  las partes de la división ======== ')
print('============  :) :) :) :) :) :) :) :):) =========')

print('')

print('========= Las divisiones n/m dan lugar  ==========')
print('========  a un cociente y a un residuo  ==========')
print('========= que satisfacen el algoritmo ============')
print('=== de la division  n = cociente*m + residuo =====')
print('=== donde n: numerador y m : denominador  ========')
print('===============  :) :) :) :) =====================')

print(' ')
print("""compruebalo tu mismo,
identifica las partes de la division""")
print('y verifica que se cumple el algoritmo')


numerador = input('Escribe el numerador de tu fraccion: ')
denominador = input('Escribe el denominador de tu fraccion: ')
n = int(numerador)
m = int(denominador)

cociente = int(round(n/m, 0))
residuo = int(n % m)

print(f"""la division {n}/{m} tiene como cociente {cociente}
y como residuo {residuo}""")
print(f"""Se cumple el algoritmo de la división ?,
es decir:  {n} = {m}*{cociente} + {residuo} ??""")

