# Jay 1
_I will rewrite this with images lateer_  
This was a matter of securing a tcp connection and conversing with the server.  
My first tcp connection was set to receive the basic 1024 bytes we learn in examples but that was not getting the entire intro message from the server.
 I used a function to receive from the socket until a "\n\n" is received ( a guess, and it worked). Since nothing in the first message is important it is dumped.  
The magic happens after I send a newline character. Then I again read from the socket until the "\n\n" character is found.  
What the server sends is a string representation of a large string of integers. To turn this string into an array of integers 
I first knocked the outer brackets (and a left over new line) off the string, split it at ", ", then created a new list 
of integers with pythons mapping function.   

*EDIT*  I just learned about `literal_eval()` when attempting jay2... use that to turn the string into a python array instead of what I did here.  

An algorithm for Max sub array is easy to find online, so I found one that had linear time and modified it to return a thruple.  
Sending a message back to the server consisting of the correct values gave me a flag.  

`nc chals3.umdctf.io 6001` returns  
```
██   ██ ███████ ██      ██████  
██   ██ ██      ██      ██   ██  
███████ █████   ██      ██████   
██   ██ ██      ██      ██       
██   ██ ███████ ███████ ██       

I've been stuck in this room for some time now. They locked me in here and told
me the only way I can leave is if I solve their problem within five seconds. 
I've tried so much, but my algorithm keeps going over the time. Can you help me?

What I have to do is find the maximum contiguous sub-array within this array of 
numbers. They keep telling me my algorithm isn't efficient enough! If you can 
send me the indices of this array, I might live to see another day.

Format: "sum, i, j" Example: 103, 345, 455

sum = the maximum contiguous sum
i = start index of sub-array
j = end index of sub-array

Press Enter to get the arr
```
Pressing enter then returns an extremely large list of integers.  
When executing `jay1.py` the result is:  
```
Response is: 9363, 4195, 13808 
Oh YES! I'm free! Here, a token of my appreciation:
UMDCTF-{K4d4n35_41g0r1thm}

```
Very rewarding flag.  

