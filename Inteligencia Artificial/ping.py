from scapy.all import ICMP, IP, sr1

# Crear un paquete ICMP (ping)
ping_packet = IP(dst="192.168.0.4") / ICMP()

# Enviar el paquete y recibir la respuesta
response = sr1(ping_packet, timeout=2)

# Verificar si se recibió una respuesta
if response:
    print("Respuesta recibida desde", response.src)
else:
    print("No se recibió respuesta.")
