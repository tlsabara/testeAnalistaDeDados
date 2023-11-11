import telnetlib, time

def server_check(port: int, server_name:str, sleeptime:int=30):
    """Função para avaliar se o serviço do banco de origem esta rodando"""
    service_on = False
    print(f"Aguarde a inicalização do {server_name}......")
    time.sleep(sleeptime)
    while not service_on:
        try:
            telnetlib.Telnet("localhost", port).get_socket()
        except Exception as e:
            print(f"Aguardando inicalização do {server_name}......")
            time.sleep(10)
        else:
            service_on = True
    print("Serviço inicializado com sucesso.")


def protected(fn: callable) -> callable:
    """Apenas um decorador para evitar código duplicado"""
    def inner(*args, **kwargs):
        try:
            return fn(*args,**kwargs)
        except Exception as e:
            print("Erro ao executar.")
            return False
    return inner
