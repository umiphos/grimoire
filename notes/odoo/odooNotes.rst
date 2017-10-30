References
# http://stackoverflow.com/questions/42686674/odoo-search-domain-filter-with-multiple-values

UPDATE employee SET name="ArturoF" WHERE id=18 OR id=19 id=21;
self.env.cr.execute("UPDATE employee SET name="ArturoF" WHERE id IN(18,19,21);")
search = self.env['employee'].search(['|','|',('id', '=', '18'),('id','=','19'),('id','=','21')])
for items in search: 
	items.name = "ArturoF"

DELETE FROM employee WHERE id=19 OR id=21;
self.env.cr.execute("DELETE FROM employee WHERE id=19 OR id=21;")
self.env['employee'].search(['|',('id', '=', '19'),('id','=','21')])

SELECT id, name FROM employee WHERE id=18;
self.env.cr.execute("SELECT id, name FROM employee WHERE id=18;")
env.['employee'].search([('id', '=', 18)])
self.env.cr.fetchall()




