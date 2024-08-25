from flask import Flask
from threading import Thread
import requests

app1 = Flask("server1")
app2 = Flask("server2")


def send_request_to_app2():
    requests.get("http://127.0.0.1:5000/test")
    return


@app1.route('/test')
def app1_test():
    print("server1 received request on /test, sending requests to server2...")
    threads = [Thread(target=send_request_to_app2) for _ in range(10)]
    for thread in threads:
        thread.start()
    for thread in threads:
        thread.join()
    return 'Request received on app1/test'


@app2.route('/test')
def hello_world():  # put application's code here
    return 'Request received on app2/test'


if __name__ == '__main__':
    app1_thread = Thread(target=app1.run, kwargs={"port": 4000})
    app1_thread.start()
    print("Server 1 is running...")
    app2_thread = Thread(target=app2.run, kwargs={"port": 5000})
    app2_thread.start()
    print("Server 2 is running...")
    app1_thread.join()
    print("Server 1 is stopped...")
    app2_thread.join()
    print("Server 2 is stopped...")
