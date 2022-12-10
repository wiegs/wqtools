# Collect API key from Delinea SecretServer Online
# you will need this SDK first: python -m pip install python-tss-sdk

from delinea.secrets.server import AccessTokenAuthorizer
from delinea.secrets.server import SecretServer

my_url = "https://hostname/SecretServer"       # customize to your URL
my_authorizer = AccessTokenAuthorizer("")      # collect from the Web UI

secret_server = SecretServer(my_url, my_authorizer)

secret = secret_server.get_secret(213)

print(f"username: {secret.fields['username'].value}\npassword: {secret.fields['password'].value}")
