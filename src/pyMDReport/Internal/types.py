from io import TextIOWrapper

class pyMDComponent: pass
class ComponentType: pass

class Group ( pyMDComponent ): pass
class Report ( Group ): pass

class Text ( pyMDComponent ): pass
class Heading ( Text ): pass
class H1 ( Heading ): pass
class H2 ( Heading ): pass
class H3 ( Heading ): pass
class Quote ( Text ): pass
class Link ( Text ): pass
class Image ( Link ): pass


class pyMDComponent:
    _identifier: str
    _parent: Group | None
    _type: ComponentType
    def __init__( self,
            parent: Group | None = None,
            identifier: str | None = None,
        ): pass
    def GetAnchor( self ) -> str: pass
    def BaseMd( self ) -> str: pass
    def Md( self ) -> str: pass

class Group(pyMDComponent):
    _components : dict[str, pyMDComponent]
    def __init__( self, 
            parent : Group | None = None, 
            identifier : str | None = None,
        ): pass
    def Add( self,
            component: pyMDComponent,
        ): pass
    def Update( self,
            componentIdentifier: str,
            component: pyMDComponent,  
        ): pass
    def Md( self ) -> str: pass
    def Get( self, identifier: str | list[str] ) -> pyMDComponent: pass

class Report(Group):
    def __init__( self, 
            parent : Group | None = None, 
            identifier : str | None = None
        ): pass
    def Export( self, output: TextIOWrapper | str ): pass

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
        ): pass
    def Md( self ) -> str: pass
    def Format( self, *args, **kwargs ): pass
    def __add__( self,
            other: Text
        ) -> Text: pass
    
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
        ): pass
    def Md( self ) -> str: pass
    def __add__( self,
            other: Text
        ) -> Heading: pass
    
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
        ): pass
    def Md( self ) -> str: pass
    def __add__( self,
            other: Text
        ) -> Quote: pass
    
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
        ): pass
    
class Image(Link):
    def __init__( self,
            src : str,
            alt : str = "",
            parent : Group | None = None, 
            identifier : str | None = None,
        ): pass