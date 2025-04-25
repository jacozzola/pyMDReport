import uuid

from pyMDReport.Internal.types import Group
from pyMDReport.Internal.ComponentTypes import ComponentType

class pyMDComponent:

    _identifier: str
    _parent: Group | None
    _type: ComponentType

    def __init__( self,
            parent: Group | None = None,
            identifier: str | None = None,
        ):

        self._identifier = identifier
        if not identifier:
            self._identifier = uuid.uuid4().hex

        self._parent = parent
        if self._parent:
            self._parent.Add(self)

        self._type = ComponentType.pymdcomponent

        self._anchor = {
            "id": uuid.uuid4().hex,
            "active": False,
        }

    def GetAnchor( self ) -> str:

        self._anchor["active"] = True        
        return "#" + self._anchor["id"]

    def BaseMd( self ) -> str:
        
        md = ""
        if self._anchor["active"]:
            md = f'<a id="{self._anchor["id"]}"></a>'

        return md

    def Md( self ) -> str:

        return ""

        

