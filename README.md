This is proof of concept for ability to connect to mssql that put into docker from 
ubuntu host system from sqlalchemy.

Setup instructions.

1. Create directory with this repo.
2. Run ``` docker run -e 'ACCEPT_EULA=Y' -e 'SA_PASSWORD=b0Ssu098' -e 'MSSQL_PID=Express' -p 1433:1433 -d microsoft/mssql-server-linux:latest ```
This link `https://docs.microsoft.com/en-us/sql/linux/quickstart-install-connect-docker` for reference.
'SA_PASSWORD' variable should match sqlalchemy connection credentials and vice versa. 
3. activate virtual environment `. .env/bin/activate`
4. run `pip install -r requirements.txt`
5. run `python app.py`
6. Go to `http://127.0.0.1:5000/`



