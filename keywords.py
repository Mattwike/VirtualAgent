import secrets

name = 'jarvis'

class input:
    killswitch = 'turn off'
    activation = 'turn on'
    playSong = 'play'
    second = 'iphone'
    main = 'main device'
    secondary = 'secondary device'
    second = 'secondary device'
    news = "get the news"
    primaryDevice = 'unknown'
    secondayDevice = 'unknown'
    phone = 'phone'
    pc = 'computer'
    set = 'set'
    inquiry = 'tell me more '
    

class output:
    startup = 'hello Matthew, How can I assist you today'
    playSong= "now playing "
    onComputer = " on your computer"
    onPhone = "on your iphone"
    pc = secrets.keys.pc
    phone = secrets.keys.phone
    articles = []