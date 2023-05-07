PrimeiroSegmento = int(input("Primeiro Segmento: "))
SegundoSegmento = int(input("Segundo Segmento: "))
TerceiroSegmento = int(input("Terceiro Segmento: "))

if PrimeiroSegmento < SegundoSegmento + TerceiroSegmento and SegundoSegmento < PrimeiroSegmento + TerceiroSegmento and TerceiroSegmento < PrimeiroSegmento + SegundoSegmento:
    print("Os segmentos acima podem formar um triângulo ")
    if PrimeiroSegmento == SegundoSegmento == TerceiroSegmento:
        print("Os segmentos acima podem formar um triângulo EQUILÀTERO\n Todos os lados são iguais")
    elif PrimeiroSegmento != SegundoSegmento != TerceiroSegmento != PrimeiroSegmento:
        print("Os segmentos acima podem formar um triângulo ESCALENO\n Todos os lados são diferentes" )
else:
    print("Os segmentos acima podem formar um triângulo ISÒSCELES\n Os dois lados são iguais e um é diferente")