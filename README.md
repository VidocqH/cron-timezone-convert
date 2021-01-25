# Change cron between timezones

[![Build Status](https://travis-ci.com/VidocqH/cron-timezone-convert.svg?branch=main)](https://travis-ci.com/VidocqH/cron-timezone-convert)  ![GitHub](https://img.shields.io/github/license/vidocqh/cron-timezone-convert?label=license) [![](https://img.shields.io/badge/python-3.6+-blue.svg)](https://www.python.org/downloads/) 

Gives a crontab expression, source and target timezones, return a new crontab expression that times change according to the given timezones.

## Install
```bash
pip3 install crontzconvert
```

## Usage

```python
convert(cron_expression, source_timezone, target_timezone)
```

```python
>> from crontzconvert import convert
>> convert('* 0/12 * * *', 'Asia/Shanghai', 'UTC') # UTC+8 to UTC
'* 16/12 * * *'
```

### TODO

Change day and week when switch timezone
