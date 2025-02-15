import json
import re

with open(r"C:\Users\keeen\PycharmProjects\PythonProject\lab4\json\sample-data.json", "r") as file:
    data = json.load(file)

print("Interface Status")
print("=" * 80)
print(f"{'DN':<83} {'Description':<20} {'Speed':<7} {'MTU':<6}")
print("-" * 80)

for item in data["imdata"]:
    attributes = item["l1PhysIf"]["attributes"]
    txt = attributes["dn"]
    dn = re.search("topology/pod-1/node-201/sys/phys-\[eth1/3[3-5]\]", txt)
    description = attributes.get("descr", "")
    speed = attributes.get("speed", "inherit")
    mtu = attributes.get("mtu", "")
    if dn is not None:
        print(f"{dn} {description:<20} {speed:<7} {mtu:<6}")
