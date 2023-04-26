Creat a gunicorn service in ubuntu:

1) Create a file named file.service in "/etc/systemd/system".

2) Run below command after that activate virtual enviroment:
pip install gunicorn
apt install gunicorn

3)grant permissions to a user in MySQL:

mysql> CREATE USER 'monty'@'localhost' IDENTIFIED BY 'some_pass'

mysql> GRANT ALL PRIVILEGES ON *.* TO 'monty'@'localhost' WITH GRANT OPTION;

mysql> CREATE USER 'monty'@'%' IDENTIFIED BY 'some_pass';

mysql> GRANT ALL PRIVILEGES ON *.* TO 'monty'@'%' WITH GRANT OPTION;

https://stackoverflow.com/questions/1559955/host-xxx-xx-xxx-xxx-is-not-allowed-to-connect-to-this-mysql-server#:~:text=1040-,Possibly,-a%20security%20precaution