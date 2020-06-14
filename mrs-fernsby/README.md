Mrs. Fernsby
============
Check out this weird Ascii message we found earlier. We can't make heads or tails of it. Any idea what it says?

https://nostradamus.imfast.io/d8184e350cc288c4533ba1ceff32531b


Writeup
-------
This one was a simple binary-to-text encoding, like [basic-balloons]
and [money-money-money-money]. Unlike those two, however, [CyberChef]
wasn't able to pick out the encoding automatically.

I used Python to try to count the number of unique characters in the file:

```python
from collections import defaultdict

# Read in the data
with open('d8184e350cc288c4533ba1ceff32531b', 'r') as f:
    s = f.read()

# Count the number of each unique character
counts = defaultdict(int)
for c in s:
    counts[c] += 1

print(counts)
print(len(counts))
```

This told me that there were `82` unique characters in the file.
It's still pure ASCII data, so I thought it might just be something a bit
more obscure and I pulled up a [list of binary-to-text encodings](https://en.wikipedia.org/wiki/Binary-to-text_encoding#Encoding_standards)
on Wikipedia.

Going through that list, I decided to try ASCII85/Base85.
Decoding that in CyberChef gave me the correct answer:

```
"Will the future bring your wisdom to me?
Or will darkness rule the kingdom for all eternity?
You will live in my heart…
I will still remember even though we are apart.
I will feel you there for me
As I walk the road of life
You help me fight for what is right
I will honour thy name" ~ Nostradamus
CCC{This_1_is_not_a_funny_flag}
```

CyberChef recipe:
https://gchq.github.io/CyberChef/#recipe=From_Base85('!-u')&input=LCQvSnBDYG1oNUFLWVQtRkVNVjgrQ11BKkRKKCk7RGZwKENHQTIsL0RmJFY9RF1pbi41NzEyLCtFcU85Q2BtN3NFYmZRKEYpcklFRl9rVjNGRCw1LkNNQFshQThjPC1Bb0RdNEA7S2EmQVRWTChESj0zPDU3MVAzRldibUJDaHQ1MUJtKyYxQmw1JjFHcCRkM0A8LUpMSj5OWkYrRXFPOUNgbWVAQmwlVC5FYjAqIUQuNydzK0QjXy1EQk8lN0Rmb10rK0VxQj5APCxwJUA7b1hxRj1tbmwrRXFPOUNgbT4kQVNgSzdEZm0xRUJPdTNxK0QsUDQrRGtaczYkIi8/K0VxNzFDRVJfNEFLWiMzQDpVTCFBZnRvKEFuOzxQRGZtMTlBU2M8LkQuT2klQmtNKyQrRCxQNCtFcUwtRjxHOj0rRUQxL0JRT1NRK0VxTzlDYG1EMERKc1o8K0VWOkIrRHRWKUFLaTdHK0FRaXJGRTFmI0A7VS4uJDpAMEpIVzRabUYnZ1kvQmxkWCFEZmY%2BcD9ZNEZ1REwjVCRDZ2d0KQ

[CyberChef]: https://gchq.github.io/CyberChef/

[basic-balloons]: ../
[money-money-money-money].
