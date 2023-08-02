from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.Qsci import QsciScintilla, QsciLexerPython

class CodeEditor(QsciScintilla):
    def __init__(self, parent=None):
        super().__init__(parent)

        # Set the font to Courier New
        font = QFont()
        font.setFamily("Courier New")
        font.setFixedPitch(True)
        font.setPointSize(10)
        self.setFont(font)
        self.setMarginsFont(font)

        # Margin 0 is used for line numbers
        fontmetrics = QFontMetrics(font)
        self.setMarginsFont(font)
        self.setMarginWidth(0, fontmetrics.width("00000") + 6)
        self.setMarginLineNumbers(0, True)
        self.setMarginsBackgroundColor(QColor("#cccccc"))

        # Brace matching: enable for a brace immediately before or after the current position
        self.setBraceMatching(QsciScintilla.SloppyBraceMatch)

        # Current line visible with special background color
        self.setCaretLineVisible(True)
        self.setCaretLineBackgroundColor(QColor("#ffe4e4"))

        # Set Python lexer
        lexer = QsciLexerPython()
        lexer.setDefaultFont(font)
        self.setLexer(lexer)

        # Auto indentation
        self.setAutoIndent(True)

        # Set tab width
        self.setIndentationsUseTabs(False)
        self.setIndentationWidth(4)

        # Autocompletion
        self.setAutoCompletionSource(QsciScintilla.AcsAll)
        self.setAutoCompletionThreshold(1)

        # Folding margin
        self.setFolding(QsciScintilla.BoxedTreeFoldStyle)

        # Disable command key
        self.SendScintilla(QsciScintilla.SCI_CLEARCMDKEY, ord('D')+ (ord('U')<<16))
        self.SendScintilla(QsciScintilla.SCI_CLEARCMDKEY, ord('D')+ (ord('D')<<16))

        # Multiline editing
        self.SendScintilla(QsciScintilla.SCI_SETMULTIPASTE, 1)
        self.SendScintilla(QsciScintilla.SCI_SETADDITIONALSELECTIONTYPING, 1)