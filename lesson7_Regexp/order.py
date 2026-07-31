import re


def is_valid_order_id(order_id):
    return bool(re.search("^ORD-...", order_id))

print(is_valid_order_id("ORD-12345"))
print(is_valid_order_id("ORD-123456"))
print(is_valid_order_id("ORD-1234567"))