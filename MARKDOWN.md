I first defined the URL to be used since that is required for the API to have something to work with.
I opted for a direct insertion of a key into line 5, because that meant I didn't need another variable
to serve as the key holder. Only the key was included within "params =" because although my research 
materials had other fields, I wanted to keep my implementation minimal so I only put the key in there. 
Some minimal status code error handling was included because that was covered in another course I'm 
taking, and it seemed like good practice for error handling based on the material. I then created the 
dataframe with the returned data, opting to only include a few columns in the final dataframe because 
my IDE's terminal just shows "..." between columns if there's too many of those.

UPDATE: I forgot to mention that the API I'm using for this assignment is the NYT Books API.