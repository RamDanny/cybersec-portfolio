Challenge Link: [Cookies](https://play.picoctf.org/practice/challenge/173)

Run the challenge website. The site contains a search bar. If the autocomplete prompt is entered, it shows us a message "I love <search-term>".
Using any other query results in no valid messages being displayed. Nothing useful seems to be revealed from the source code.

But upon inspecting the successful autocomplete prompt, it is visible that: submitting the form leads to the `.../check` URL.
And inspecting the cookie field of the response, the unsuccessful attempt has a value of -1, while a successful attempt has a non-negative value (0 in this case).

Thus, custom packets are sent to the `.../check` URL, changing the cookie field each time.
This is done using Burpsuite Intruder, which enumerates over the cookie field, substituting values from 0 and onward.
At a value of 18, the match occurs and the flag is displayed in the response packet.
