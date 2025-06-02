import requests


class Discord:
    def __init__(self):
        self.channels = []

    def add_channel(self, channel):
        self.channels.append(channel)
        return self

    def notify_all(self, message):
        data = {"content": message}
        for channel in self.channels:
            try:
                response = requests.post(channel, json=data)
                response.raise_for_status()
            except requests.exceptions.RequestException as e:
                print(f"Failed to send Discord notification: {e}")
