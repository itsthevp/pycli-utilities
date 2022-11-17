"""
    Copyright (c) 2022 Vishv Patel (https://github.com/itsthevp)

    Permission is hereby granted, free of charge, to any person obtaining a copy of
    this software and associated documentation files (the "Software"), to deal in
    the Software without restriction, including without limitation the rights to
    use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of
    the Software, and to permit persons to whom the Software is furnished to do so,
    subject to the following conditions:

    The above copyright notice and this permission notice shall be included in all
    copies or substantial portions of the Software.

    THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
    IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS
    FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR
    COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER
    IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN
    CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
"""

from source.cli import CSVUtils


class ValidateCSV(CSVUtils):
    prog = "csv-validate"
    description = "This utility is designed to validate CSV file."

    def main(self) -> None:
        with open(
            file=self.args.input, mode="r", encoding=self.args.encoding
        ) as fo:
            line = fo.readline()
            cols = line.count(self.args.seperator)
            while line:
                if line.count(self.args.seperator) != cols:
                    self.log("Result: INVALID")
                    break
                line = fo.readline()
            else:
                self.log("Result: VALID")


def run() -> None:
    ValidateCSV().run()


if __name__ == "__main__":
    run()