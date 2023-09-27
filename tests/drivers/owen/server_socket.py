import asyncio


async def handle_connection(reader, writer):
    addr = writer.get_extra_info("peername")
    print("Соединение с", addr)
    while True:
        # Receive
        try:
            data = await reader.read(1024)
        except ConnectionError:
            print(f"Клиент внезапно закрылся во время получения от {addr}")
            break
        print(f"Получено {data} от: {addr}")
        if not data:
            break
        data = data
        print(f"Отправлено: {data} в: {addr}")
        try:
            writer.write(data)
            await writer.drain()
        except ConnectionError:
            print(f"Клиент внезапно закрылся, не удается отправить")
            break
    writer.close()
    print("Разъединение с", addr)


async def server(host, port):
    server_soc = await asyncio.start_server(handle_connection, host, port)
    print(f"Старт сервера")
    async with server_soc:
        await server_soc.serve_forever()

HOST = "localhost"
PORT = 50003

asyncio.run(server(HOST, PORT))
