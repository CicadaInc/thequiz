from PodSixNet.Channel import Channel


class ClientChannel(Channel):
    def Network(self, data):
        print(data)

    def Network_myaction(self, data):
        print("myaction:", data)
