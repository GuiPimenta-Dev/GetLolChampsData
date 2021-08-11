import datetime
import time
import random
from .base_bot import BaseBot
from pages.facebook import FacebookPage
import queue


class FacebookBot(BaseBot):
    def __init__(self):
        self.page = FacebookPage()

    def run(self, args, out_queue: queue):
        email = args['email']
        password = args['password']
        codes = args['codes']

        try:
            self.page.login(email=email, password=password, codes=codes)
            status = self.page.comment()
        except Exception:
            status = "FAILED"


        data = {
            'email': email,
            'status': status,
            'date': datetime.datetime.now().strftime("%m/%d/%Y %H:%M:%S")
        }

        self.page.close()

        out_queue.put(data)
