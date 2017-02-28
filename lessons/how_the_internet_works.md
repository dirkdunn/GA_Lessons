# How the Internet works
- Explain how the internet works, including what web server is and what a client is
- Differentiate between internet and web
- Explain what protocols are
- Explain what TCP/IP is
- IP Addresses
- Define DNS and identify its role in the client-server relationship
- Define HTTP and differentiate it from other protocols
- List some common HTTP response codes
- Explain what SSL is (high level)
- Describe the role of ports for incoming/outgoing data
- Explain what a REST API is
- List the HTTP verbs most relevant to REST API's


https://www.youtube.com/watch?v=7_LPdttKXPc&t=190s

### How does the internet work?  
Draw the internet model, and go through the process of it:

Client - Server relationship

What is a web server?

### The Internet VS The web  
The web is linked hypertext documents
It is software that actually takes you from one place to another using protocols.

The internet is an international connection of networks, it is a world wide connection of computer networks.

you can use the internet without the web, but not the web without the internet  
text messaging
voip

### What are protocols?  
A **protocol** is a procedure or a system of rules.  

On the internet, protocol refers to the procedure or way that networks communicate with eachother.


### IP Addresses  
An IP address is a number that is used in order for your computer to have a location.

It is the mailing address equivalent of your computer

**192.168.0.16**  
**|---------|--|  **  
**Network Code, Host ID**

Network ID is:
Host ID is:

### TCP/IP
**IP Protocol** - (Internet Protocol )In charge of routing information to different computers & devices. It's what allows two computers to figure out where the other one is.

Windowing is the process of sending data from one endpoint to another

**TCP** -   
It's what breaks it down to packets  

When going from one computer to another, we need a way to know the quality of the transmission, in order to know how much data we can send.

IP Connects the computers together, TCP is then what deals with the communication between computers

[Protocol Activity](https://gist.github.com/dirkdunn/4a01254d8faab7fedc8b2c3f9f35f0f2)

### What is DNS?  
DNS stands for Domain Name Service, It's what translates the domain name you type into your browser to an IP address that can be used to find the server you are looking for.

ISP's usually have their own DNS service, it's a giant hash table.

### What is HTTP
When we talk about the protocol for the WWW, we are usually referring to HTTP

Hypertext Transfer Protocol, it is the protocol that the web uses to break something down, transfer it, and then re-assemble it in another location.

Different from FTP  (files) to and from a computer to a server
Different from SMTP (email) for sending email

[Vsauce The Web Is Not The Internet](https://www.youtube.com/watch?v=scWj1BMRHUA)

### HTTP Codes  
HTTP protocol sends response codes every time we reach out for a web page.


**SUCCESS**  
200 - OK  
**300 REDIRECTION**  
301- Moved Permanently  
302- Temporary Redirect  
**Client Error**  
404- File Not Found  
**Server Error**  
500 - Internal Server Error  


### SSL (High Level) (Improve?)

443 port 

SSL stands for secure socket layer, and is a way that we can encrypt our HTTP protocol so that it is more difficult for crackers to get our information.

You need to get an SSL certificate in order to get this set up.

HTTPS is how we know that we are connected via SSL.

### Ports  
65,535 TCP Ports and another 65,535 UDP ports

A port can be thought of as a wall of sockets that connections can connect to, when we make a TCP connection, it will connect over a random port.

The internet is over port 80
FTP Is usually 21

### REST API  
Representational State transfer - It's way that we can model our back end applications.

Our request represents what we are trying to do

**Define**  
**GET** - Get a resource   
**POST** - Send something to the server (add a blog post)  
**PUT**- Replacing a resource in it's entirety  
**PATCH** - Updating a resource  
**DELETE** - Delete a resource
