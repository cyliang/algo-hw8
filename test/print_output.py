# vim: set syntax=python filetype=python:

import msgpack

with open("../output.txt", "rb") as input_file:
	inPack = msgpack.Unpacker(input_file, use_list = True)

	for unpacked in inPack:
		print unpacked
