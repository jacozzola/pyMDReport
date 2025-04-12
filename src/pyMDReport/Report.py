from pyMDReport.types import Group, pyMDComponent
from pyMDReport.exceptions import AddGroupException, AddComponentException

class Report:

    def __init__( self ):
        
        self.groups : dict[str, Group] = {}

    def AddGroup(
            self,
            group: Group,
            groupIdentifier: str | None = None,
        ):

        groupId = group.identifier
        if groupIdentifier:
            groupId = groupIdentifier

        if groupId in self.groups.keys():
            raise AddGroupException("A Group with the given identifier already exists in this report")
        
        self.groups[groupId] = group

    def AddComponent(
            self,
            groupIdentifier: str,
            component: pyMDComponent,
            componentIdentifier: str | None = None,
        ):
        
        group = self.groups.get(groupIdentifier)
        
        if not group:
            raise AddComponentException(f"Unknown groupIdentifier: {groupIdentifier}")
        
        group.AddComponent(
            component, 
            componentIdentifier,
        )

    def MdRows( self ) -> list[str]:

        mdRows = []
        for groupIdentifier in self.groups.keys():
            group = self.groups[groupIdentifier]
            mdRows += group.MdRows()
        return mdRows
    
    def Md( self ) -> str:
        
        return '\n'.join(self.MdRows())

    def Export(
            self,
            outputFile: str,
        ):

        md = self.Md()

        print(md)
        with open(outputFile, "w+") as outputHandle:
            outputHandle.write( md )