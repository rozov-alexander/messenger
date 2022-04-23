"""5. Выполнить пинг веб-ресурсов yandex.ru, youtube.com и преобразовать 
результаты из байтовового в строковый тип на кириллице."""


import subprocess
import platform
from chardet import detect

code = '-n' if platform.system().lower() == 'windows' else '-c'
args_1 = ['ping', 'yandex.ru', code, '4']
args_2 = ['ping', 'youtube.com', code, '4']
def ping_server(*args):
    subproc_ping = subprocess.Popen(args, stdout=subprocess.PIPE)
    for line in subproc_ping.stdout:
        res = detect(line)
        line = line.decode(res['encoding']).encode('utf-8')
        print(line.decode('utf-8'))

ping_server(*args_1)
ping_server(*args_2)