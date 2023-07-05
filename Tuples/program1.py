""" Write a python program that scans an email address and forms a tuple of user name and domain

Sample Input:

22cs453@kpriet.ac.in

Sample output:

User name: 22cs452

Domain name: kpriet.ac.in """

def parse_email(email):
    username, domain = email.split('@')
    return (username, domain)

email_address = "22cs453@kpriet.ac.in"
username, domain = parse_email(email_address)

print("User name:", username)
print("Domain name:", domain)
