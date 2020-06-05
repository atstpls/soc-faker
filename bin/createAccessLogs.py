from socfaker import SocFaker
import sys

path_file = sys.argv[1]
clients = int(sys.argv[2])

sf = SocFaker()

count=0
while count < 10:
    logs = sf.logs.access(type='test', path_file=path_file, clients=clients)

    with open("/app/logs/access.log", "a") as f:
        for line in logs:
            f.write(line + "\n")
    count += 1

