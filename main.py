from antlr4 import *
from CSVFilterLexer import CSVFilterLexer
from CSVFilterParser import CSVFilterParser
from MyCSVVisitor import MyCSVVisitor
from CustomErrorListener import CustomErrorListener

def main():
    input_stream = FileStream("programa.dsl", encoding='utf-8')
    lexer = CSVFilterLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = CSVFilterParser(stream)

    # Add custom error listener
    parser.removeErrorListeners()
    parser.addErrorListener(CustomErrorListener())

    tree = parser.prog()
    visitor = MyCSVVisitor()
    visitor.visit(tree)

if __name__ == "__main__":
    main()
