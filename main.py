from attack.brute_force import brute_force_attack


def main():
    password = input("Digite a senha para teste: ")
    print(f"Senha definida: {password}")

    brute_force_attack(password)


if __name__ == "__main__":
    main()
