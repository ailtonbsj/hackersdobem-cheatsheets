#!/bin/python

import os
import socket

# Função para coletar informações do sistema
def coletar_informacoes_sistema():
    hostname = socket.gethostname()
    kernel_version = os.uname().release
    cpu_info = os.popen('cat /proc/cpuinfo | grep "model name" | uniq').read().strip()
    mem_info = os.popen('free -h | grep "Mem:"').read().strip()
    disk_space = os.popen('df -h').read()

    informacoes = {
        "Hostname": hostname,
        "Kernel Version": kernel_version,
        "CPU Info": cpu_info,
        "Memory Info": mem_info,
        "Disk Space": disk_space
    }

    return informacoes

# Função para gerar um relatório
def gerar_relatorio(informacoes):
    relatorio = "Relatório do Sistema Linux\n\n"
    for chave, valor in informacoes.items():
        relatorio += f"{chave}: {valor}\n"

    with open("relatorio_linux.txt", "w") as arquivo:
        arquivo.write(relatorio)

if __name__ == "__main__":
    informacoes_sistema = coletar_informacoes_sistema()
    gerar_relatorio(informacoes_sistema)
    print("Relatório gerado com sucesso em 'relatorio_linux.txt'")

