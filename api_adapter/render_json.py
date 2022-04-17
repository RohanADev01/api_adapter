import re
import xmltodict
import json
from datetime import datetime

MISSING = "ERROR DATA MISSING"
INVALID = "ERROR INVALID DATA TYPE. EXPECTED: "

def conv_xml_to_dict(ubl_file_name):
    try:
        xml_string = open(ubl_file_name).read()
        return xmltodict.parse(xml_string)
    except FileNotFoundError:
        raise Exception('UBL cannot be found')

# Confirms data for a string is relevant and accurate
def try_string(input_string):
    try:
        if not input_string:
            raise TypeError
        elif type(input_string) != str:
            raise ValueError
        else:
            return input_string
    except TypeError:
        return MISSING
    except ValueError:
        return INVALID + "STRING"

def try_int(input_int):
    try:
        return int(input_int)
    except TypeError:
        return MISSING
    except ValueError:
        return INVALID + "INT"

# Confirms data for a float is relevant and accurate
def try_float(input_float):
    try:
        return float(input_float)
    except TypeError:
        return MISSING
    except ValueError:
        return INVALID + "FLOAT"

def try_currency(input_currency):
    try:
        return "{:.2f}".format(float(input_currency))
    except TypeError:
        return MISSING
    except ValueError:
        return INVALID + "FLOAT"

def try_date(input_date):
    try:
        if not input_date:
            raise TypeError
        return datetime.strptime(input_date, '%Y-%M-%d').date()
    except TypeError:
        return MISSING
    except SyntaxError:
        return INVALID + "DATE FORMATTED YYYY-MM-DD"


# Gets a string of ID
def get_ID(ubl_dict):
    val = ubl_dict['Invoice']['cbc:ID']
    return try_string(val)

# Gets a string of InvoiceTaxSchemeID
def get_InvoiceTaxSchemeID(ubl_dict):
    val = ubl_dict['Invoice']['cac:InvoiceLine']['cac:Item']['cac:ClassifiedTaxCategory']['cac:TaxScheme']['cbc:ID']['#text']
    return try_string(val)

# Gets a string of InvoiceName
def get_InvoiceName(ubl_dict):
    val = ubl_dict['Invoice']['cac:InvoiceLine']['cac:Item']['cbc:Name']
    return try_string(val)

# Gets a date of IssueDate
def get_IssueDate(ubl_dict):
    val = ubl_dict['Invoice']['cbc:IssueDate']
    return try_date(val)

# Gets a currency of PayableAmount
def get_PayableAmount(ubl_dict):
    val = ubl_dict['Invoice']['cac:LegalMonetaryTotal']['cbc:PayableAmount']['#text']
    return try_currency(val)

# Gets a currency of PayableAmount
def get_PayableAmount(ubl_dict):
    val = ubl_dict['Invoice']['cac:LegalMonetaryTotal']['cbc:PayableAmount']['#text']
    return try_currency(val)

# Gets a float of InvoiceQuantity
def get_InvoiceQuantity(ubl_dict):
    val = ubl_dict['Invoice']['cac:InvoiceLine']['cbc:InvoicedQuantity']['#text']
    return try_float(val)

# Gets a currency of Currency
def get_Currency(ubl_dict):
    val = ubl_dict['Invoice']['cac:InvoiceLine']['cbc:LineExtensionAmount']['#text']
    return try_currency(val)

# Gets a string of PaymentTerms
def get_PaymentTerms(ubl_dict):
    val = ubl_dict['Invoice']['cac:PaymentTerms']['cbc:Note']
    return try_string(val)

# Gets a currency of TaxAmount
def get_TaxAmount(ubl_dict):
    val = ubl_dict['Invoice']['cac:TaxTotal']['cbc:TaxAmount']['#text']
    return try_currency(val)

# Gets a currency of TaxableAmount
def get_TaxableAmount(ubl_dict):
    val = ubl_dict['Invoice']['cac:TaxTotal']['cac:TaxSubtotal']['cbc:TaxableAmount']['#text']
    return try_currency(val)

# Gets a currency of TaxExclusiveAmount
def get_TaxExclusiveAmount(ubl_dict):
    val = ubl_dict['Invoice']['cac:LegalMonetaryTotal']['cbc:TaxExclusiveAmount']['#text']
    return try_currency(val)

# Gets a currency of TaxInclusiveAmount
def get_TaxInclusiveAmount(ubl_dict):
    val = ubl_dict['Invoice']['cac:LegalMonetaryTotal']['cbc:TaxInclusiveAmount']['#text']
    return try_currency(val)

# Gets an int of TaxSchemeID
def get_TaxSchemeID(ubl_dict):
    val = ubl_dict['Invoice']['cac:TaxTotal']['cac:TaxSubtotal']['cac:TaxCategory']['cac:TaxScheme']['cbc:ID']['@schemeID']
    return try_string(val)

# Gets a string of the SupplierRegistrationName
def get_SupplierRegistration(ubl_dict):
    val = ubl_dict['Invoice']['cac:AccountingSupplierParty']['cac:Party']['cac:PartyLegalEntity']['cbc:RegistrationName']
    return try_string(val)

# Gets a string of SupplierStreet
def get_SupplierStreet(ubl_dict):
    val = ubl_dict['Invoice']['cac:AccountingSupplierParty']['cac:Party']['cac:PostalAddress']['cbc:StreetName']
    return try_string(val)

# Gets a string of SupplierCity
def get_SupplierCity(ubl_dict):
    val = ubl_dict['Invoice']['cac:AccountingSupplierParty']['cac:Party']['cac:PostalAddress']['cbc:CityName']
    return try_string(val)

# Gets a string of SupplierPost
def get_SupplierPost(ubl_dict):
    val = ubl_dict['Invoice']['cac:AccountingSupplierParty']['cac:Party']['cac:PostalAddress']['cbc:PostalZone']
    return try_int(val)

# Gets a string of SupplierCountry
def get_SupplierCountry(ubl_dict):
    val = ubl_dict['Invoice']['cac:AccountingSupplierParty']['cac:Party']['cac:PostalAddress']['cac:Country']['cbc:IdentificationCode']['#text']
    return try_string(val)

# Gets a string of the CustomerRegistration
def get_CustomerRegistration(ubl_dict):
    val = ubl_dict['Invoice']['cac:AccountingCustomerParty']['cac:Party']['cac:PartyLegalEntity']['cbc:RegistrationName']
    return try_string(val)

# Gets a string of the CustomerStreet
def get_CustomerStreet(ubl_dict):
    val = ubl_dict['Invoice']['cac:AccountingCustomerParty']['cac:Party']['cac:PostalAddress']['cbc:StreetName']
    return try_string(val)

# Gets a string of the CustomerCity
def get_CustomerCity(ubl_dict):
    val = ubl_dict['Invoice']['cac:AccountingCustomerParty']['cac:Party']['cac:PostalAddress']['cbc:CityName']
    return try_string(val)

# Gets an int of the CustomerPost
def get_CustomerPost(ubl_dict):
    val = ubl_dict['Invoice']['cac:AccountingCustomerParty']['cac:Party']['cac:PostalAddress']['cbc:PostalZone']
    return try_int(val)

# Gets a strings of the IdentificationCode
def get_CustomerCountry(ubl_dict):
    val = ubl_dict['Invoice']['cac:AccountingCustomerParty']['cac:Party']['cac:PostalAddress']['cac:Country']['cbc:IdentificationCode']['#text']
    return try_string(val)

def form_json(filename: str) -> json:
    ubl_dict = conv_xml_to_dict(filename)
    output = {
        'InvoiceID': get_ID(ubl_dict),
        'InvoiceTaxSchemeID': get_InvoiceTaxSchemeID(ubl_dict),
        'InvoiceName': get_InvoiceName(ubl_dict),
        'IssueDate': get_IssueDate(ubl_dict),
        'PayableAmount': get_PayableAmount(ubl_dict),
        'InvoiceQuantity': get_InvoiceQuantity(ubl_dict),
        'Currency': get_Currency(ubl_dict) ,
        'PaymentTerms': get_PaymentTerms(ubl_dict),
        'TaxAmount': get_TaxAmount(ubl_dict),
        'TaxableAmount': get_TaxableAmount(ubl_dict),
        'TaxExclusiveAmount': get_TaxExclusiveAmount(ubl_dict),
        'TaxInclusiveAmount': get_TaxInclusiveAmount(ubl_dict),
        'TaxSchemeID': get_TaxSchemeID(ubl_dict),
        'SupplierRegistration': get_SupplierRegistration(ubl_dict),
        'SupplierStreet': get_SupplierStreet(ubl_dict),
        'SupplierCity': get_SupplierCity(ubl_dict),
        'SupplierPost': get_SupplierPost(ubl_dict),
        'SupplierCountry': get_SupplierCountry(ubl_dict),
        'CustomerRegistration': get_CustomerRegistration(ubl_dict),
        'CustomerStreet': get_CustomerStreet(ubl_dict),
        'CustomerCity': get_CustomerCity(ubl_dict),
        'CustomerPost': get_CustomerPost(ubl_dict),
        'CustomerCountry': get_CustomerCountry(ubl_dict)
    }
    return output
