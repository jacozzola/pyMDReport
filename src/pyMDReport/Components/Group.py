from pyMDReport.Components.pyMDComponent import pyMDComponent, pyMDComponentType
from pyMDReport.exceptions import AddComponentException
from pyMDReport.types import Group, Report

class Group(pyMDComponent):

    def __init__(
            self, 
            *components: pyMDComponent,
            parent: Group | Report | None = None,
            identifier: str | None = None, 
        ):
        
        super().__init__(parent, identifier)

        self.components : dict[str, pyMDComponent] = {}
        self.componentType = pyMDComponentType.Group

        if len(components) > 0:
            for component in components:
                self.Add(component)

    def Add(
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
        component.parent = self

    def MdRows( self ) -> list[str]:
        
        mdRows = []
        for componentIdentifier in self.components.keys():
            component = self.components[componentIdentifier]
            mdRows += component.MdRows()
        return mdRows
    
    def Fill(
            self,
            componentData: dict[str, dict], 
        ):

        for componentIdentifier in componentData.keys():
            if componentIdentifier in self.components.keys():
                self.components[componentIdentifier].Fill( componentData[componentIdentifier] )