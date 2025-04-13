import uuid

from pyMDReport.types import Group, pyMDComponentType

class pyMDComponent:

    def __init__(
            self,
            parent: Group | None = None,
            identifier: str | None = None,
        ):

        if not identifier:
            identifier = uuid.uuid4()

        self.identifier = identifier

        self.parent = parent
        if parent:
            parent.Add(self)

        self.componentType = pyMDComponentType.Generic

    def MdRows(
            self  
        ) -> list[str]:

       return []
    
    def Md( 
            self 
        ) -> str:
        
        return "\n".join(self.MdRows())
    
    def Fill(
            self
        ):

        return