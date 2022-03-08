class Calculo:
    def __init__(self):
        self.__valor_gasolina = 6.20
        self.__valor_alcool = 5.30
        self.__valor_diesel = 4.10

    def calcular_gasto(self, quilometros, consumo):
        if(quilometros <= 0 or consumo <= 0):
            raise Exception('O valor recebido não pode ser menor ou igual a zero')

        gasto_gasolina = round(
            (quilometros/consumo) * self.__valor_gasolina,2)
        gasto_alcool = round(
            (quilometros / consumo) * self.__valor_alcool, 2)
        gasto_diesel = round(
            (quilometros / consumo) * self.__valor_diesel, 2)

        return """
        O valor total gasto será de:
        
        Gasolina: R${}
        Álcool:   R${}
        Diesel:   R${}
        """.format(
            gasto_gasolina, gasto_alcool, gasto_diesel
        )