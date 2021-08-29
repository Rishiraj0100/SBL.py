Quickstart
==========


Firstly, we will begin from installing SBL.py:

Installing
-----------

.. code-block:: sh

    pip install -U git+https://github.com/Rishiraj0100/SBL.py.git


Then we will create a Client

Making a Client
----------------

.. code-block:: python3

    from sblpy import SBLApiClient

    SblClient = SBLApiClient(bot, "YOUR SBL API TOKEN HERE") # Your dpy bot

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

    print(SblClient.getBotLikes())



What if You are discord-list.cf User
then you can simply change the URL

Sync for discord-list.cf
-------------------------

.. code-block:: python3

    import sblpy

    sblpy.http.Route.BASE = "https://discord-list.cf/api/auth"

