from datetime import datetime, timezone, timedelta

TURKEY_TZ = timezone(timedelta(hours=3))


def to_turkey_time(ts: datetime) -> datetime:
    # Eğer timezone yoksa, UTC olarak kabul et (güvenli varsayım)
    if ts.tzinfo is None:
        ts = datetime(ts.year, ts.month, ts.day, ts.hour, ts.minute, ts.second, tzinfo=timezone.utc)

    # Türkiye saatine çevir
    return ts.astimezone(TURKEY_TZ)