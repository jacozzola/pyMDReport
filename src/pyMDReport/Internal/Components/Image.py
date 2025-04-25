from pyMDReport.Internal.Components.Link import Link

from pyMDReport.Internal.types import Group

from pyMDReport.Internal.ComponentTypes import ComponentType

class Image(Link):

    def __init__( self,
        src : str,
        alt : str = "",
        parent : Group | None = None, 
        identifier : str | None = None,
    ):
        
        super().__init__(
            parent = parent,
            target = src, 
            identifier = identifier, 
            text = alt,
        )

        self._text = f"!{self._text}"
        self._outText = self._text

        self._type = ComponentType.image