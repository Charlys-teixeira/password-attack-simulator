import itertools
import time
import string
import os


def load_wordlist():
    try:
        base_path = os.path.dirname(os.path.dirname(__file__))
        wordlist_path = os.path.join(base_path, "wordlist.txt")

        with open(wordlist_path, "r") as file:
            return [line.strip() for line in file]

    except FileNotFoundError:
        print("Wordlist não encontrada, pulando etapa...")
        return []


def check_wordlist(target_password, wordlist):
    print("\nTestando wordlist...")

    for pwd in wordlist:
        if pwd == target_password:
            print("Senha encontrada na wordlist:", pwd)
            return True

    return False


def estimate_time(target_password, charset, attempts_per_second=100000):
    password_length = len(target_password)
    charset_size = len(charset)

    total_combinations = charset_size**password_length
    estimated_time = total_combinations / attempts_per_second

    print("\n=== ESTIMATIVA ===")
    print("Combinações:", total_combinations)
    print("Tempo estimado (s):", estimated_time)
    print("==================\n")

    return estimated_time


def show_results(attempts, start_time):
    total_time = time.time() - start_time
    speed = attempts / total_time if total_time > 0 else 0

    print("Tentativas:", attempts)
    print("Tempo:", total_time)
    print("Velocidade:", speed)


def brute_force(target_password, charset, time_limit=10):
    start_time = time.time()
    attempts = 0

    for length in range(1, len(target_password) + 1):
        print(f"Tentando senhas com tamanho {length}")

        for combination in itertools.product(charset, repeat=length):
            attempt = "".join(combination)
            attempts += 1

            if time.time() - start_time > time_limit:
                print("\nTempo limite atingido.")
                show_results(attempts, start_time)
                return False

            if attempt == target_password:
                print("\nSenha encontrada:", attempt)
                show_results(attempts, start_time)
                return True

    print("\nSenha não encontrada.")
    show_results(attempts, start_time)
    return False


def brute_force_attack(target_password):
    print("Iniciando ataque...")

    # 🔹 WORDLIST
    wordlist = load_wordlist()
    if wordlist and check_wordlist(target_password, wordlist):
        return

    # 🔹 CONFIG
    charset = string.ascii_letters + string.digits

    # 🔹 ESTIMATIVA
    estimated_time = estimate_time(target_password, charset)

    if estimated_time > 30:
        print("Senha muito complexa para brute force em tempo razoável.")
        return

    # 🔹 BRUTE FORCE
    brute_force(target_password, charset)
