from pyMDReport.Components.pyMDComponent import pyMDComponent

class ExampleComponent(pyMDComponent):

    def __init__(
            self, 
            identifier,
            text: str, 
            parent = None,
        ):
        
        super().__init__(identifier, parent)

        self.text = text

    def MdRows(self):
        return [self.text]