from datetime import timedelta, time

def get_time(timedelta:timedelta):
    """
        тут не понял как достать из timedelta time вроде как timedelta.time но нет
        я искал, честно :)
    """
    
    hours, remainder = divmod(timedelta.total_seconds(), 3600)
    minutes, seconds = divmod(remainder, 60)
    return time(int(hours), int(minutes), int(seconds))

