from pyMDReport.Components.pyMDComponent import pyMDComponent
from pyMDReport.types import Group, Report

class ExampleComponent(pyMDComponent):

    def __init__(
            self, 
            text: str, 
            identifier: str | None = None,
            parent: Group | Report | None = None
        ):
        
        super().__init__(identifier, parent)

        self.text = text

    def MdRows(self):
        return [self.text]