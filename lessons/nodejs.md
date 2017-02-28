# NodeJS
- Explain what Node.js is & why it exists
- Explain what environment variables are and why they're useful
- Explain the event loop
- Explain what NVM is
- Explain what NPM is
- Modify the bash_profile to use a specific version of Node.js
- Explain node modules
- Explain how to include and use modules in a Node.js application
- Write a basic module that we can require
- Explain npm init & package.json
- Diving in with learnyounode


### What is nodeJS?
nodeJS is a wrapper that is built on top of google chromes v8 javascript runtime engine.

It allows us to do many things with javascript, anything that has to do with communicating with the computer

You can build utilities on your machine (mocha)
You can make network requests
You can work with the file system

global = window
process = document

``` Javascript
// Node hello world as a module
console.log('Hello, World!');
```

Explain module.exports
### What is the event loop?  
Javascript is an event driven language, it is a language designed to respond to behavior, because it was made for the web.

This works out well for the back end also, because it allows use to execute multiple things at once without stopping.

### What is NVM  
NVM stands for Node Version Manager, it allows us to manage our versions of node

###  Using different version of node

**In the .bash_profile:**

Let's install NVM with curl  
curl -o- https://raw.githubusercontent.com/creationix/nvm/v0.32.1/install.sh | bash

This will install NVM and add a line to our NVM file

Changing the version of node:  
`nvm alias default v4.3.2`

```
Usage:
nvm install <version>       Download and install a <version>
nvm use <version>           Modify PATH to use <version>
nvm ls                      List versions (installed versions are blue)
```

### What is NPM?  
- What is a package manager?
- Node Package Manager  
 npm is the package manager for the Node JavaScript platform.  It puts modules in place so that node can find the

 Most commonly, it is used to publish, discover, install, and develop node programs.

 ### Using modules  
 We fetch packages with NPM, now what?

```Javascript
var romanMD5 = require('romanmd5');
```


Let's write a basic module:
 ``` Javascript
 // Node hello world as a module
 module.exports = function(){
   console.log('Hello, World!');
 };
 ```

 ### NPM Init & The package.json file  
 We can use the `npm init` command to start a project with node.

 Show the package.json, and go through what it means.

 Go over --save
 `npm install --save`

**Main Activity**
### Diving in with learnyounode   
`npm install -g learnyounode`  
For a large portion of this class we will work with teams one each exercise, and then review them afterwards.

1. Split into groups
2. Install learnyounode
3. Let's work through first one together
4. After that, we will alot time  for each lesson, and then review them afterwards
