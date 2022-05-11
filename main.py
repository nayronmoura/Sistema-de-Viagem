from menus import main_menu

def init():
    main_menu()
    choose = int(input("Qual menu deseja acessar? "))
    match choose:
        case 1:
                motorista.main()
