from pyMDReport.types import Report, pyMDComponent

class pyMDComponent:

    def __init__(
            self,
            identifier: str,
            parent: Report | pyMDComponent | None = None,
        ):

        self.identifier = identifier

    def MdRows(
            self  
        ) -> list[str]:

       pass 