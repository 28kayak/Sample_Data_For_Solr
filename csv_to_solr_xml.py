#!/usr/bin/env python

import pandas as pd


df_header = pd.read_csv('sample_products_data_csv/sample_products3.csv', header=0)
print(df_header)

#product_codes = df_header["code"]
#print(product_codes)
#product_name = df_header["name"]
#product_unit_amount = df_header["unit_amount"]
#product_release_day = df_header["release_day"]
#product_maker = df_header["maker"]#

#product_price = df_header["price"]


xml_file = open("sample_products_data_solr_xml/sample_products3.xml", "w")


def convert_row(row):
    #print("----")
    print(row.product_name)
    #print(row.values.code)
    #print("====")
    return """<doc>
    <field name="id">%d</field>
    <field name="product_code">%s</field>
    <field name="product_name">%s</field>
    <field name="product_unit_amount">%s</field>
    <field name="product_maker">%s</field>
    <field name="field_release_day">%s</field>
    <field name="product_price">%s</field>
</doc>""" % (int(row.name + 600), row.code,  row.product_name, row.unit_amount, row.maker, row.release_day, row.price)


#print('\n'.join(df_header.apply(convert_row, axis=1)))
xml_file.write("<add>")
xml_file.write(' '.join(df_header.apply(convert_row, axis=1)))
xml_file.write("</add>")
# <field name="id">%s</field>