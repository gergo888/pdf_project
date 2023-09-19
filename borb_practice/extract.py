#!chapter_005/src/snippet_002.py
import typing
from borb.pdf import Document
from borb.pdf import PDF
import pprint

def main():

    # read the Document
    doc: typing.Optional[Document] = None
    with open("output.pdf", "rb") as in_file_handle:
        doc = PDF.loads(in_file_handle)

    # check whether we have read a Document
    assert doc is not None

    # print the \Author key from the \Info dictionary
    print("Author: %s" % doc.get_document_info().get_keywords())
    pprint.pprint(doc.to_json())
    page = doc.get_page(0)
    pprint.pprint(page.get_page_info())

if __name__ == "__main__":
    main()
