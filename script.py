from xmlrpc import client

db = "odoo"
username = "cantine@cantine.fr"
password = "cantine"
url = "http://10.0.2.117:8069"

common = client.ServerProxy('{}/xmlrpc/2/common'.format(url))
uid = common.authenticate(db, username, password, {})

models = client.ServerProxy('{}/xmlrpc/2/object'.format(url))

id = models.execute_kw(db, uid, password, 'res.partner', 'create', [{
    'name': 'Azerty azertyuiop'

}])
models.execute_kw(db, uid, password,
    'res.partner', 'search_read',
    [[['is_company', '=', False], ['is_company', '=', True]]],
    {'fields': ['name', 'title', 'firstname'], 'limit': 5})
print(id)
