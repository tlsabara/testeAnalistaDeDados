import os
import platform
from pathlib import Path
from core_projeto.utils import server_check, protected

class DockerExecutor:
    """Classe para implementar a inversão de dependencia"""
    def __init__(self, start_cmd: callable, stop_cmd: callable, init_airflow_cmd: callable):
        self.start_cmd = start_cmd
        self.stop_cmd = stop_cmd
        self.init_airflow_cmd = init_airflow_cmd

    @staticmethod
    def configure_env():
        ROOT_DIR = Path(os.path.abspath(os.path.curdir))
        file = ROOT_DIR / "airflow" / ".env"
        email_inform = input("Digite o email para receber os informativos:")
        with open(file, "w") as fl:
            fl.write("AIRFLOW_UID=1000\n")
            fl.write(f"TARGET_MAIL={email_inform}")

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


@protected
def docker_cmd_linux_init_ariflow() -> bool:
    """Inicializa a configuração do airflow no linux"""
    os.system('cd ./airflow && sudo docker compose up airflow-init')
    return True


@protected
def docker_cmd_windows_init_ariflow() -> bool:
    """Inicializa a configuração do airflow no linux"""
    os.system('cd ./airflow; docker compose up airflow-init')
    return True


def create_commander():
    if platform.system() == "Windows":
        return DockerExecutor(
            start_cmd=docker_cmd_windows_start,
            stop_cmd=docker_cmd_windows_stop,
            init_airflow_cmd=docker_cmd_windows_init_ariflow
        )

    if platform.system() == "Linux":
        return DockerExecutor(
            start_cmd=docker_cmd_linux_start,
            stop_cmd=docker_cmd_linux_stop,
            init_airflow_cmd=docker_cmd_linux_init_ariflow
        )

    raise OSError("Plataforma/Arquitetura não implementada.")
