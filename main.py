from calculo import Calculo

def main():
        print(
        """
        Esta aplicação tem como finalidade demonstrar os valores que serão gastos 
        com combustivel durante uma viagem, com base no consumo do seu veículo, e 
        com a distância determinada por você!
        """
        )

        print('Os combustíveis disponíveis para este cálculo são:')
        print(' ° Álcool')
        print(' ° Dísel')
        print(' ° Gasolina')

        print('  ')

        try:
            quilometros = float(input('Quantos km vão ser percorridos\n'))
            consumo = float(input('Consumo de combustível do veículo(km/l)\n'))
            calculo = Calculo()
            print(
                calculo.calcular_gasto(quilometros, consumo)
            )
        except ValueError as erro:
            print('O valor recebido não é válido')
            exit()

if __name__=='__main__':
    main()

