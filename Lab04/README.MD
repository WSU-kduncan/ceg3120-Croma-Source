Part 2 SSH
- I added my keypair to my proxy instance
- sudo ssh -i key.pem ubuntu@10.0.1.11 (Webserver1)
- sudo ssh -i key.pem ubuntu@10.0.1.10 (Webserver2)

Part 2 Haproxy
- install haproxy (sudo apt-get install haproxy)
- config files for haproxy is /etc/haproxy/haproxy.cfg
- ![haproxy](https://user-images.githubusercontent.com/77748353/199121929-abd1152e-dc0b-4a23-98f2-d5c0ad06f2d8.PNG)
- sudo systemctl restart haproxy
- https://www.haproxy.com/blog/haproxy-configuration-basics-load-balance-your-servers/

Part 2 Webserver
- install apache2 (sudo apt-get install apache2)
- I edited index.html located at /var/www/html (this is where the sever files are located because it's the default and I did not change it)\
- sudo systemctl restart apache2
- https://ubuntu.com/tutorials/install-and-configure-apache#3-creating-your-own-website

Proof of proxy
- ![Prox1](https://user-images.githubusercontent.com/77748353/199121951-7b0edccb-19a2-4d6b-ac32-72e66cbfac6c.PNG)
- ![Prox2](https://user-images.githubusercontent.com/77748353/199121956-8b7759d8-742b-4af2-adba-7bb452bdd1ca.PNG)
