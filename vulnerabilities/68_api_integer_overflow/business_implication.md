
- An integer overflow during a buffer length calculation can result in allocating a buffer that
is too small to hold the data to be copied into it. This in turn can cause a buffer overflow when the data is copied.
- Withdrawing 1 unit from an account with a balance of 0 could cause an integer underflow and yield
a new balance of 4,294,967,295.
- A very large positive number in a transaction could be cast as a signed integer by backend. The interpreted value
could become a negative number and reverse the direction of the transaction.
