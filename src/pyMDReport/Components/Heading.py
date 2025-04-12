class HeadingLevel:
    h1 = 1
    h2 = 2
    h3 = 3

class Heading:

    def __init__(
            self,
            text: str,
            headingLevel: HeadingLevel | int = HeadingLevel.h1,
        ):

        self.text = text
        self.headingLevel = headingLevel

    

    def MdRows():
        pass
        