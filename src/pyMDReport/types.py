class pyMDComponent: pass
class Group ( pyMDComponent ): pass
class Report: pass

class pyMDComponent:
    identifier: str
    parent: Report | pyMDComponent | None
    def __init__( self, 
        identifier: str, 
        parent: Report | pyMDComponent | None = None, 
    ): pass
    def MdRows( self ) -> list[str]: pass 

class Group ( pyMDComponent ):
    components: dict[str, pyMDComponent]
    def AddComponent( self, 
        component: pyMDComponent, 
        componentIdentifier : str | None = None, 
    ): pass

class Report:
    groups : dict[str, Group]
    def AddGroup( self, 
        group: Group, 
        groupIdentifier: str | None = None, 
    ): pass
    def AddComponent( self, 
        groupIdentifier: str, 
        component: pyMDComponent,
    ): pass