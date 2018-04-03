- Install python3 on MAC and virtual env
``` 
brew install python3
brew postinstall python3
pip3 install --user --upgrade pip
pip3 install --user --upgrade virtualenv
virtualenv -p `which python3` path_to_env
``` 
- for mac and python-3.6.4_2
```
virtualenv -p /usr/local/Cellar/python3/3.6.4_2/bin/python3 path_to_env
```
- Activate env
``` 
source ./env/bin/activate
``` 
- Install other dependencies
``` 
pip3 install --upgrade dependency
``` 
