from settings import MENU, resources

# TODO 0 - Funções da Coffee Machine
make_coffee = True


def coffee_supply(cafe_client):
    """Função avalia se há material suficiente para fazer o café solicitado"""

    if cafe_client == MENU["espresso"]:
        if cafe_client["ingredients"]["water"] > resources["water"]:
            print("Sorry there is not enough water.")

            return False

        elif cafe_client["ingredients"]["coffee"] > resources["coffee"]:
            print("Sorry there is not enough coffee.")
            return False
        else:
            return True

    else:
        if cafe_client["ingredients"]["water"] > resources["water"]:
            print("Sorry there is not enough water.")
            return False

        elif cafe_client["ingredients"]["milk"] > resources["milk"]:
            print("Sorry there is not enough milk.")
            return False

        elif cafe_client["ingredients"]["coffee"] > resources["coffee"]:
            print("Sorry there is not enough coffee.")
            return False
        else:
            return True


def inventory_consuption():
    """Essa função calcula o inventório atual de materiais necessário para preparar o café"""
    if cafe_client == MENU["espresso"]:
        for ingrediente in ["water", "coffee"]:
            resources[ingrediente] -= cafe_client["ingredients"][ingrediente]
    else:
        for ingrediente in ["water", "milk", "coffee"]:
            resources[ingrediente] -= cafe_client["ingredients"][ingrediente]


def purchase_fulfillment(total, cafe_client):
    """Essa função avalia se o pagamento inserido é suficiente para processar a ordem e se é necessário devolver
    troco para o cliente. """

    if total > cafe_client["cost"]:
        change = total - cafe_client["cost"]
        print(f"Here is ${change} in change.")

    elif total == cafe_client["cost"]:
        print("I will make your coffee right the way!")

    elif total < cafe_client["cost"]:
        print("Sorry that's not enough money. Money refunded.")
        return False


# TODO 1 - Perguntar ao cliente qual a opção de café ele deseja.

while make_coffee:

    choice = input("What would you like? (espresso/latte/cappuccino): ").lower()

    # TODO 2 - Gera report ou desliga a coffee machine

    if choice == "report":
        print("Water: " + f"{resources['water']}mL")
        print("Milk: " + f"{resources['milk']}mL")
        print("Coffee: " + f"{resources['coffee']}mL")

    elif choice == "off":
        make_coffee = False

    # TODO 3 - Avaliar se há material sufiente para fazer o café

    else:
        cafe_client = MENU[choice]

        if not coffee_supply(cafe_client):

            print("You can't buy now")
            make_coffee = False

        else:

            # TODO 4 - Solicitar pagamento. Quaters, dimes, nickels, pennies.

            print(f"A {choice} costs " + f"${cafe_client['cost']}")
            print("Please insert coins.")
            quaters = float(input("how many quarters?: "))
            dimes = float(input("how many dimes?: "))
            nickles = float(input("how many nickles?: "))
            pennies = float(input("how many pennies?: "))
            total = (quaters * 0.25) + (dimes * 0.10) + (nickles * 0.05) + (pennies * 0.01)

            # TODO 5 - Avaliar se o pagamento realizado é suficiente para comprar o café desejado.

            if purchase_fulfillment(total, cafe_client) == False:
                make_coffee = False

            else:
                # TODO 6 - Preparar café

                print(f"Here is your {choice}. Enjoy! ☕️")

        # TODO 7 - Report status do material existente (Só é possível prosseguir com o preparo do café se houver material suficiente)
        if make_coffee:
            inventory_consuption()

