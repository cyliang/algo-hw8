# vim: set syntax=python filetype=python:

import msgpack

with open("../input.txt", "wb") as output_file:
	msgpack.pack(1, output_file)
	msgpack.pack(4, output_file)
	msgpack.pack([0, 1, 1, 2], output_file)
