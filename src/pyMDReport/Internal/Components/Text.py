from pyMDReport.Internal.Components.pyMDComponent import pyMDComponent

from pyMDReport.Internal.ComponentTypes import ComponentType

from pyMDReport.Internal.types import Group, Text

class Text(pyMDComponent):

    _text : str
    _outText : str

    def __init__( self,
            parent : Group | None = None, 
            identifier : str | None = None,
            text: str | None = None,
            bold : bool = False,
            italic: bool = False,
            strike: bool = False,
            sub: bool = False,
            sup: bool = False,
            underlined : bool = False,
        ):

        super().__init__(
            parent = parent, 
            identifier = identifier,
        )

        if strike:
            text = f"~~{text}~~"

        if bold and italic:
            text = f"***{text}***"
        elif bold:
            text = f"**{text}**"
        elif italic:
            text = f"_{text}_"

        if sub:
            text = f"<sub>{text}</sub>"

        if sup:
            text = f"<sup>{text}</sup>"

        if underlined:
            text = f"<ins>{text}</ins>"

        self._text = text
        self._outText = text
        
        self._type = ComponentType.text

    def Md( self ) -> str:

        md = self.BaseMd()

        return md + self._outText
    
    def Format( self, *args, **kwargs ):

        self._outText = self._text.format(*args, **kwargs)

    def __add__( self,
            other: Text
        ) -> Text:

        sep = " "

        txt = Text(
            parent = None, 
            identifier = self._identifier, 
            text = self._text + sep + other._text,
        )

        txt._outText = self._outText + sep + other._outText
        txt._parent = self._parent

        txt._anchor = self._anchor

        if txt._parent:
            txt._parent.Update(txt._identifier, txt)

        return txt