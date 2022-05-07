from menus import main_menu
from Motoristas import motoristacontroller as motorista
def init():
    main_menu()
    choose = int(input("Qual menu deseja acessar? "))
    match choose:
        case 1:
                motorista.main()
