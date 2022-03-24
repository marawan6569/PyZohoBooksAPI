from PyZohoBooksAPI import ZohoAuth, Contacts, Invoices

# auth = ZohoAuth(
#     client_id='1000.GD6CJ7MWC8AWC6CZI1ZL474UYURQXS',
#     client_secret='ab74c6e5565fd99fdee9e40b364cd960941c4529da'
# )

# print(auth.generate_token(code='1000.c8a9c216a67f7ae988f3c706a547dfa4.9b799eda80b7839310ef35c56e46bb23'))
# print(auth.refresh_token(refresh_token='1000.455b2011ed031afa48df852cfcfe7f9b.0aeb72a01ad1841ccbf5df8e548f9445'))


# contacts = Contacts(token='1000.ce1d8d22982db8d5c80ea8c8903ca458.b53a0d99b4b0325f4ff554a8a452a92b',
#                     organization_id='774525475')

# _, cl = contacts.contacts_list()
# print(_, cl)

# _, contact = contacts.get_contact(contact_id='3168296000000075177')
# print(_, contact)


# _, contact = contacts.check_by_email(email='marawan6569@gmail.com')
# print(_, contact)


# _, contact = contacts.create_contact(contact_data={'contact_name': 'ahmed mohamed'})
# print(_, contact)

# invoices = Invoices(token='1000.974b30cc15660e53a11904fca98066ea.607e25ecd3f226ff0484960dd020e74e',
#                     organization_id='774525475')

# invoice = invoices.create_invoice(invoice_data={
#     "invoice_number": "test-000001",
#     "customer_id": "3168296000000075177",
#     "line_items": [
#         {
#             "item_id": "3168296000000075168",
#         }
#     ]
# })

# invoice = invoices.email_an_invoice(invoice_id='3168296000000089012', email_data={
#     'to_mail_ids': ['marawan6569@gmail.com'],
#     'subject': 'Invoice from catdogmail.live Inc ',
#     'body': '<h1>Thank uou ;)</h1>'
# })
# print(invoice)
