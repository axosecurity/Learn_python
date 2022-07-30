
import os

mk = "sudo mkdir $HOME/axosecurity"


knock1 = "sudo subfinder -d domain | sudo tee /home/axosolaman/axosecurity/domain_subfinder.log"

domain1 = input("TARGET DOMAIN \n")

print(knock1)

#path = input("GIVE A PATH FOR SAVEING FILES\n")

os.system(mk)



#os.system("go install -v github.com/projectdiscovery/subfinder/v2/cmd/subfinder@latest")

os.system("sudo subfinder -d " + domain1 + " | sudo tee $HOME/axosecurity/" + domain1 + "_subfinder.log")

os.system("sudo ls $HOME/axosecurity | lolcat")


















