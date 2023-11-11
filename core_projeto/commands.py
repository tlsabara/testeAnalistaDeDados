import os
from core_projeto.utils import server_check, protected


@protected
def docker_cmd_windows_start() -> bool:
    """Inicializa os containers no windows"""
    os.system('cmd /c "cd ./docker_databases; docker compose up -d; exit"')
    server_check(port=10000, server_name="Servidor de Origem")
    os.system('cmd /c "cd ./airflow; docker compose up -d; exit"')
    server_check(port=8080, server_name="Servidor do Airflow", sleeptime=10)
    return True


@protected
def docker_cmd_windows_stop() -> bool:
    """Para a execução dos conainers no windows"""
    os.system('cmd /c "cd ./docker_databases; docker compose down; exit"')
    os.system('cmd /c "cd ./airflow; docker compose down; exit"')
    return True


@protected
def docker_cmd_linux_start() -> bool:
    """Inicializa os containers no linux"""
    os.system('cd ./docker_databases && sudo docker compose up -d')
    server_check(port=10000, server_name="Servidor de Origem")
    os.system('cd ./airflow && sudo docker compose up -d')
    server_check(port=8080, server_name="Servidor do Airflow", sleeptime=10)
    return True


@protected
def docker_cmd_linux_stop() -> bool:
    """Para a execução dos conainers no linux"""
    os.system('cd ./docker_databases && sudo docker compose down')
    os.system('cd ./airflow && sudo docker compose down')
    return True
