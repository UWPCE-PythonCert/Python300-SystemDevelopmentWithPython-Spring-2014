import json

obj = {"key": "value"}
obj2 = {"key": obj}
obj["key"] = obj2

print obj["key"]
print obj2["key"]

print json.dumps(obj2)
