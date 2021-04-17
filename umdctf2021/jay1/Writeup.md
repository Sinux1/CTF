# Jay 1
_I will rewrite this with images lateer_  
This was a matter of securing a tcp connection and conversing with the server.  
My first tcp connection was receiving the basic 1024 we learn in examples but that was not getting the entire intro message from the server.
 I used a function to receive from the socket until a sentary is received. Since nothing in the first message is important it is dumped.  
The magic happems after I send a newline character. Then I again read from the socket until the sentary character is found.  
What the server sends is a string representation of a large string of integers. To turn this string into an array of integers 
I first knocked the outer brackets (and a left over new line) off the string, split it at ", ", then created a new list 
of integers with pythons mapping function.   
An algorithm for Max sub array is easy to find online, so I found one that had linear time and modified it to return a thruple.  
Sending a message back to the server consisting of the correct values gave me a flag.  
