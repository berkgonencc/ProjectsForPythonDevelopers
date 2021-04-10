"""
Collect an email address from the user and then find out if the user has
a custom domain name or a popular domain name. For example:

Input: mary.jane@gmail.com
Output: Hey Mary, I see your email is registered with Google. That's cool!.
Input: peter.pan@myfantasy.com
Output: Hey Peter, looks like you've got your own custom setup at MyFantasy. Impressive!.

This is a convenient python project that has a lot of use in the future.
The program helps get you the username and domain name from an email address.
"""

user_email = input("Enter an e-mail address: ").lower().strip()
user = user_email[:user_email.index('@')]
domain = user_email[user_email.index('@')+1:]

popular_domains = {'gmail.com': 'Google', 'hotmail.com': 'Microsoft',
                   'yahoo.com': 'Verizon Media', 'outlook.com': 'Microsoft'}

if '.' in user:
    user = user[:user.index('.')]

if domain in popular_domains.keys():
    print(f"Hey {user.capitalize()}, I see your email is registered with"
          f" {domain[:domain.index('.')].capitalize()}. That's cool!")
else:
    print(f"Hey {user.capitalize()}, looks like you've got your own custom setup at"
          f" {domain[:domain.index('.')].capitalize()}. Impressive!")

