#!/usr/bin/env python

import pandas as pd


df_header = pd.read_csv('sample_products_data_csv/sample_products3.csv', header=0)

product_codes = df_header["code"]
product_name = df_header["name"]
product_unit_amount = df_header["unit_amount"]
product_price = df_header["price"]
product_maker = df_header["maker"]
product_release_day = df_header["release_day"]

xml_file = open("sample_products_data_solr_xml/sample_products3.xml", "w")


def convert_row(row):
    return """<doc><field name="product_code">%s</field>
    <field name="product_name">%s</field>
    <field name="product_unit_amount" >%s</field>
    <field name="product_price">%s</field>
    <field name="product_maker">%s</field>
    <field name="field_release_day">%s</field>
</doc>""" % (
    row.code, row.name, row.unit_amount, row.price, row.maker, row.release_day)


#print('\n'.join(df_header.apply(convert_row, axis=1)))
xml_file.write("<add>")
xml_file.write('\n'.join(df_header.apply(convert_row, axis=1)))
xml_file.write("</add>")