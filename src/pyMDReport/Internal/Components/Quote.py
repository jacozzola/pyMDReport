from pyMDReport.Internal.Components.Text import Text

from pyMDReport.Internal.ComponentTypes import ComponentType

from pyMDReport.Internal.types import Group, Quote

class Quote(Text):

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
            text = text, 
            bold = bold, 
            italic = italic, 
            strike = strike, 
            sub = sub, 
            sup = sup, 
            underlined = underlined,
        )

        self._type = ComponentType.quote
        
    def Md( self ) -> str:

        md = self.BaseMd()
        if md != "":
            md += "  \n"

        return md + f"> {self._outText}\n"
    
    def __add__( self,
            other: Text
        ) -> Quote:

        sep = " "

        q = Quote(
            parent = None, 
            identifier = self._identifier, 
            text = self._text + sep + other._text,
        )

        q._parent = self._parent
        q._outText = self._outText + sep + other._outText

        if q._parent:
            q._parent.Update(q._identifier, q)

        return q