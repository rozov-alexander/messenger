"""5. Выполнить пинг веб-ресурсов yandex.ru, youtube.com и преобразовать 
результаты из байтовового в строковый тип на кириллице."""


import subprocess

args_1 = ['ping', 'yandex.ru', '-c', '4']
args_2 = ['ping', 'youtube.com', '-c', '4']

def ping_server(*args):
    subproc_ping = subprocess.Popen(args, stdout=subprocess.PIPE)
    for line in subproc_ping.stdout:
        line = line.decode('cp866').encode('utf-8')
        print(line.decode('utf-8'))

ping_server(*args_1)
ping_server(*args_2)