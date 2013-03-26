import html2text

def test_table():
    print html2text.html2text("<table><tr><th>Header 1</th><th>Header 2</th></tr><tr><td>1</td><td>Hello</td></tr></table>")

def test_norm():
    print html2text.normtable("|Header 1|Header 2|\n|:-----|:-----|\n|1|Hello|")

#    print html2text.normtable("|Header 1|Header 2|\n|:-----|:-----|\n|1|Hello|")
test_table()
#test_norm()