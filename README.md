# Simulated L2 Network

Sample Nested Network Blockchain

# Add 

Syntax: `/add`

Create a Length of the Layer-1 Network with blocks made up of a nested blockchain.

The command prompts a the user to type a number for their desired length.


# Add Value

Syntax: `/add_val val [block-idx]`

Adds a value `val` to the network located at the block of the L1 network at `block-idx`. This almost works like a nested LinkedList with O(n^2), where `n` is the length of the chain. 

It should be noted that both the layer 1 and 2 networks are parallel in terms of size.


# Print a Specified Value

Syntax: `/view [block-idx]`

Prints the network of a specified network located at `block-idx` of the L1 network.

The run-time of this process is `O(n^2)`, where `n` is the length of the L1 or L2 chain (as they are the same).

# More Information

Both Networks use Proof of Work, making it almost unscalable using the same protocol, which is a downside.

Made in Python.
