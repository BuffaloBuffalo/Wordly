class ResultsManipulator:
    def __init__(self, results):
        self.results=results
    def sortByLengthDesc(self):
        copy = list(self.results)
        copy.sort(key=len)
        copy.reverse()
        return copy 