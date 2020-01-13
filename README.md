# example_jsonld
##### Repo name is kind of a misnomer
 
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

  
```
$ VERSION=v0.0.6
$ pip install pip install “git+git://github.com/xkortex/example_jsonld.git@$VERSION”
$ python -c "import example_jsonld.data_paths"
```
Out:
```
The contents of your model:
this is model0.0.6
```
