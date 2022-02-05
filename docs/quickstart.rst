Quickstart
==========


Firstly, we will begin from installing SBL.py:

Installing
-----------

.. code-block:: sh

    pip install SBL.py -U


Then we will create a Client

Making a Client
----------------

.. code-block:: python3

    from sblpy import SBLApiClient

    SblClient = SBLApiClient(bot, "YOUR SBL API TOKEN HERE") # Your dpy bot

Then we will make error handler

Making Error Handler
--------------------

.. code-block:: python3

    @SblClient.on_error
    async def on_sbl_err(error):
      print(error)

Then we will post stats

Posting stats
---------------

.. code-block:: python3

    SblClient.postBotStats()

You can also use our inbuilt AutoPoster handler cog fot this too

Inbuilt AutoPoster Cog
------------------------

.. code-block:: python3

    from sblpy import SBLCog

    SBLCog.setup(
        bot, # your dpy bot
        "YOUR AUTH TOKEN HERE" # your SBL Api auth token
    )

Then we will get bot likes

Getting likes
---------------

.. code-block:: python3

    print(bot.SBLClient.getBotLikes())


Like Webhook System
--------------------

This means when someone likes for bot, we will get notified

First set environment variable

.. code-block:: python3

    import os

    os.environ["SBL_HOOK_TOKEN"] = "BOT'S SBL AUTHORIZATION TOKEN"

The if you use Flask

.. code-block:: python3

    from sblpy.webhook.flask import flask_webhook

    myapp.register_blueprint(flask_webhook, url_prefix="/sbl")

.. note::
   The passed parameter ``url_prefix`` is the path where the notification hooks should recieve

or if you use Quart

.. code-block:: python3

    from sblpy.webhook.quart import quart_webhook

    myapp.register_blueprint(quart_webhook, url_prefix="/sbl")

or if you use nothing then

.. code-block:: python3

    from sblpy.webhook import flask

    flask.run(in_thread=True,debug=True)
