from server import run


def changed(url):               # Activates when a new url is opened
    print(f"Main: {url}")

if __name__ == '__main__':
    try:
        run()               # Runs the main server.
    except KeyboardInterrupt:
        pass