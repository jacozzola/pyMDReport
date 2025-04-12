from pyMDReport.Components.pyMDComponent import pyMDComponent
from pyMDReport.exceptions import AddComponentException

class Group(pyMDComponent):

    def __init__(self, identifier, parent = None):
        
        super().__init__(identifier, parent)
        
        self.components : dict[str, pyMDComponent] = {}

    def AddComponent(
            self,
            component: pyMDComponent,
            componentIdentifier: str | None = None,
        ):

        componentId = component.identifier
        if componentIdentifier:
            componentId = componentIdentifier

        if componentId in self.components.keys():
            raise AddComponentException("A pyMDComponent with the given identifier already exists in this group")
        
        self.components[componentId] = component

    def MdRows( self ) -> list[str]:
        
        mdRows = []
        for componentIdentifier in self.components.keys():
            component = self.components[componentIdentifier]
            mdRows += component.MdRows()
        return mdRows
    
    def Md( self ) -> str:
        
        return '\n'.join(self.MdRows())