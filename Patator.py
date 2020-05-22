# coding:utf8

import subprocess
import socket
import requests
import time
import os
import hashlib

class Pentools:
    def __init__(self):
        self.presentation="""   

    ██████╗  █████╗ ████████╗ █████╗ ████████╗ ██████╗ ██████╗  
    ██╔══██╗██╔══██╗╚══██╔══╝██╔══██╗╚══██╔══╝██╔═══██╗██╔══██╗
    ██████╔╝███████║   ██║   ███████║   ██║   ██║   ██║██████╔╝
    ██╔═══╝ ██╔══██║   ██║   ██╔══██║   ██║   ██║   ██║██╔══██╗
    ██║     ██║  ██║   ██║   ██║  ██║   ██║   ╚██████╔╝██║  ██║
    ╚═╝     ╚═╝  ╚═╝   ╚═╝   ╚═╝  ╚═╝   ╚═╝    ╚═════╝ ╚═╝  ╚═╝
                /\                                ______,....----,
  /VVVVVVVVVVVVVV|===================''''''''''''       ___,..-' 
  `^^^^^^^^^^^^^^|======================----------''''''         
                \/                                               
 [---]     Auteur:   Fayred         [---]
 [---]     Version: BETA 1.0        [---]
 [---] Date de création: 13/04/2020 [---]
 
 0/ Help
 1/ Scan_IP
 2/ Scan_Port
 3/ Dirforce
 4/ Hashbreaker
 5/ Serveur_Web
 6/ Listener
 99/ Terminal CMD
 [CTRL+C pour quitter]       
        """
        print(self.presentation)

    def Accueil(self):
        try:
            while 1:
                outils_a_utiliser=input("pentools/$> ").lower()
                if outils_a_utiliser == "0" or outils_a_utiliser == "help":
                    self.Help()
                elif outils_a_utiliser == "1" or outils_a_utiliser == "scan_ip":
                    self.Scan_IP()
                elif outils_a_utiliser == "2" or outils_a_utiliser == "scan_port":
                    self.Scan_Port("localhost")
                elif outils_a_utiliser == "3" or outils_a_utiliser == "dirforce":
                    self.Bruteforce_Arborescence_Web()
                elif outils_a_utiliser == "4" or outils_a_utiliser == "hashbreaker":
                    self.Hashbreaker()
                elif outils_a_utiliser == "5" or outils_a_utiliser == "serveur_web":
                    self.Serveur_Web()
                elif outils_a_utiliser == "6" or outils_a_utiliser == "listener":
                    self.Listener()
                elif outils_a_utiliser == "99" or outils_a_utiliser == "cmd":
                    while 1:
                        self.Terminal()
        except KeyboardInterrupt:
            time.sleep(0.1)
            print("<EXIT>")
            exit(0)

    def Help(self):
        print("""
    Help:
        - 1/ Scan_IP
        - 2/ Scan_Port
        - 3/ Dirforce (Obtention de l'arborescence d'un site avec une wordlist)
        - 4/ Hashbreaker (cassage de hash)
        - 5/ Serveur_Web
        - 6/ Listener
        - 99/ Terminal CMD
        """)

    def Scan_IP(self):
        try:
            for i in range(256):
                addr_ip="192.168.43."+str(i)
                commande=subprocess.Popen("ping {} -n 1".format(addr_ip), stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                out, err = commande.communicate()
                out=out.decode('latin1')
                if "Impossible" not in out:
                    print("[+] IP {} existante".format(addr_ip))
        except KeyboardInterrupt:
            self.ExceptionClavierBack()

    def Scan_Port(self, ip, delimiteur_port=(0, 65536)):
        try:
            for port in range(delimiteur_port[0], delimiteur_port[1]):
                s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                r=s.connect_ex((ip, port))
                if r == 0:
                    print("[+] Port >'{}' sur ip >'{}' OUVERT".format(port, ip))
        except KeyboardInterrupt:
            self.ExceptionClavierBack()

    def Bruteforce_Arborescence_Web(self, fichier="dirb.txt", url="https://google.com/"):
        try:
            with open(fichier, "r", encoding='utf8') as f:
                wordlist=f.read().split() 
            for mots in wordlist:
                r=requests.get(url+mots)
                if r.status_code != 404:
                    print("[+] Trouvé <{}> : {}{}".format(r.status_code, url, mots))      
        except KeyboardInterrupt:
            self.ExceptionClavierBack()

    def Hashbreaker(self, type_de_hash="md5", hash="098f6bcd4621d373cade4e832627b4f6", fichier="hashbreaker.txt"):  
        try:
            with open(fichier, 'r', encoding='utf8') as f:
                wordlist=f.read().split()  
            if type_de_hash == "md5":
                for mots in wordlist:
                    h=hashlib.md5(mots.encode())
                    h=h.hexdigest()
                    print(h, end="\r")
                    if h == hash:
                        print("\n[+] Hash cracké : {}".format(mots))
                        break
        except KeyboardInterrupt:
            self.ExceptionClavierBack()

    def Serveur_Web(self):
        pass
    
    def Listener(self):
        pass

    def Terminal(self):
        try:
            cmd=input("[PT] {}$/> ".format(os.getcwd()))
            subprocess.call(cmd, shell=True)
        except KeyboardInterrupt:
            self.ExceptionClavierBack()

    def ExceptionClavierBack(self):
        time.sleep(0.1)
        print("<BACK>")
        self.Accueil()

if __name__ == "__main__":
    Pentools=Pentools()
    Pentools.Accueil()