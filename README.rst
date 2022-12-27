conda-recipes
=============

Collection of recipes for the Conda package manager


Build command
-------------

Examples::

  $ conda build --output-folder out --python X.Y package-path/
  $ conda build -c conda-forge --output-folder out --python X.Y package-path/


Upload
------

Examples::

  $ anaconda upload out/noarch/packagename-x.y.z.tar.bz2
  $ anaconda upload -u username out/noarch/packagename-x.y.z.tar.bz2


Clean
-----

Examples::

  $ conda build purge
