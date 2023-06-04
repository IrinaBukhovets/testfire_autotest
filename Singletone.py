class Singletone(type):

    _instance = {}

    def __call__(self, *args, **kwargs):
        if self not in self._instance:
            self._instance[self] = super(Singletone, self).__call__(*args, **kwargs)
        return self._instance[self]