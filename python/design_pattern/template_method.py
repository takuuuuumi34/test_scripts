class Report:
    def __init__(self):
        self.title = "some title"
        self.text = ["hoge", "fuga"]

    def output_report(self):
        self.output_start()
        self.output_head()
        self.output_body_start()
        self.output_body()
        self.output_body_end()
        self.output_end()

    def output_start(self):
        pass

    def output_head(self):
        pass

    def output_body_start(self):
        pass

    def output_body_end(self):
        pass

    def output_body(self):
        for l in self.text:
            self.output_line(l)

    def output_end(self):
        pass

    def output_line(self):
        pass


class HTMLReport(Report):
    def output_start(self):
        print("<html>")

    def output_head(self):
        print("<head>")
        print("<title>{}</title>".format(self.title))
        print("</head>")

    def output_body_start(self):
        print("<body>")

    def output_body_end(self):
        print("</body>")

    def output_body(self):
        for l in self.text:
            self.output_line(l)

    def output_line(self, l):
        print("<p>{}</p>".format(l))

    def output_end(self):
        print("</html>")
        print("")


class PlaneTextReport(Report):
    def output_head(self):
        print("***{}***".format(self.title))

    def output_line(self, l):
        print(l)

    def output_end(self):
        print("")

if __name__ == "__main__":
    report = PlaneTextReport()
    report.output_report()

    report = HTMLReport()
    report.output_report()
