#!/usr/bin/python

host_path = r"C:\Windows\System32\drivers\etc\hosts"
redirect = "127.0.0.1"


def is_blocked_time(block_start, block_end):
	"Checks if the current time is in the blocked interval"
