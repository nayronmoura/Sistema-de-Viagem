import menus
from Veiculo import veiculoController
from Motoristas import motoristacontroller
from Viagem import viagemController

def main():
    menus.main_menu()
    chose = int(input("Escolha uma opção: "))
    match chose:
        case 1:
            motoristacontroller.main()
        case 2:
            veiculoController.main()
        case 3:
            viagemController.main()

main()