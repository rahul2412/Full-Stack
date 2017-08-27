## Server Address
IP address : http://52.77.249.55/
app url : http://52.77.249.55/
ssh port : 2200
user: grader ( with sudo priveledge)

## firewall configuration (UFW)
1) default ssh port changed to 2200
2) ports allowed are 123(ntp), 80(http), 2200(ssh)
3) default outgoing allowed & incoming dennied. 

## Softwares installed
1) git
2) libapache2-mod-wsgi
3) postgresql 
4) apache2 
5) flask
6) other dependencies of flask project

## others
1) keys were generated for grader user
2) remote login for root is disabled
3) time configured according to utc
4) catalog project deployed on server with ip : http://52.77.249.55/
5) all packages updated

