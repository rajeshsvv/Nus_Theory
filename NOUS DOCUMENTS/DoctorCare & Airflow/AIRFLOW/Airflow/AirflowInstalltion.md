# Airflow Installation on CentOS 7
This file demonstrates installation of Python 3.6, Apache airflow on CentOS 7 and 
configuring PostgreSQL database as the meta database for airflow instead of the default SQLite database

## Software Requirements
* CentOS 7 <br>
* Python 3.6.7
* Airflow 1.10
* PostgreSQL 11

## Prerequisites

Root access to CentOS 7 machine

## System update commands

    [root@localhost ~]# yum update
    
    [root@localhost ~]# yum install yum-utils
    
    [root@localhost ~]# yum groupinstall development

## Installing Python 3.6

    [root@localhost ~]# yum install https://centos7.iuscommunity.org/ius-release.rpm
    
    [root@localhost ~]# yum install python36u
    
    [root@localhost ~]# yum install python36u-pip
    
    [root@localhost ~]# yum install python36u-devel

Testing you Python 3.6 installation

    [root@localhost ~]# python3.6 –V

## Installing Postgres 11

    yum update      # Only if necessary
    
    rpm -Uvh https://download.postgresql.org/pub/repos/yum/11/redhat/rhel-7-x86_64/pgdg-centos11-11-2.noarch.rpm

    yum install postgresql11-server postgresql11-contrib
    
    /usr/pgsql-11/bin/postgresql-11-setup initdb
    
    systemctl start postgresql-11.service
   
To check if PostgreSQL is running

    ps -eaf | grep postgres 
    
    
#### To access the PostgreSQL console to type commands

    [root@localhost ~]# sudo su - postgres
    
    -bash-4.2$ psql 
    
Creating database for airflow and adding user in PostgreSQL database
    
    postgres=# CREATE USER <your_username_here> PASSWORD '<your_password_here>';
    
    postgres=# CREATE DATABASE your_database_name;
    
    postgres=# GRANT ALL PRIVILEGES ON ALL TABLES IN SCHEMA public TO <your_username_here>;
    
    postgres=# ALTER USER <your_username-here> SUPERUSER;
    
    postgres=# ALTER USER <your_username-here> CREATEDB;
    
If it is PostgreSQL role instead of user then use commands below

    postgres=# ALTER ROLE <your_username-here> SUPERUSER;
    
    postgres=# ALTER ROLE <your_username-here> CREATEDB;
    
    postgres=# ALTER ROLE <your_username-here> WITH LOGIN;
    
Restart of PostgreSQL is required. To restart the PostgreSQL service

    [root@localhost ~]# systemctl restart postgresql-11.service
    
Changing the necessary PostgreSQL configuration files to help airflow connect to PostgreSQL database
 
    [root@localhost ~]# sudo su - postgres
    
    -bash-4.2$ cd <postgresql_version_directory>/data
    
Once in this directory we need to edit two file

* pg_hba.conf

    Under IPv4 Local Connections
        
        TYPE    DATABASE    USER    ADDRESS            METHOD
        
        \# IPv4 Local Connections:
        host    all         all     127.0.0.1/32       trust
    
* postgresql.conf

    Under Connection Settings 
    
        # — Connection Settings -
        #listen_addresses = ‘localhost’     # what IP address(es) to listen on;
        listen_addresses = ‘*’              # Add this line for Apache-Airflow connection
    
Restart of PostgreSQL is required after changing the config files. To restart the PostgreSQL service

    [root@localhost ~]# systemctl restart postgresql-11.service

    
## Create a virtual environment to set up airflow

    [root@localhost ~]# python3.6 -m venv <your_environment_name>
    
    [root@localhost ~]# . <your_environment_name>/bin/activate

## Installing Apache airflow

    [root@localhost ~]# AIRFLOW_GPL_UNIDECODE=yes pip install apache-airflow[postgres]
    
Change directory to airflow home to edit the airflow.cfg file. Change the SQLalchemy connection string to point to PostgreSQL instead of SQLite

    sql_alchemy_conn = postgresql+psycopg2://<postgresql_username>@127.0.0.1:5432/<database_name>
    
    Example:
    sql_alchemy_conn = postgresql+psycopg2://nmathew@127.0.0.1:5432/airflow


Save the changes in config and initialize the airflow database using below:

    [root@localhost ~]# airflow initdb
    
Open new terminal and start the airflow scheduler

    [root@localhost ~]#  airflow scheduler
    
Open another new terminal and start the airflow webserver 

    [root@localhost ~]#  airflow webserver 

Open your web browser and navigate to http://localhost:8080 to view the airflow UI
