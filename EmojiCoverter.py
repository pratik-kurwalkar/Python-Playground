# Emoji Converter

msg = input('> ')
print('In Emoji Converter')

def make_emoji(msg):
    emojis = {
        ':)': '😁',
        'lol': '😂',
        ':(': '😔'
    }
    list = msg.split(' ')  # Splits the parts of string when provided char encountered and returns list
    # print(list)
    for i in list:
        if i in emojis.keys():
            msg = msg.replace(i, emojis.get(i))  # replace method does not modify original string, but returns modified string
    else:
        return msg

print(make_emoji(msg))
