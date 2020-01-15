example_jsonld
==============

Note: Repo name is kind of a misnomer
 
An example repo demonstrating usage of json-ld to 
link files, data, and metadata into a cohesive 
narrative. 

I am also using this repo to test out pip-as-binary-management, 
in other words, using `pip` with `git-lfs` for 
versioning and distributing big ML models. 

Versions are just git tags. 

The ultimate game plan of this scheme is to use git/pip to manage files 
and versions, and have git-hooks or some cli tool in order to manage the metadata
in .json files. Indexing and searching would be performed completely
offline. No server, no provisioning, no fuss.  

`example_jsonld/data/model.bin` is my stand-in for some big binary
blob of data. `*.bin` is tracked by `lfs`. Instead of binary, I
just have some text, the contents of which represent different
versions of this model. Eventually I'll get some actual PoC 
in here. 

Example install and run
__________________________________
  
.. code-block:: bash

    $ VERSION=v0.0.6
    $ pip install pip install “git+git://github.com/xkortex/example_jsonld.git@$VERSION”
    $ python -c "import example_jsonld.data_paths"


Out:
--------

.. code-block::

    The contents of your model:
    this is model-0.0.6


Testing Automated Metadata Scraping
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

I am experimenting with using :code:`.rst` as a savvy and easy way to point to
project files, models, metadata, and the like. By using this snippet of code, this
file can be compiled to xml:

.. code-block::

    infile = 'README.rst'
    ofile = 'docs/_build/readme.xml'
    docutils.core.publish_file(source_path=path, destination_path=ofile, writer_name='xml')

Some parameters:

:foo: bar

:data_dir: ./data

This will include the raw contents of the file
................................................

.. include:: data/meta.txt



