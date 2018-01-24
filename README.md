This is proof of concept for ability to connect to mssql that put into docker from 
ubuntu host system from sqlalchemy.

Setup instructions.

1. Create directory with this repo.
2. Run ``` docker run -e 'ACCEPT_EULA=Y' -e 'SA_PASSWORD=b0Ssu098' -e 'MSSQL_PID=Express' -p 1433:1433 -d microsoft/mssql-server-linux:latest ```
This link `https://docs.microsoft.com/en-us/sql/linux/quickstart-install-connect-docker` for reference.
'SA_PASSWORD' variable should match sqlalchemy connection credentials and vice versa. 
3. Enter docker container `docker exec -it <container_id> bash`
4. Run `/opt/mssql-tools/bin/sqlcmd -S localhost -U SA -P 'b0Ssu098'`
5. In sql command prompt run `CREATE DATABASE testdb` and on next string type `go` and press `Enter`
6. You can check that database is created by query `SELECT Name from sys.Databases`. Remember that you should type query and then type `go` on next string and then query will be executed. After creating database and tables you can exit.
7. Go to folder that contains `app.py` and activate virtual environment `. .env/bin/activate`
8. run `pip install -r requirements.txt`
9. run `python app.py`
10. Go to `http://127.0.0.1:5000/`



