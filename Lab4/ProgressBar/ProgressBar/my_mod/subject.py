class Subject:
    def __init__(self):
        self.__obs_list = []

    def add__observer(self, obs):
        self.__obs_list.append(obs)

    def notify(self, *args, **kwargs):
        for obs in self.__obs_list:
            obs.upade(*args, **kwargs)
