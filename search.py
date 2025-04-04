import yt_dlp

def getUrl(query):
    ydl_opts = {"quiet": True, "default_search": "ytsearch1"}
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        result = ydl.extract_info(query, download=False)
        if "entries" in result:
            return [
                {
                    "title": entry.get("title"),
                    "url": entry.get("webpage_url"),
                    "views": entry.get("view_count"),
                    "duration": entry.get("duration"),
                }
                for entry in result["entries"]
            ]
    return []

