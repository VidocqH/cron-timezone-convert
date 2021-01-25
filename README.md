# Change cron between timezones

## Usage

```python
convert(cron_expression, source_timezone, target_timezone)
```

```python
>> from crontzconvert import convert
>> convert('* 0/12 * * *', 'Asia/Shanghai', 'UTC')
'* 16/12 * * *'
```

### TODO

Change day and week when switch timezone
