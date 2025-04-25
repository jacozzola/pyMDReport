from pyMDReport.Internal.Components.Text import Text
from pyMDReport.Internal.Components.pyMDComponent import pyMDComponent

from pyMDReport.Internal.types import Group
from pyMDReport.exceptions import InvalidLinkException

from pyMDReport.Internal.ComponentTypes import ComponentType

class Link(Text):

    def __init__( self, 
        target : str | pyMDComponent,
        parent : Group | None = None, 
        identifier : str | None = None, 
        text : str | None = None, 
        bold : bool = False, 
        italic : bool = False, 
        strike : bool = False, 
        sub : bool = False, 
        sup : bool = False, 
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

        if type(target) != str:
            if type(target) != pyMDComponent and not issubclass(type(target), pyMDComponent):
                raise InvalidLinkException(f"Invalid link target: {target}")
            target = target.GetAnchor()
            
        self._text = f"[{self._text}]({target})"
        self._outText = self._text
        
        self._type = ComponentType.link