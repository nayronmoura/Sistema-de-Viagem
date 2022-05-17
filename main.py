import menus
import Veiculo.veiculoController as veiculo
import Motoristas.motoristacontroller as motorista
import Viagem.viagemController as viagem


def main():
    while True:
        menus.main_menu()
        chose = int(input("Escolha uma opção: "))
        match chose:
            case 1:
                motorista.main()
            case 2:
                veiculo.main()
            case 3:
                viagem.main()
            case 4:
                break


main()
