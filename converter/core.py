# Developed for Anunzio International by Anzul Aqeel. Contact +971545822608 or +971585515742. Linkedin Profile: linkedin.com/in/anzulaqeel

from datetime import datetime
import dateutil.parser # Might be an external dep? 
# "Dependencies: Primarily standard Python libraries for a zero-dependency approach unless necessary."
# Let's rely on standard datetime.strptime with common formats or basic trying.

class DateConverter:
    COMMON_FORMATS = [
        "%Y-%m-%d",           # 2024-12-25
        "%Y/%m/%d",           # 2024/12/25
        "%d-%m-%Y",           # 25-12-2024
        "%d/%m/%Y",           # 25/12/2024
        "%m/%d/%Y",           # 12/25/2024
        "%Y-%m-%d %H:%M:%S",  # 2024-12-25 10:00:00
        "%Y-%m-%dT%H:%M:%S",  # ISO 8601
        "%d %b %Y",           # 25 Dec 2024
        "%b %d, %Y",          # Dec 25, 2024
    ]

    @staticmethod
    def convert(date_str, target_format="%Y-%m-%d"):
        date_str = date_str.strip()
        
        # Try finding a matching format
        dt = None
        for fmt in DateConverter.COMMON_FORMATS:
            try:
                dt = datetime.strptime(date_str, fmt)
                break
            except ValueError:
                continue
        
        # Fallback: ISO format often includes timezone ("+00:00") or milliseconds (".000") which simple strptime might miss
        # if string ends with Z, replace with +0000
        if dt is None:
             try:
                 dt = datetime.fromisoformat(date_str.replace('Z', '+00:00'))
             except ValueError:
                 pass

        if dt:
            return dt.strftime(target_format), None
        
        return None, "Unable to detect source format. Please ensure it is a common format (ISO, YMD, DMY)."

# Developed for Anunzio International by Anzul Aqeel. Contact +971545822608 or +971585515742. Linkedin Profile: linkedin.com/in/anzulaqeel
