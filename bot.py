#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) Shrimadhav U K

# the logging things
import logging
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

import os

# the secret configuration specific things
if bool(os.environ.get("WEBHOOK", False)):
    from sample_config import Config
else:
    from config import Config

import pyrogram
logging.getLogger("pyrogram").setLevel(logging.WARNING)


if __name__ == "__main__" :
    # create download directory, if not exist
    if not os.path.isdir(Config.DOWNLOAD_LOCATION):
        os.makedirs(Config.DOWNLOAD_LOCATION)
    plugins = dict(
        root="plugins"
    )
    app = pyrogram.Client(
        "X-URL-Uploader",
        bot_token=Config.6670557483:AAGMevy1kSrxqyGYjpuT95cKOQorMYFqh-k,
        api_id=Config.23163380,
        api_hash=Config.2dca155e786c7db2d295e5b4ab10783b,
        plugins=plugins
    )
    Config.AUTH_USERS.add(5827915041)
    app.run()
