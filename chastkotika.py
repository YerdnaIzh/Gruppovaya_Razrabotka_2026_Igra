import os
import time
import random
import sys

# Цвета для терминала (работает в большинстве современных консолей)
RED = "\033[91m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
CYAN = "\033[96m"
WHITE = "\033[97m"
BOLD = "\033[1m"
RESET = "\033[0m"

# Список "страшных" фраз для имитации взлома
HACK_LINES = [
    "Инициализация обхода защиты...",
    "Подключение к удалённому серверу 192.168.1.1...",
    "Обход файрвола [OK]",
    "Сканирование открытых портов...",
    "Порт 22 (SSH) — уязвим",
    "Порт 80 (HTTP) — уязвим",
    "Порт 443 (HTTPS) — уязвим",
    "Порт 3306 (MySQL) — уязвим",
    "Загрузка эксплойта...",
    "Обход антивируса...",
    "Расшифровка паролей...",
    "Получение root-доступа...",
    "Копирование базы данных пользователей...",
    "Извлечение cookie-файлов...",
    "Подмена MAC-адреса...",
    "Маскировка под системный процесс...",
    "Установка бэкдора...",
    "Удаление логов...",
    "Соединение зашифровано (AES-256)",
    "Передача данных на сервер...",
]

FAKE_IPS = [
    "45.133.1.87", "185.220.101.4", "103.21.244.0",
    "91.219.236.12", "176.32.103.5", "203.0.113.42",
]

def slow_print(text, delay=0.03, color=GREEN):
    """Печатает текст посимвольно."""
    sys.stdout.write(color)
    for ch in text:
        sys.stdout.write(ch)
        sys.stdout.flush()
        time.sleep(delay)
    sys.stdout.write(RESET + "\n")


def progress_bar(label, duration=2.0, color=CYAN):
    """Рисует фейковый прогресс-бар."""
    total = 30
    sys.stdout.write(f"{color}{label} [")
    for i in range(total):
        sys.stdout.write("█")
        sys.stdout.flush()
        time.sleep(duration / total)
    sys.stdout.write(f"] 100%{RESET}\n")


def fake_hex_dump(lines=5):
    """Печатает псевдо-дамп памяти."""
    for _ in range(lines):
        addr = f"0x{random.randint(0x1000, 0xFFFF):04X}"
        data = " ".join(f"{random.randint(0, 255):02X}" for _ in range(8))
        print(f"{YELLOW}{addr}{RESET}  {data}")
        time.sleep(0.1)


def glitch_text(text, color=RED, flashes=4):
    """Эффект "глюка"."""
    for _ in range(flashes):
        junk = "".join(random.choice("!@#$%^&*<>/\\|01") for _ in range(len(text)))
        sys.stdout.write(f"\r{color}{BOLD}{junk}{RESET}")
        sys.stdout.flush()
        time.sleep(0.08)
    sys.stdout.write(f"\r{color}{BOLD}{text}{RESET}\n")


def matrix_rain(duration=1.5):
    """Короткий дождь из символов."""
    chars = "01ABCDEF!@#$%"
    width = 60
    end = time.time() + duration
    while time.time() < end:
        line = "".join(random.choice(chars) if random.random() > 0.3 else " "
                       for _ in range(width))
        print(f"{GREEN}{line}{RESET}")
        time.sleep(0.05)


def fake_hack():
    os.system("cls" if os.name == "nt" else "clear")
    time.sleep(0.3)

    slow_print(">>> ЗАПУСК HACKER_TOOL v3.7 <<<", delay=0.02, color=CYAN)
    slow_print("Подключение к консоли администратора...", delay=0.02)
    time.sleep(0.4)

    for i, line in enumerate(HACK_LINES, 1):
        color = GREEN if i % 3 else YELLOW
        slow_print(f"[{i:02d}] {line}", delay=0.015, color=color)
        time.sleep(random.uniform(0.15, 0.4))

        # Периодически показываем прогресс или дамп
        if i % 5 == 0:
            progress_bar("  Прогресс", duration=1.0)
        if i % 7 == 0:
            fake_hex_dump(3)

    print()
    progress_bar("Установка соединения", duration=2.0, color=CYAN)
    progress_bar("Копирование данных", duration=2.5, color=YELLOW)
    progress_bar("Шифрование пакетов", duration=1.5, color=GREEN)
    print()

    slow_print(">>> ДОСТУП ПОЛУЧЕН <<<", delay=0.05, color=RED)
    time.sleep(0.5)
    glitch_text("!!! СИСТЕМА ВЗЛОМАНА !!!")

    print()
    matrix_rain(1.2)
    print()

    slow_print(f"IP-адрес цели: {random.choice(FAKE_IPS)}", delay=0.02, color=YELLOW)
    slow_print("Root-пароль: " + "".join(random.choice("abcdef0123456789") for _ in range(16)),
               delay=0.02, color=RED)
    slow_print("Извлечено файлов: " + str(random.randint(1000, 9999)), delay=0.02, color=CYAN)
    slow_print("Удалено логов: " + str(random.randint(50, 500)), delay=0.02, color=GREEN)
    print()

    slow_print("Нажмите Enter для выхода...", delay=0.02, color=WHITE)
    input()


if __name__ == "__main__":
    try:
        fake_hack()
    except KeyboardInterrupt:
        print(f"\n{GREEN}Взлом отменён. (шутка){RESET}")