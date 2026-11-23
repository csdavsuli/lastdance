from netmiko import ConnectHandler


csatlakozasi_adatok = {
    "device_type":"cisco_ios",
    "host" :"192.168.40.92",
    "username":"sshAdmin",
    "password":"Admin12",
        
}

try:
    with ConnectHandler(**csatlakozasi_adatok) as kapcsolat:
        #print(kapcsolat.find_prompt())
        
        print(kapcsolat.check_enable_mode())

        #startup conf mentes
        #print(kapcsolat.save_config())
        #send-command "---"
        
        #output=kapcsolat.send_command("show running-config")
        #print(output)
        
        #Mi az eszköz neve?
        
        #A1
        kimenet=kapcsolat.find_prompt()
        kimenet=kimenet.rstrip('#')
        print(kimenet)

        #A2
        
        print(kimenet[0:-1])

        #B
        kimenet=kapcsolat.send_command("show running-config").split('\n')
        #print(kimenet)
        
        i=0
        while  "hostname" not in kimenet[i]:
            i += 1
        
        print(kimenet[i].split(' ')[1]) 

        #C
        kimenet=kapcsolat.send_command("show running-config | include hostname").strip()
        print(kimenet.split(' ')[1])
        
        
        
        
        kimenet = kapcsolat.send_command('show vlan summary | include existing VLANs')
        
        print(f"VLANOK száma a kapcsolón: {kimenet.strip().split(':')[1].strip()}") 
except Exception as ex:
        print("Hiba a csatlakozáskor: {ex}")