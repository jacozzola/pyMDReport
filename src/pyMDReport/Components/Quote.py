from pyMDReport.Components.Text import Text
from pyMDReport.types import Group, Report

class Quote(Text):

    def __init__(
            self,
            parent: Group | Report | None = None,
            identifier: str | None = None, 
            text: str | None = None,
        ):

        super().__init__(parent, identifier, text)

    def MdRows(self):
        
        return [f"> {self.text}\n"]