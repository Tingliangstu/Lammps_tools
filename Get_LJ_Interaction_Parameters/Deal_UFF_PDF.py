#!/usr/bin/python
# -*- coding: UTF-8 -*-

import  camelot                                                 #An extension that specifically extracts tables from a PDF
import  matplotlib.pyplot  as  plt

def   get_pdf_information ():
         tables = camelot.read_pdf('UFF.pdf', pages='3', flavor='stream', table_area=['68,710, 545,140']) #strip_text=' \n')
         camelot.plot(tables[0], kind='text')
         #plt.show()                                              # Leave it uncommented when needed
         table_df = tables[0].df
         print(type(table_df))
         table_df[7:71].to_csv('LJ_data.csv')


if       __name__ == "__main__":

         get_pdf_information() 
