import sys

sys.path.append('/usr/local/nsti')
from server import app as application

app.secret_key = 'mysecretkey'
