# fonction pour variables et librairies locales
def main():
    # import utiles uniquement
    from socket import socket,AF_INET,SOCK_STREAM
    from time import time

    timestampOld = 0
    # création socket TCP pour récepetion des paquets
    sock = socket(AF_INET, SOCK_STREAM)
    sock.bind(('', 12345))
    # on accepte une connexion only, on en accepte une seule en attente
    sock.listen(1)
    conn, addr = sock.accept()

    while True:
        # réception des données en TCP et sauvegarde heure de réception
        data, timestamp = conn.recv(1024), time()
        # ouverture du fichier en append ou en rewrite si dernière transmition reçu il y a plus de 5min
        f = open("/opt/gclc/gclc.log", "w" if (timestamp-timestampOld > 300) else "a")
        # timestamp après réception
        timestampOld = timestamp
        # écrire fichier 
        f.write(data)
        f.close()

main()
