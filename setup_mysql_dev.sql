-- creates the database hbnb_dev_db and the user hbnb_dev
CREATE DATABASE IF NOT EXISTS hbnb_dev_db;
CREATE USER iF NOT EXISTS hbnb_dev@localhost;
GRANT ALL PRIVILEGES ON hbtn_dev_db TO hbnb_dev@localhost IDENTIFIED BY 'hbnb_dev_pwd';
GRANT SELECT ON `performance_schema`.* TO 'hbnb_dev'@'localhost';
