VPC
- allows user to set their own virtual private network up for instances created in AWS
![Petrock-VPC](https://user-images.githubusercontent.com/77748353/194653888-4a6457e0-6df7-4195-99d9-bcfc90e3d8af.PNG)


Subnet
- Allows users to split up a larger network into smaller address spaces allowing for control over what devices are attached to what subnets so you can secure for important devices onto one subnet and personal devices onto another.
![Petrock-Subnet](https://user-images.githubusercontent.com/77748353/194655170-7dd16db4-b550-419b-b436-adcec0d30242.PNG)


Internet Gateway
- allows your VPC to connect to the internet and the internet to connect to your VPC
- ![Petrock-VPC](https://user-images.githubusercontent.com/77748353/194655947-73623540-ab4f-4409-8353-e5f6e426f133.PNG)


Route Table
- directs traffic through what is called a route to through the subnet or gateway
- ![Petrock-routetable](https://user-images.githubusercontent.com/77748353/194656850-fe8abec0-a644-48d8-9c6d-c747ced27d35.PNG)


Security Groups
- allows users to set up port rules and what external ip addresses can use them.\
- ![Petrock-sg](https://user-images.githubusercontent.com/77748353/194657319-3295beac-c67d-4d8a-95fa-ba852b8e9cae.PNG)


Instance Setup
- Upon inital setup I had to copy my private key over to my new instance and used that to ssh into the new machine.
- I went into and copied /etc/hostnames and pasted into /etc/hostnames.old and editied the file so it would say Petrock-AMI
- copied /etc/hosts to /etc/hosts.old and within /etc/hosts added a line that says "127.0.1.1 Petrock-AMI"
-Used this guide https://www.tecmint.com/set-hostname-permanently-in-linux/
- ![Petrock-Hosts](https://user-images.githubusercontent.com/77748353/194659976-f3902d91-9b43-4275-a0db-3e0d74a0a9d5.PNG)
- ![Petrock-Hostname](https://user-images.githubusercontent.com/77748353/194659998-aed74a49-150f-47af-b6ea-b72a3d2f5bad.PNG)
