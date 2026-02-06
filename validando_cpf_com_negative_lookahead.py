# coding=utf8
# the above tag defines encoding for this document and is for Python 2.x compatibility

import re

regex = re.compile(
    r"^(?!(\d)\1{2}\.\1{3}\.\1{3}-\1{2})(\d{3}\.\d{3}\.\d{3}-\d{2})$",
    flags=re.M,
    )

test_str = (
    "822.877.860-07\n"
	"694.255.450-22\n"
	"209.541.150-15\n"
	"082.405.020-75\n"
	"289.236.250-43\n"
	"506.257.950-32\n"
	"806.737.290-01\n"
	"066.901.210-62\n"
	"941.564.050-28\n"
	"049.726.020-40\n"
	"534.171.700-79\n"
    "111.111.111-11\n"
	"616.361.030-06")

print(regex.findall(test_str))