class pyMDComponentType:
    Generic = 0x01
    Group = 0x10
    Text = 0x20
    Heading = 0x21
    Table = 0x30



class pyMDComponent: pass

class Group ( pyMDComponent ): pass

class Report ( Group ): pass

class Text ( pyMDComponent ): pass

class Heading ( Text ): pass

class H1 ( Heading ): pass
class H2 ( Heading ): pass
class H3 ( Heading ): pass



class pyMDComponent:
    identifier: str
    parent: Group | None
    componentType: pyMDComponentType
    def __init__( self, 
        identifier: str | None = None, 
        parent: Group | None = None, 
    ): pass
    def MdRows( self ) -> list[str]: pass
    def Md( self ) -> str: pass 

class Group ( pyMDComponent ):
    components: dict[str, pyMDComponent]
    def Add( self,
        component: pyMDComponent, 
        componentIdentifier : str | None = None, 
    ): pass

class Report ( Group ):
    pass

class Text ( pyMDComponent ):
    text: str

class Heading ( Text ):
    MAX_HEADING_LEVEL: int

class H1 (Heading): pass
class H2 (Heading): pass
class H3 (Heading): pass