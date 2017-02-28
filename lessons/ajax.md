# Ajax

**Write On Board**
- What is AJAX
- Synchronous VS Asynchronous
- AJAX VS Regular Requests
- What is Cross Origin Resource Sharing?
- What are the methods .ajax, $.get and $.getJSON?
- How to make a AJAX request
- What is a callback?
- Reviewing AJAX

**Round 1**
- Explain what AJAX is and what problem it solves
- Explain the difference between synchronous and asynchronous program execution.
- Explain the difference between an AJAX request and a synchronous request.
- Explain the need for CORS and how it enables secure requests to be made across domains
- Describe how the native XMLHttpRequest differs from the jQuery AJAX implementation

**Round 2**
- Explain what $.ajax is, and how it relates to methods such as $.get and $.getJSON.
- Use jQuery $.ajax to make an asynchronous GET request.
- Use jQuery $.ajax to make an asynchronous POST request.
- Provide a callback to capture an AJAX response when it's ready.
- Render HTML content using data loaded from an AJAX request.

**10 minute break**

**Round 3**
- Overview of AJAX
- End Activity

## Round 1
---
### What is AJAX?  
AJAX stands for "Asynchronous Javascript And XML"  

**Points:**
- Why the acronym (XML @ the end)
- What difference does AJAX make on the web?
- Quick overview of the WWW
- Draw a diagram of how AJAX works.

### Synchronous  VS Asynchronous
- Explain what Synchronous is
- Explain Asynchronous
- refer to diagram again

### AJAX VS Regular Requests
- Show an example of synchronous
- show an example of asynchronous on a webpage

### What is CORS?
CORS stands for 'Cross Origin Resource Sharing'  

- What is CORS?
- Explain why the WWW implements CORS

### Activity
You want to use AJAX to get content from another website and put it on your page.

Draw two boxes, with the word "browser" in one, and "server" in the other, draw out how an ajax request works on your desk with a partner, write out the steps of what is going on in this scenario.

## Round 2
---
### What is $.ajax, $.get  and $.getJSON?  
Let's write some AJAX!

Here's how it's done in vanilla:
``` Javascript
function loadDoc() {
  var xhttp = new XMLHttpRequest();
  xhttp.onreadystatechange = function() {
    if (this.readyState == 4 && this.status == 200) {
     document.getElementById("demo").innerHTML = this.responseText;
    }
  };
  xhttp.open("GET", "ajax_info.txt", true);
  xhttp.send();
}
```

How it's done w/ jQuery
``` Javascript
    var req = $.ajax({
      url: "url",
      method: 'GET'
  });

  req.done(function(res){
    // What's the AJAX response?
  });
  req.fail(function(err){
  // What's the AJAX error?
  });
```

W/ JSONP
```Javascript
function logResults(json){
  console.log(json);
}

$.ajax({
  url: "https://api.github.com/users/jeresig",
  dataType: "jsonp",
  jsonpCallback: "logResults"
});
```
- explain mandatory $.ajax parameters
- work through jQuery $.ajax doc page, explain capabilities
- explain JSON.stringify(), JSON.parse()

### Let's make a GET AJAX request  
- Diagram what an API is, and how GET works with this
- Explain the Hipster Jesus API, draw how HJAPI works on diagram

``` Javascript
$.getJSON('http://hipsterjesus.com/api/', function(data) {
     $('#content').html( data.text );
 });
```
- Render the result on the page w/ jQuery

### Explain the callback, what it's role is.
- Recall what a callback is
- Recall callbacks from previous lessons with arrays
- What's the role of callbacks in AJAX?
- Relate the callbacks

### Rendering the HTML to our page (Showing what we asked for)
- Show how code inside the callback showed what's on the page
- Draw or refer to a/the diagram of AJAX, and augment it with how the view is generated.


### Activity   
Let's stringify this 'user' object, and the paste it into, a JSON file.  

``` Javascript
var user = {
  firstName: 'John',
  lastName: 'Wilks Booth',
  profileImage: 'url',
  aboutMe: 'I\'m a wheelin\' dealin\' sun of a gun'
};

var jsonUser = JSON.stringify(user);

console.log(jsonUser);
```

Make a request to this file using AJAX and load something onto the page, you can use your existing code and modify it if you need to.


## Round 3
---
## Overview of AJAX
- How AJAX works
- Step by step our code, what is it doing?
- Q & A


### Activity (25 min)  
Taking everything we learned, let's make an HTML page with multiple boxes and in each of these boxes let's put some content from ajax.

For text we can use  
http://hipsterjesus.com/api/

Information:  
http://hipsterjesus.com


For images we can use  
http://www.splashbase.co/api/v1/images/random  

Information:  
http://www.splashbase.co/api
