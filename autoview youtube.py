import webbrowser, time
url = input("Enter Url: ")
duration = input("Enter Time: ")
while True:
    webbrowser.open_new(url)
    time.sleep(int(duration))

