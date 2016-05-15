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


@app.template_filter('filesize')
def filter_filesize(size_bytes):
    sz = size_bytes
    fmt = '%d %s'
    if sz < 1024:
        return fmt % (sz, 'B')
    sz /= 1024
    if sz < 1024:
        return fmt % (sz, 'KB')
    sz /= 1024
    return fmt % (sz, 'MB')


@app.template_filter('timerange')
def filter_str_timerange(secs):
    if secs > 3600:
        return '%dh %dm' % (secs / 3600, (secs % 3600) / 60)
    elif secs > 60:
        return '%dm %ds' % (secs / 60, secs % 60)
    else:
        return '%ds' % secs
