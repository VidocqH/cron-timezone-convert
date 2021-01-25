# Change cron between timezones

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
