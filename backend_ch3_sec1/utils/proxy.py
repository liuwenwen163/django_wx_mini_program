# encoding: utf-8
import backend.settings

__author__ = "bbw"


def proxy():
    if backend.settings.USE_PROXY:
        # add your proxy here
        return {}
    else:
        return {}
