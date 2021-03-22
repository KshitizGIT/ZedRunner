# ZedRunner

Retrieves horse racing data by calling zed.run apis and store them to MySQL Database.


## Prerequisites
1. python
2. pipenv

## Installation

```bash
git clone https://github.com/KshitizGIT/ZedRunner.git
cd ZedRunner
pipenv install --deploy
```

## How to run ?

`zed.py` is the script to run to initiate the data fetch and storage scripts. This script takes two parameters: 
1. type:
   This is a required parameter. Available options are horse, race and stable
2. force:
   This is a optional parameter. Default value is False.
   
### Examples
```bash
pipenv run python zed.py --type horse
pipenv run python zed.py --type race --force True
pipenv run python zed.py --type stable
```
