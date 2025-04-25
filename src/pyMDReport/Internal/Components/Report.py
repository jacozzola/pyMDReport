from pyMDReport.Internal.Components.Group import Group

from pyMDReport.Internal.ComponentTypes import ComponentType

from io import TextIOWrapper

class Report(Group):

    def __init__( self, 
            parent : Group | None = None, 
            identifier : str | None = None
        ):
        
        super().__init__(
            parent = parent, 
            identifier = identifier
        )

        self._type = ComponentType.report

    def Export( self, output: TextIOWrapper | str ):

        if type(output) == str:
            output = open(output, "w")
        
        output.write( self.Md() )
