from pyMDReport.Components.Text import Text
from pyMDReport.types import Group, Report

class Heading(Text):

    MAX_HEADING_LEVEL = 3

    def __init__(
            self,
            headingLevel: int,
            parent: Group | Report | None = None,
            identifier: str | None = None, 
            text: str | None = None,
        ):

        super().__init__(
            parent = parent, 
            identifier = identifier,
            text = text,
        )

        if headingLevel > self.MAX_HEADING_LEVEL:
            headingLevel = self.MAX_HEADING_LEVEL

        self.headingLevel = headingLevel

    def MdRows(self):
        
        return [f"{'#'*self.headingLevel} {self.text}"]
    


class H1(Heading):

     def __init__(
            self,
            parent: Group | Report | None = None,
            identifier: str | None = None, 
            text: str | None = None,
        ):

        super().__init__(1, parent, identifier, text)



class H2(Heading):

     def __init__(
            self,
            parent: Group | Report | None = None,
            identifier: str | None = None, 
            text: str | None = None, 
        ):

        super().__init__(2, parent, identifier, text)



class H3(Heading):

     def __init__(
            self,
            parent: Group | Report | None = None,
            identifier: str | None = None, 
            text: str | None = None,
        ):

        super().__init__(3, parent, identifier, text)