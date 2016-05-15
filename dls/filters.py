from dls import app
from datetime import datetime


@app.template_filter('datetime')
def filter_datetime(date):
    return date.strftime('%d %b, %I:%M %p')


@app.template_filter('timeago')
def filter_timeago(time):
    timedelta = datetime.now() - time
    secs = timedelta.total_seconds()
    fmt = '%d %s ago'
    if secs < 60:
        return fmt % (secs, 'secs')
    secs /= 60
    if secs < 60:
        return fmt % (secs, 'mins')
    secs /= 60
    if secs <= 24:
        return fmt % (secs, 'hrs')
    else:
        return '%dd %dh ago' % (int(secs / 24), int(secs % 24))
