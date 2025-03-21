import requests
import os


class Discord:
    def __init__(self):
        self.channels = []

    def add_channel(self, channel):
        self.channels.append(channel)
        return self

    def notify_all(self, message):
        data = {"content": message}
        for channel in self.channels:
            requests.post(channel, json=data)
