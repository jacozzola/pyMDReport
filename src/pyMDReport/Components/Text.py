from pyMDReport.Components.pyMDComponent import pyMDComponent
from pyMDReport.types import Group, Report

class Text(pyMDComponent):

    def __init__(
            self,
            parent: Group | Report | None = None,
            identifier: str | None = None, 
            text: str | None = None,
        ):

        super().__init__(parent, identifier)
        
        self.text = ""
        if text:
            self.text = text.replace("\n", " \t")

    def MdRows(self):
        
        return [f"{self.text}\n"]
    
    def Fill(
            self, 
            text: str,
        ):

        self.text = text.replace("\n", " \t")