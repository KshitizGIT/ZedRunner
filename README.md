# ZedRunner

Retrieves horse racing data by calling zed.run apis and store them to MySQL Database.


## Prerequisites
1. python
2. pipenv
3. MySQL with full unicode support

## Installation

```bash
git clone https://github.com/KshitizGIT/ZedRunner.git
cd ZedRunner
pipenv install --deploy
```
Also, you will need to run the scripts located inside the `migrations` folder to a MySQL database.

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

## Configuration

Check the `config.py` file. This contains all the configuration for database and telegram bot settings.
```python 
Database = {
'host': 'localhost',
'user': 'zedrunner',
'password': '#ZedRunner@2021',
'database': 'zed'
}
 
BOT = {
   'token': '1793290514:AAFjFd95hzTxOb-lxN1ymc3vV7uBcUlJ-Xc' ,
   'channel': '@zed_channel_test'
}
API_RETRY_COUNT = 3

```
