from subprocess import Popen, PIPE

hosts = [
    'www.cyber.org.il',
    'www.ynet.co.il',
    'www.google.com',
    'www.yahoo.com',
    'www.gggggg.com'
]

def no_threads():
    for host in hosts:

        process = Popen(['ping', '-c', '1', host], stdout=PIPE) # -c becuase I am on unix
        print(process.stdout.read().decode())

start1 = time.time()
no_threads()
end1 = time.time()
time1 = end1 - start1


def with_threads():
    pass