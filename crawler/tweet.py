import emoji


class Tweet():
    def __init__(self, text: str):
        self.text = text.lower()
        self.tags = self.find("@", forbidden="#")
        self.hashtags = self.find("#", forbidden="@")

    def find(self, prefix, forbidden):
        ret = []
        _text = self.text
        _text = _text.replace(forbidden, " ")

        if not _text.startswith("RT"):

            for word in _text.split(" "):
                word = self.remove_emojis(word)

                if len(word) >= 2 and word.count(prefix) == 1:
                    word = word.split(prefix)
                    word = prefix + word[len(word) - 1]
                    word = word.strip()

                    if word not in ret and len(word) >= 2 and word.startswith(prefix):
                        ret.append(word.lower())

        return ret

    def remove_emojis(self, s):
        return ''.join(c for c in s if c not in emoji.UNICODE_EMOJI['en'])
