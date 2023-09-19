# 1. beolvasás
# 2. kilistázás jsonban 1 obj
# 3. kilistázás jsonban több obj
# 4. objektum neve, x,y
# 5. bitmap készítése

import typing
from borb.pdf import Document
from borb.pdf import PDF


class MyPDFObject:

    def __init__(self):
        self.x = None
        self.y = None
        self.width = None
        self.height = None


def main():
    # read the Document
    doc: typing.Optional[Document] = None
    with open('output.pdf', "rb") as in_file_handle:
        doc = PDF.loads(in_file_handle)

    # check whether we have read a Document
    assert doc is not None

    print(doc.get_page(0).get_page_info())
    print(doc.get_page(0).get_document())
    print(doc.get_page(0).items())

    res = doc.to_json()
    decoded_bytes = res['XRef']['Trailer']['Root']['Pages']['Kids'][0]['Contents']['DecodedBytes']
    res_str = str(decoded_bytes[2:-1])
    pdf_object_list = []
    pdf_obj = None
    print("--------------------------------")
    for line in res_str.split("\\n"):
        if "BT" in line:
            pdf_obj = MyPDFObject()
        if pdf_obj is not None:
            if "Tm" in line:
                print(line.split())
                current_line = line.split()
                pdf_obj.height = current_line[0]
                pdf_obj.width = current_line[5]
                pdf_obj.x = current_line[4]
                pdf_obj.y = current_line[5]
        if "ET" in line:
            pdf_object_list.append(pdf_obj)

    '''
    q                                               betszi a stack-be az új grafikus környezet                     
    BT                                              szöveg kezdete
    0.000000 0.000000 0.000000 rg                   RGB szín
    /F1 1.000000 Tf                                 F1 típusú font, méret 1                                 
    12.000000 0 0 12.000000 59.500000 748.284000 Tm font transzformáció, méret: 12, x, y, szélesség 
    (Hello World!) Tj                               (string) szöveg                                
    ET                                              szöveg vége
    Q                                               kiveszi a stackből a grafikus környezetet
    '''

    for pdf_obj in pdf_object_list:
        print(pdf_obj.x, pdf_obj.y)

if __name__ == "__main__":
    main()
