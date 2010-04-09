'''
Copyright (c) 2010 openpyxl

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.

@license: http://www.opensource.org/licenses/mit-license.php
@author: Eric Gazoni
'''

class Color(object):

    BLACK = 'FF000000'
    WHITE = 'FFFFFFFF'
    RED = 'FFFF0000'
    DARKRED = 'FF800000'
    BLUE = 'FF0000FF'
    DARKBLUE = 'FF000080'
    GREEN = 'FF00FF00'
    DARKGREEN = 'FF008000'
    YELLOW = 'FFFFFF00'
    DARKYELLOW = 'FF808000'

    def __init__(self, index):

        self.index = index


class Font(object):

    UNDERLINE_NONE = 'none'
    UNDERLINE_DOUBLE = 'double'
    UNDERLINE_DOUBLE_ACCOUNTING = 'doubleAccounting'
    UNDERLINE_SINGLE = 'single'
    UNDERLINE_SINGLE_ACCOUNTING = 'singleAccounting'

    def __init__(self):

        self.name = 'Calibri'
        self.size = 11
        self.bold = False
        self.italic = False
        self.superscript = False
        self.subscript = False
        self.underline = self.UNDERLINE_NONE
        self.strikethrough = False
        self.color = Color(Color.BLACK)

class Fill(object):

    FILL_NONE = 'none'
    FILL_SOLID = 'solid'
    FILL_GRADIENT_LINEAR = 'linear'
    FILL_GRADIENT_PATH = 'path'
    FILL_PATTERN_DARKDOWN = 'darkDown'
    FILL_PATTERN_DARKGRAY = 'darkGray'
    FILL_PATTERN_DARKGRID = 'darkGrid'
    FILL_PATTERN_DARKHORIZONTAL = 'darkHorizontal'
    FILL_PATTERN_DARKTRELLIS = 'darkTrellis'
    FILL_PATTERN_DARKUP = 'darkUp'
    FILL_PATTERN_DARKVERTICAL = 'darkVertical'
    FILL_PATTERN_GRAY0625 = 'gray0625'
    FILL_PATTERN_GRAY125 = 'gray125'
    FILL_PATTERN_LIGHTDOWN = 'lightDown'
    FILL_PATTERN_LIGHTGRAY = 'lightGray'
    FILL_PATTERN_LIGHTGRID = 'lightGrid'
    FILL_PATTERN_LIGHTHORIZONTAL = 'lightHorizontal'
    FILL_PATTERN_LIGHTTRELLIS = 'lightTrellis'
    FILL_PATTERN_LIGHTUP = 'lightUp'
    FILL_PATTERN_LIGHTVERTICAL = 'lightVertical'
    FILL_PATTERN_MEDIUMGRAY = 'mediumGray'

    def __init__(self):

        self.fill_type = self.FILL_NONE
        self.rotation = 0
        self.start_color = Color(Color.WHITE)
        self.end_color = Color(Color.BLACK)

class Border(object):

    BORDER_NONE = 'none'
    BORDER_DASHDOT = 'dashDot'
    BORDER_DASHDOTDOT = 'dashDotDot'
    BORDER_DASHED = 'dashed'
    BORDER_DOTTED = 'dotted'
    BORDER_DOUBLE = 'double'
    BORDER_HAIR = 'hair'
    BORDER_MEDIUM = 'medium'
    BORDER_MEDIUMDASHDOT = 'mediumDashDot'
    BORDER_MEDIUMDASHDOTDOT = 'mediumDashDotDot'
    BORDER_MEDIUMDASHED = 'mediumDashed'
    BORDER_SLANTDASHDOT = 'slantDashDot'
    BORDER_THICK = 'thick'
    BORDER_THIN = 'thin'

    def __init__(self):

        self.border_style = self.BORDER_NONE
        self.color = Color(Color.BLACK)

class Borders(object):

    DIAGONAL_NONE = 0
    DIAGONAL_UP = 1
    DIAGONAL_DOWN = 2
    DIAGONAL_BOTH = 3

    def __init__(self):

        self.left = Border()
        self.right = Border()
        self.top = Border()
        self.bottom = Border()
        self.diagonal = Border()
        self.diagonal_direction = self.DIAGONAL_NONE

        self.all_borders = Border()
        self.outline = Border()
        self.inside = Border()
        self.vertical = Border()
        self.horizontal = Border()

class Alignment(object):

    HORIZONTAL_GENERAL = 'general'
    HORIZONTAL_LEFT = 'left'
    HORIZONTAL_RIGHT = 'right'
    HORIZONTAL_CENTER = 'center'
    HORIZONTAL_CENTER_CONTINUOUS = 'centerContinuous'
    HORIZONTAL_JUSTIFY = 'justify'

    VERTICAL_BOTTOM = 'bottom'
    VERTICAL_TOP = 'top'
    VERTICAL_CENTER = 'center'
    VERTICAL_JUSTIFY = 'justify'

    def __init__(self):

        self.horizontal = self.HORIZONTAL_GENERAL
        self.vetical = self.VERTICAL_BOTTOM
        self.text_rotation = 0
        self.wrap_text = False
        self.shrink_to_fit = False
        self.indent = 0

class NumberFormat(object):

    FORMAT_GENERAL = 'General'

    FORMAT_TEXT = '@'

    FORMAT_NUMBER = '0'
    FORMAT_NUMBER_00 = '0.00'
    FORMAT_NUMBER_COMMA_SEPARATED1 = '#,##0.00'
    FORMAT_NUMBER_COMMA_SEPARATED2 = '#,##0.00_-'

    FORMAT_PERCENTAGE = '0%'
    FORMAT_PERCENTAGE_00 = '0.00%'

    FORMAT_DATE_YYYYMMDD2 = 'yyyy-mm-dd'
    FORMAT_DATE_YYYYMMDD = 'yy-mm-dd'
    FORMAT_DATE_DDMMYYYY = 'dd/mm/yy'
    FORMAT_DATE_DMYSLASH = 'd/m/y'
    FORMAT_DATE_DMYMINUS = 'd-m-y'
    FORMAT_DATE_DMMINUS = 'd-m'
    FORMAT_DATE_MYMINUS = 'm-y'
    FORMAT_DATE_XLSX14 = 'mm-dd-yy'
    FORMAT_DATE_XLSX15 = 'd-mmm-yy'
    FORMAT_DATE_XLSX16 = 'd-mmm'
    FORMAT_DATE_XLSX17 = 'mmm-yy'
    FORMAT_DATE_XLSX22 = 'm/d/yy h:mm'
    FORMAT_DATE_DATETIME = 'd/m/y h:mm'
    FORMAT_DATE_TIME1 = 'h:mm AM/PM'
    FORMAT_DATE_TIME2 = 'h:mm:ss AM/PM'
    FORMAT_DATE_TIME3 = 'h:mm'
    FORMAT_DATE_TIME4 = 'h:mm:ss'
    FORMAT_DATE_TIME5 = 'mm:ss'
    FORMAT_DATE_TIME6 = 'h:mm:ss'
    FORMAT_DATE_TIME7 = 'i:s.S'
    FORMAT_DATE_TIME8 = 'h:mm:ss@'
    FORMAT_DATE_YYYYMMDDSLASH = 'yy/mm/dd@'

    FORMAT_CURRENCY_USD_SIMPLE = '"$"#,##0.00_-'
    FORMAT_CURRENCY_USD = '$#,##0_-'
    FORMAT_CURRENCY_EUR_SIMPLE = '[$EUR ]#,##0.00_-'

    def builtin_format_codes(self):

        return dict([(f, getattr(self, f)) for f in dir(self) if f.startswith('FORMAT_')])

    def __init__(self):

        self.format_code = self.FORMAT_GENERAL

class Protection(object):

    PROTECTION_INHERIT = 'inherit'
    PROTECTION_PROTECTED = 'protected'
    PROTECTION_UNPROTECTED = 'unprotected'

    def __init__(self):

        self.locked = self.PROTECTION_INHERIT
        self.hidden = self.PROTECTION_INHERIT

class DocumentStyle(object):

    def __init__(self):

        self.font = Font()
        self.fill = Fill()
        self.borders = Borders()
        self.alignment = Alignment()
        self.number_format = NumberFormat()
        self.protection = Protection()