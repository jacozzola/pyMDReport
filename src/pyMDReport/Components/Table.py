from pyMDReport.Components.pyMDComponent import MdComponent

class Table(MdComponent):

    def __init__(
            self,
            *args,
            data: list[dict] = [],
            columns: list[str] | None = None,
            columnNames: dict[str, str] | None = None,
            **kwargs,
        ):
        '''
        Table.__init__  
        ### params

        - **data** _list[ dict ]_   
        Data to be displayed with the table
        
        - **? columns** _list[ str ]_    
        Keys of **data**'s objects that will be included in the table   
        If not given will be inherited by the first element of **data**

        - **? columnNames** _dict[ str, str ]_    
        Dictionary that associates **columns** with their names  
        If given the names will replace the columns in the table    

        ### returns
        **Table** object
        '''

        super().__init__(*args, **kwargs)

        self.data = data
        self.columns = columns
        self.columnNames = columnNames


    def MdRows( self ):

        mdRows = []

        columns = []
        if self.columns:
            columns = self.columns
        elif len(self.data) > 0:
            columns = list(self.data[0].keys())

        if len(columns) == 0:
            return mdRows

        colRow = "|"
        sepRow = "|"
        emptyRow = "|"
        for column in columns:
            colName = column
            if column in self.columnNames.keys():
                colName = self.columnNames[column]
            colRow += colName + "|"
            sepRow += "-|"
            emptyRow += " |"
        
        mdRows.append(colRow)
        mdRows.append(sepRow)

        if len(self.data) == 0:
            mdRows.append(emptyRow)
            return mdRows

        for element in self.data:
            mdString = "|"
            for column in columns:
                mdString += f"{element.get(column, " ")}|"
            mdRows.append(mdString)

        return mdRows