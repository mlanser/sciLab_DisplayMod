from abc import ABC, abstractmethod


class _DisplayBase(ABC):
    def __init__(self, resX, resY, colors, displType):
        self._resX = resX
        self._resY = resY
        self._colors = colors
        self._type = displType

    def __str__(self):
        return '{}:{}x{}x{}'.format(self._type, self._resX, self._resY, self._colors)

    def __repr__(self):
        return "TYPE: '{}' - RES: w{}x h{} x {}bit".format(self._type, self._resX, self._resY, self._colors)

    @property
    def colors(self):
        return self._colors

    @property
    def type(self):
        return self._type

    @property
    def resolution(self):
        return self._resX, self._resY

    @staticmethod
    def _parse_attribs(attribs, key, default=None):
        if attribs is None:
            return default

        return attribs.get(key, default)

    @abstractmethod
    def clear(self, attribs=None):
        pass

    @abstractmethod
    def display_msg(self, msg='', attribs=None):
        pass

    @abstractmethod
    def display_table(self, data=None, columns=None, attribs=None):
        pass

    @abstractmethod
    def display_status(self, tasks=None, msg=None):
        pass

    @abstractmethod
    def display_log(self, data):
        pass

    @abstractmethod
    def display_progress(self, data):
        pass
