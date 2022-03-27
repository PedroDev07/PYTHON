import ipaddress
import re

ip = '192.168.10.10'

endereco = ipaddress.ip_address(ip)
print(endereco + 2880)

faixa_rede = '192.168.100.3/24'
rede = ipaddress.ip_network(faixa_rede, strict=False)
print(rede)