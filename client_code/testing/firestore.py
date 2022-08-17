from ..firebase_client import firestore as fs
from ..firebase_client import authentication as auth
from datetime import datetime

"""Read Data from Firestore"""
def get_multiple_documents():
  query = fs.db.collection('test').limit(1000)
  docs = fs.get_docs(query)
  return docs
  
def get_single_document():
  doc_ref = fs.db.collection('test').doc('doc_uid')
  doc = fs.get_doc(doc_ref)
  return doc


"""Write Data"""
def add_document():
  doc_ref = fs.db.collection('test')
  data = {'_id': 'öaksdjflöasdjflöasdkfjöalksdfjölasdf', 'transaction_details': None, 'given_money': 0, 'transaction_id': None, 'shop_uid': '6BVygdTmsLB6mqwR4L4c', 'total_sum_incl': 0, 'company_uid': 'HmtJvWK74DbV0tWNrbyy', 'employee_uid': 'd7y9Unjvnk0H9aqBh6op', 'uid': None, 'articles': [], 'total_sum_excl': 0, 'payment_items':{'id': 'cash', 'name': 'cash', 'amount': 0, 'currency': 'EUR'}, 'is_payment_valid': True, 'vat_rates': [], 'payment_option': None, 'shop_name': 'Filiale Dorfplatz', 'able_to_sign': True, 'created': True, 'tip': 10, 'zs_count': 0, 'payment_failed': False, 'ft_response': {'ftSignatures': [], 'ftQueueID': '4caa8012-71dc-4ab0-8b5a-d00e9bc551f8', 'ftCashBoxIdentification': 'fiskaltrust2', 'cbTerminalID': '1', 'ftCashBoxID': '7ebd10a6-ee2d-4558-8131-acf10a2dec1a', 'ftState': '4707387510509010944', 'ftReceiptIdentification': 'ftBE3#', 'ftQueueRow': '3044', 'ftQueueItemID': '8dbb27af-d6ce-4d1c-8721-3454b1ebed49', 'cbReceiptReference': '2'}, 'able_to_print': False, 'total_sum_discounted_excl': 0, 'retour_money': 0, 'cancelled': False, 'isodate': '2022-03-29', 'pos_name': 'Kassa1 Neueste Filiale', 'ft_cancel_response': None, 'pos_uid': 'vEv4bb2PVjqXbvJBjts0', 'receipt_case': 'zero', 'total_sum_discounted_incl': 0, 'able_to_save': True, 'version': 3, 'discount': 0, 'timestamp': 13245345, 'employee_name': 'Cornelius Blank', 'table_uid': None, 'cancel_reason': '', 'from_order': None, 'cycle_time_seconds': 605, 'company': {'rechnungstext': 'Die Rechnung wird per Einzug beglichen. Danke!', 'text_order': 'Danke für eure Bestellung! ', 'fax': '', 'date_bis': None, 'einsatz_tags': None, 'kassa_pin': '1234', 'mobil': '+43 664 12345', 'price_label_config': {'color': [-45, -150, None], 'price_type': 'normal', 'price_date': '2021-12-30', 'font_color': 'white'}, 'plz': 6789, 'logo': 'https://firebasestorage.googleapis.com/v0/b/markone-qa.appspot.com/o/HmtJvWK74DbV0tWNrbyy%2Flogo.jpeg?alt=media&token=9d7c3fb2-dbaf-4d6d-a268-7dcd6d44d43f', 'holidays': [], 'posChangeAmount': 500, 'requests': None, 'bank': 'Raiffeisen Monfort', 'strasse': 'Dorfstraße 34', 'bank2': 'Volksbank Salzburg', 'allergene_tags': None, 'ort': 'Musterdorf', 'date_von': None, 'article_cache': None, 'iban2': 'AT45 5432 2134 1223', 'article_tags': None, 'country_code': '', 'uid_number': 'AT123456', 'fibu_tags': None, 'company_lfs_text': 'None', 'production_print_settings': {'tafelplan': 0, 'ofenplan': 0, 'mischplan': 3}, 'festnetz': '05572 58062', 'kassa_pin_settings': '1234', 'land': 'Österreich', 'label_config': {'include_logo': True, 'label_format': '60_40', 'price_type': 'normal', 'price_date': '2022-03-17', 'hide_price': False}, 'bic': 'RVVGAT2B422', 'url': '', 'Name': 'Muster Bakery', 'dsgvo_text': None, 'iban': 'AT254571000101002076', 'warengruppe_tag': None, 'bestellgruppen_tags': None, 'owner': None, 'open_hours': [True, True, True, True, True, True, True], 'company_mail': 'muster@bakery.com', 'bic2': 'VolsB4dssdsdsdsdsdsd5645'}}
  fs.add_doc(doc_ref,data)


"""Listeners"""
def callback_test(data):
  print('callback test triggered')
  
def add_listener():
  query = fs.db.collection('test').limit(50)
  listener = fs.add_listener(query,callback_test)
  return listener
