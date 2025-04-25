from pyMDReport.Internal.Components.Text import Text

from pyMDReport.Internal.ComponentTypes import ComponentType

from pyMDReport.Internal.types import Group, Heading

class Heading(Text):

    MAX_HEADING_LEVEL = 3
    _headingLevel: int

    def __init__( self, 
        parent : Group | None = None, 
        identifier : str | None = None,
        headingLevel : int = 1,
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

        if headingLevel < 1: headingLevel = 1
        if headingLevel > self.MAX_HEADING_LEVEL: headingLevel = self.MAX_HEADING_LEVEL
        
        self._headingLevel = headingLevel

        self._type = ComponentType.heading
        
    def Md( self ) -> str:

        return f"{'#'*self._headingLevel} {self._outText}"
    
    def __add__( self,
            other: Text
        ) -> Heading:

        sep = " "

        h = Heading(
            parent = None, 
            identifier = self._identifier, 
            text = self._text + sep + other._text,
            headingLevel = self._headingLevel
        )

        h._parent = self._parent
        h._outText = self._outText + sep + other._outText

        if h._parent:
            h._parent.Update(h._identifier, h)

        return h
    


class H1(Heading):

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
            headingLevel = 1,
            bold = bold, 
            italic = italic, 
            strike = strike, 
            sub = sub, 
            sup = sup, 
            underlined = underlined,
        )


class H2(Heading):

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
            headingLevel = 2,
            bold = bold, 
            italic = italic, 
            strike = strike, 
            sub = sub, 
            sup = sup, 
            underlined = underlined,
        )


class H3(Heading):

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
            headingLevel = 3,
            bold = bold, 
            italic = italic, 
            strike = strike, 
            sub = sub, 
            sup = sup, 
            underlined = underlined,
        )