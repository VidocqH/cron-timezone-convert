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

### Why I do this?

I find the cron of Github actions is at the UTC timezone and I have a lot of actions need to maintain their start time. So I write this.

It can only change hour now. Need to fix.
