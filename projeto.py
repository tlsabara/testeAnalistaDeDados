#!/usr/bin/python

import argparse
from core_projeto.commands import create_commander

if __name__ == '__main__':
    cmd_ = create_commander()

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
        cmd_.configure_env()
        cmd_.init_airflow_cmd()

    if args.iniciar and args.parar:
        print("--iniciar e --parar não podem ser uitilizados juntamente")
        exit()

    if args.iniciar and not args.parar:
        cmd_.start_cmd()

    if args.parar and not args.iniciar:
        cmd_.stop_cmd()

    exit()