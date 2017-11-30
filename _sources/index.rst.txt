.. pyflow documentation master file, created by
   sphinx-quickstart on Mon Nov 20 14:49:41 2017.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

MousePy
=======

MousePy's aim is to provide a simple abstraction layer for `Mouseflow's <https://api-docs.mouseflow.com/>`_ RESTful API.

For more information regarding Mouseflow's RESTful's implementation and how to configure the API keys, please refer to `Mouseflow's official documentation <http://help.mouseflow.com/help_center>`_.

.. toctree::
   :maxdepth: 2
   :caption: Contents:

   modules
   release
   contributing

Example
=======

List all available websites
------------------------------

.. code-block:: python

   connection = Mouseflow(
       user,
       token
   )

   list_of_websites = connection.websites().list()

Select a specific site
-------------------------

.. code-block:: python

   connection = Mouseflow(
       user,
       token
   )

   website = connection.websites("website name or id")

Credits
=======

`NEWCRAFT <https://www.newcraftgroup.com/>`_ empower companies to accelerate by using our craftsmanship. Our clients understand that new technology and new customer behavior create large-scale opportunities for growth. To compete with fast growing and agile disruptors, our clients are determined to capitalize their huge industry experience. NEWCRAFT help them grow faster with acceleration consultancy, digital marketing and data science.

In releasing this client API to the public, NEWCRAFT hopes to facilitate the Python community's work when implementing Mouseflow within their developement stack.

Our data science team helps you in the process of structuring databases, connecting APIs, and managing your digital management platform in order to unlock actionable insights. Other areas of expertise are product trend discovery, machine learning, IoT, and predictive analytics.

If you, or your business, need our help implementing or integrating technologies such as Mouseflow, contact us at info@newcraftgroup.com.

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
