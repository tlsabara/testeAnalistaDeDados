#!/usr/bin/python
import platform
import argparse
import os
from pathlib import Path

def protected(fn: callable) -> callable:

    def inner(*args, **kwargs):
        try:
            return fn(*args,**kwargs)
        except Exception as e:
            print("Erro ao executar.")
            return False
    return inner

@protected
def docker_cmd_windows_start() -> bool:
    os.system('cmd /c "cd ./docker_databases; docker compose up -d; exit"')
    os.system('cmd /c "cd ./airflow; docker compose up -d; exit"')
    return True

@protected
def docker_cmd_windows_stop() -> bool:
    os.system('cmd /c "cd ./docker_databases; docker compose down; exit"')
    os.system('cmd /c "cd ./airflow; docker compose down; exit"')
    return True


@protected
def docker_cmd_linux_start() -> bool:
    os.system('cd ./docker_databases && sudo docker compose up -d')
    os.system('cd ./airflow && sudo docker compose up -d')
    return True


@protected
def docker_cmd_linux_stop() -> bool:
    os.system('cd ./docker_databases && sudo docker compose down')
    os.system('cd ./airflow && sudo docker compose down')
    return True



if __name__ == '__main__':
    op_sys = platform.system()

    ROOT_DIR = Path(os.path.abspath(os.path.curdir))


    parser = argparse.ArgumentParser()

    parser.add_argument(
        "--configurar", "-c",
        help="Inicia o configurador",
        required=False,
        action="store_true"
    )
    parser.add_argument(
        "--iniciar", "-i",
        help="Inicia o ambiente (servidores no docker)",
        required=False,
        action="store_true"
    )
    parser.add_argument(
        "--parar", "-p",
        help="Inicia o ambiente (servidores no docker)",
        required=False,
        action="store_true"
    )

    args = parser.parse_args()

    if not args.iniciar and not args.configurar and not args.parar:
        print("Execute com '--configurar' ou '--iniciar'!!")
        input()

    if args.configurar:
        file = ROOT_DIR / "airflow" / ".env"
        email_inform = input("Digite o email para receber os informativos:")
        with open(file, "w") as fl:
            fl.write("AIRFLOW_UID=1000\n")
            fl.write(f"TARGET_MAIL={email_inform}")


    if args.iniciar and not args.parar:
        if op_sys == "Linux":
            docker_cmd_linux_start()
        if op_sys == "Wndows":
            docker_cmd_windows_start()

    if args.parar and not args.iniciar:
        if op_sys == "Linux":
            docker_cmd_linux_stop()
        if op_sys == "Wndows":
            docker_cmd_windows_stop()

    exit()