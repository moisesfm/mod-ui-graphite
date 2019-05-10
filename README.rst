Alignak WebUI Graphite Module
=============================

** To be rewritten**

*Alignak WebUI module for the Alignak broker*

.. image:: https://badge.fury.io/py/alignak_module_glpi.svg
    :target: https://badge.fury.io/py/alignak-module-nsca
    :alt: Most recent PyPi version

.. image:: https://img.shields.io/badge/License-AGPL%20v3-blue.svg
    :target: http://www.gnu.org/licenses/agpl-3.0
    :alt: License AGPL v3

Installation
------------

The installation of this module will copy some configuration files in the Alignak default configuration directory (eg. */usr/local/share/alignak*). The copied files are located in the default sub-directory used for the modules (eg. *arbiter/modules*).

From PyPI
~~~~~~~~~
To install the module from PyPI::

    sudo pip install alignak-module-ui-graphite


From source files
~~~~~~~~~~~~~~~~~
To install the module from the source files (for developing purpose)::

    git clone https://github.com/mohierf/mod-ui-graphite
    cd mod-ui-graphite
    sudo pip install . -e

**Note:** *using `sudo python setup.py install` will not correctly manage the package configuration files! The recommended way is really to use `pip`;)*


Short description
-----------------

This module for Alignak UI allows to view the Graphite views in the Web UI.


Bugs, issues and contributing
-----------------------------

Contributions to this project are welcome and encouraged ... `issues in the project repository <https://github.com/mohierf/mod-ui-graphite/issues>`_ are the common way to raise an information.
