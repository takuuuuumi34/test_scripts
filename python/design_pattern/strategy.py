class Report(object):
    def __init__(self, title, text, formatter):
        self.title = title
        self.text = text
        self.formatter = formatter

    def output_report(self):
        self.formatter.output_report(self.title, self.text)


class Formatter(object):
    def output_report(self, title, text):
        assert False


class HTMLFormatter(Formatter):
    def output_report(self, title, text):
        print("<html>")
        print("<head>")
        print("<title>{}</title>".format(title))
        print("</head>")
        print("<body>")
        for l in text:
            print("<p>{}</p>".format(l))
        print("</body>")
        print("</html>")
        print("")


class PlainTextFormatter(Formatter):
    def output_report(self, title, text):
        print("***{}***".format(title))
        for l in text:
            print(l)
        print("")

if __name__ == "__main__":
    report = Report("some title", ["hoge", "fuga"], PlainTextFormatter())
    report.output_report()

    report = Report("some title", ["hoge", "fuga"], HTMLFormatter())
    report.output_report()
