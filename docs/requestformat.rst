.. _requestformat:

Format of requests and responses
================================

Suppose we have the following models::

    from flask.ext.restless import Entity
    from elixir import Date, DateTime, Field, Unicode
    from elixir import ManyToOne, OneToMany

    class Person(Entity):
        name = Field(Unicode, unique=True)
        birth_date = Field(Date)
        computers = OneToMany('Computer')

    class Computer(flask.ext.restless.Entity):
        name = Field(Unicode, unique=True)
        vendor = Field(Unicode)
        owner = ManyToOne('Person')
        purchase_time = Field(DateTime)

Also suppose we have registered an API for these models at ``/api/person`` and
``/api/computer``, respectively.

.. note::

   For all requests that would return a list of results, the top-level JSON
   object is a mapping from ``"objects"`` to the list. JSON lists are not sent
   as top-level objects for security reasons. For more information, see `this
   <http://flask.pocoo.org/docs/security/#json-security>`_.

.. http:get:: /api/person

   Gets a list of all ``Person`` objects.

   **Sample response**:

   .. sourcecode:: http

       HTTP/1.1 200 OK

       {"objects": [{"id": 1, "name": "Jeffrey", "age": 24}, ...]}

.. http:get:: /api/person?q=<searchjson>

   Gets a list of all ``Person`` objects which meet the criteria of the
   specified search. For more information on the format of the value of the
   ``q`` object, see :ref:`searchformat`.

   **Sample response**:

   .. sourcecode:: http

      HTTP/1.1 200 OK

      {"objects": [{"id": 1, "name": "Jeffrey", "age": 24}, ...]}

   If the value of the ``q`` parameter indicates that a function should be
   evaluated on the matched instances instead, the response would look like
   this:

   .. sourcecode:: http

      HTTP/1.1 200 OK

      {"sum__age": 135, "avg__age": 25.5, ...}

.. http:get:: /api/person/(int:id)

   Gets a single instance of ``Person`` with the specified ID.

   **Sample response**:

   .. sourcecode:: http

      HTTP/1.1 200 OK

      {"id": 1, "name": "Jeffrey", "age": 24}

.. http:delete:: /api/person/(int:id)

   Deletes the instance of ``Person`` with the specified ID.

   **Sample response**:

   .. sourcecode:: http

      HTTP/1.1 204 No Content

.. http:post:: /api/person

   Creates a new person with initial attributes specified as a JSON string in
   the body of the request.

   **Sample request**:

   .. sourcecode:: http

      POST /api/person HTTP/1.1
      Host: example.com

      {"name": "Jeffrey", "age": 24}

   **Sample response**:

   .. sourcecode:: http

      HTTP/1.1 201 Created

      {"id": 1}

.. http:patch:: /api/person/(int:id)
.. http:put:: /api/person/(int:id)

   Sets specified attributes on the instance of ``Person`` with the specified
   ID number. :http:put:`/api/person/1` is an alias for
   :http:patch:`/api/person/1`, because the latter is more semantically correct
   but the former is part of the core HTTP standard.

   **Sample request**:

   .. sourcecode:: http

      PATCH /api/person/1 HTTP/1.1
      Host: example.com

      {"name": "Foobar"}

   **Sample response**:

   .. sourcecode:: http

      HTTP/1.1 201 Created

      {"id": 1, "name": "Foobar", "age": 24}

Error messages
--------------

Most errors return :http:statuscode:`400`. A bad request, for example, will
receive a response like this:

.. sourcecode:: http

   HTTP/1.1 400 Bad Request

   {"message": "Unable to decode data"}