# https://book.pythontips.com/en/latest/context_managers.html
# https://www.w3schools.com/python/python_ref_file.asp
# https://www.tutorialsteacher.com/python/magic-methods-in-python
# https://dmitrygolovach.com/python-magic-context-manager/

class CsvReader:
    # def __init__(self, file_name, method):
    def __init__(self, filename=None, sep=',', header=False, skip_top=0, skip_bottom=0):
        try:
            self.fileOpened = False
            self.file = open(filename, "r")
            self.header = header
            self.fileHeader = []
            self.records = []
            self.sep = sep
            self.skip_top = skip_top
            self.skip_bottom = skip_bottom
            self.len = 0
            self.fileOpened = True
        except Exception:
            return

    def __enter__(self):
        if not self.fileOpened:
            return None

        firstIter = True
        for line in self.file.readlines():
            newRecord = (line.strip('\n')).split(self.sep)
            if firstIter:
                self.field_nb = line.count(self.sep) + 1
                if self.header:
                    self.fileHeader.append(newRecord)
                firstIter = False
            self.records.append(newRecord)
            if len(newRecord) != self.field_nb:
                self.records = None
                return None
            for i in newRecord:
                if len(i) == 0:
                    self.records = None
                    return None
        self.len = len(self.records)
        return self

    def __exit__(self, type, value, traceback):
        if value or traceback or type:
            print("Error: {}".format(value, traceback.tb_frame))
        if self.fileOpened:
            self.file.close()
        return True

    def getdata(self):
        """ Retrieves the data/records from skip_top to skip bottom.
        Return:
        nested list (list(list, list, ...)) representing the data.
        """
        cpRecords = self.records
        cpSkiptop = self.skip_top
        cpSkipbottom = self.skip_bottom
        cpLen = self.len

        if self.header:
            del cpRecords[0]

        while cpLen and cpSkiptop > 0:
            del cpRecords[0]
            cpLen -= 1
            cpSkiptop -= 1
        while cpLen and cpSkipbottom > 0:
            del cpRecords[-1]
            cpLen -= 1
            cpSkipbottom -= 1
        return cpRecords

    def getheader(self):
        """ Retrieves the header from csv file.
        Returns:
        list: representing the data (when self.header is True).
        None: (when self.header is False).
        """
        if self.header is True:
            return self.fileHeader
        else:
            return None
