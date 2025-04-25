from pyMDReport.Internal.Components.pyMDComponent import pyMDComponent

from pyMDReport.Internal.types import Group
from pyMDReport.Internal.ComponentTypes import ComponentType

from pyMDReport.exceptions import AddComponentException, GetComponentException, UpdateComponentException

class Group(pyMDComponent):

    _components : dict[str, pyMDComponent]

    def __init__( self, 
            parent : Group | None = None, 
            identifier : str | None = None,
        ):

        super().__init__(
            parent = parent, 
            identifier = identifier,
        )

        self._components = {}

        self._type = ComponentType.group

    def Add( self,
            component: pyMDComponent,
        ):

        componentId = component._identifier

        if componentId in self._components.keys():
            raise AddComponentException("A pyMDComponent with the given identifier already exists in this group")
        
        self._components[componentId] = component

    def Update( self,
            componentIdentifier: str,
            component: pyMDComponent,  
        ):

        if componentIdentifier not in self._components.keys():
            raise UpdateComponentException(f"Component identifier not found: {componentIdentifier}")
        
        self._components[componentIdentifier] = component

    def Md( self ) -> str:

        md = self.BaseMd()
        if md != "":
            md += "  \n"
        
        componentsMd = [component.Md() for cId, component in self._components.items()]
        md += '  \n'.join(componentsMd)

        return md
    
    def Get( self, identifier: str | list[str] ) -> pyMDComponent:

        if type(identifier) == str:
            
            component = self._components.get(identifier)

            if not component:
                raise GetComponentException(f"Component with given identifier not found: {identifier}")
            
        elif type(identifier) == list:

            if len(identifier) == 1:
                identifier = identifier[0]
                return self.Get( identifier )

            group = self._components.get(identifier[0])

            if not group:
                raise GetComponentException(f"Group not found: {identifier[0]}")
            
            if group._type != ComponentType.group:
                raise GetComponentException(f"Component is not a Group: {identifier[0]}")

            component = group.Get(identifier[1:])

        return component
            
            