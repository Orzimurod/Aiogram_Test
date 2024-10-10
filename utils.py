from contents import words

async def get_word(key, lang = 'uz'):
    word = words.get(key+ '-' + lang)
    return word