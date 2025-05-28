from num2words import num2words

def valor_pago_por_extenso(numero):
    #numero = "15.532,72"
    #numero = str(numero).replace(".","").replace(",",".")
    valor_por_extenso = num2words(numero, ordinal=False, lang='pt_BR', to='currency')
    return valor_por_extenso
# Converter para texto por extenso em português do Brasil

# Imprimir o resultado
print(valor_pago_por_extenso("15.532,72"))