from netmiko import ConnectHandler


csatlakozasi_adatok = {
    "device_type":"cisco_ios",
    "host" :"192.168.40.36",
    "username":"sshAdmin",
    "password":"Admin12",
        
}

try:
    with ConnectHandler(**csatlakozasi_adatok) as kapcsolat:
        pass

except Exception as ex:
        print("Hiba a csatlakozáskor: {ex}")