import multiprocessing as mp
import os
from typing import *

import jieba

jieba.initialize()


class Executor(object):
    def __init__(self, n_proc=os.cpu_count()):
        self._mp = mp.get_context('fork')

        self._pool = self._mp.Pool(n_proc)
        self._queue = self._mp.Queue()

    def split(self, lines: Iterable[str]):
        for it in self._pool.imap(self._do_split, lines):
            yield it

    @staticmethod
    def _do_split(line: str):
        return jieba.lcut(line)

    def finish(self):
        self._pool.close()
        self._pool.join()
