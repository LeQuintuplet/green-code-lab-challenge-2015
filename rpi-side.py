# fonction pour variables et librairies locales
def main():
    # import utiles uniquement
    from  socket import socket, AF_INET, SOCK_DGRAM, SOCK_STREAM
    from time import time,strftime
    from  datetime import datetime
    ss = socket
    # création socket UDP pour récepetion des paquets
    sockUDP = ss(AF_INET, SOCK_DGRAM)
    sockUDP.bind(('', 514))
    # création socket TCP pour transmition sure des données
    sockTCP = ss(AF_INET, SOCK_STREAM)
    sockTCP.connect(('51.255.62.22', 12345))

    while 1:
        # réception des données en UDP
        data, addr = sockUDP.recvfrom(1024)
        # ajout timestamp
        temps = datetime.fromtimestamp(time()).strftime('%b %e %R:%S')
        # envoi
        sockTCP.send( "%s %s" % ( temps, data ) )
        
        # Version avec traitement des caractères spéciaux
        # remplacer la ligne 21 par les deux lignes ci dessous pour l'utiliser
        #msgList = [ (c if ord(c) >= 32 else "#" + str( oct( ord(c) ) )) for c in data[:-1] ]
        #sockTCP.send( "%s %s\n" % ( temps, "".join(msgList) ) )
        

main()
