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


Dealing with many2many
===========================

This web has everything about widgets
==================================================
https://www.cybrosys.com/blog/many2many-fields-and-its-widgets-odoo

**In case the web dies, a summary from it's content:**

many2many widgets
many2many widget (default)

- many2many_tags widget
- many2many_checkboxes  widget
- many2many_kanban widget
- many2many_binary widget
- x2many_counter widget

**The simple way to add a many2many**

field_name = fields.Many2many('res.partner',string="many2many_default")
<field name="field_name"/>

Calling a server action from tests
======================================
If you are going to run a server action on_create or on_write and you need it for a test, you can always do it this way
server_action.run_action_code_multi(server_action, eval_context=dict({}, active_id=team_a.id, active_model='crm.team', env=self.env, record=team_a))

Another way to achive this is importing this
from odoo.tests import tagged

@tagged('post_install', '-at_install')
class MyClass()

Adding a nice search parameter for you want
==================================

Aparently is just an inherit of the filter/search view, after that we just make an xpath like this

<xpath expr="//search" position="inside">
<field name="your_field_to_search" string="Some random name" filter_domain="[('any_value_to_filter','ilike', self)]"/>
</xpath>

If you want to make other fields in the search, just add pipe | and then add any other value you want. Remember that the context value you are writing in the search field, is self.
