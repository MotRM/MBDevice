import multiprocessing
import socket
import pytest


def handle_connection(sock, addr):  # New
    with sock:
        print("Соединение с", addr)
        while True:
            try:
                data = sock.recv(1024)
            except ConnectionError:
                print(f"Клиент внезапно закрылся во время получения от {addr}")
                break
            print(f"Получено {data} от: {addr}")
            if not data:
                break
            print(f"Отправлено: {data} в: {addr}")
            try:
                sock.sendall(data)
                exit(0)
            except ConnectionError:
                print(f"Клиент внезапно закрылся, не удается отправить")
                break
        print("Разъединение с", addr)


def sever(HOST, PORT):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as serv_sock:
        serv_sock.bind((HOST, PORT))
        serv_sock.listen(1)
        print("Сервер запущен")
        while True:
            print("Ожидаю содинение")
            sock, addr = serv_sock.accept()
            p = multiprocessing.Process(target=handle_connection,
                                        args=(sock, addr))  # New
            p.start()


@pytest.fixture
def run_server():
    HOST = "localhost"
    PORT = 50003
    multiprocessing.Process(target=sever(HOST, PORT))
