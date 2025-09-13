def getSongInfo(input: str):
    input = input.lower()
    artist, song = None, None

    if "play" in input and "by" in input and "songs" not in input:
        start = input.find("play") + len("play")
        end = input.find("by")
        song = input[start:end].strip()
        artist = input[end + len("by"):].strip()

        if "on" in artist:
            artist = artist[:artist.find("on")].strip()
        
    elif "play" in input and "songs" not in input:
        start = input.find("play") + len("play")
        end = input.find("on")
        song = input[start:end].strip()

    elif "by" in input and "songs" in input:
        start = input.find("by")
        artist = input[start + len("by"):].strip()

        if "on" in artist:
            artist = artist[:artist.find("on")].strip()
        
    
    return song,artist
