from flask import Flask
from sqlalchemy import create_engine

# docker run -e 'ACCEPT_EULA=Y' -e 'SA_PASSWORD=b0Ssu098' -e 'MSSQL_PID=Express' -p 1433:1433 -d microsoft/mssql-server-linux:latest
app = Flask(__name__)
engine = create_engine('mssql+pymssql://SA:b0Ssu098@localhost:1433')
connection = engine.connect()


@app.route('/')
def index():
    result = connection.execute('SELECT Name from sys.Databases')
    return 'Hello '+str(result)


if __name__ == '__main__':
    app.run()
