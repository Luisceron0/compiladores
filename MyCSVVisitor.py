import csv
from CSVFilterVisitor import CSVFilterVisitor

class MyCSVVisitor(CSVFilterVisitor):
    def __init__(self):
        self.data = []
        self.filtered_data = []
        self.filename = ""

    def visitLoadStat(self, ctx):
        self.filename = ctx.STRING().getText().replace('"', '')
        with open(self.filename, newline='') as f:
            self.data = list(csv.DictReader(f))
        return None

    def visitFilterStat(self, ctx):
        column = ctx.STRING().getText().replace('"', '')
        op = ctx.OPERATOR().getText()
        value = int(ctx.INT().getText())
        self.filtered_data = [
            row for row in self.data
            if eval(f"{int(row[column])} {op} {value}")
        ]
        return None

    def visitPrintStat(self, ctx):
        for row in self.filtered_data:
            print(row)
        return None
