###### commands to run after git clone:

`docker build -t flask-mysql-login .`

`docker volume create mysql-volume`

**Create Table in MySQL: (type each commad)**

run mysql container

`docker pull mysql:latest`

`docker run --name flask-mysql -d -p 3306:3306 -e MYSQL_ROOT_PASSWORD=root -e MYSQL_DATABASE=usersdb -v mysql-volume:/var/lib/mysql mysql:latest`

go into mysql conatiner

`docker exec -it mysql mysql -u root -p`

password: root

`create database usersdb;`

`use usersdb;`

`CREATE TABLE users(
id INT AUTO_INCREMENT PRIMARY KEY,
username VARCHAR(50),
password VARCHAR(50)
);`

`exit`

**now run flask app:**

`docker run --name flask-login-app -d -p 5000:5000 flask-mysql-login:latest`

now open any browser go to 5000 port for localhost or any aws ec2.
