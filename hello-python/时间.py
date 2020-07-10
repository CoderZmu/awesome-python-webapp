from datetime import datetime, timedelta, timezone
import re

def to_timestamp(dt_str, tz_str):
  tz_hour = re.match(r'UTC([\+\-]\d{1,2}):\d{2}', tz_str).group(1)
  tz = timezone(timedelta(hours=int(tz_hour)))
  dt = datetime.strptime(dt_str, '%Y-%m-%d %H:%M:%S')
  dt = dt.replace(tzinfo=tz)
  return dt.timestamp()


to_timestamp('2015-6-1 08:10:30', 'UTC+7:00')