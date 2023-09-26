#program to validate ip4 address 
# we know ip4 address consist of 4 parts and each part must be in btween 0-255 
#here we are using inbuilt python  funtion to check it
import ipaddress
 
def validate_ip_address(ip_address):
    
    try:
        ipaddress.ip_address(ip_address)
        print("IP address is valid")
    except ValueError:
        print("IP address is Invalid")

if __name__ == '__main__':
    s = input("Enter the ipv4 address to be validated : ")
    validate_ip_address(s)