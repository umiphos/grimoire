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


Setting the same value to a list of fields
==========================================

Let's say that we have an object and we want to set a series of fields, then you probably are going to make a loop
and acces for all the elements like 

for field in fields:
    setattr(object, field, 'value')

This setattr can be done throught odoo with object._cache[field] = 'value'

This is just to keep the things the odoo-way


Domain for a field Many2one filtered by Many2Many
=================================================

If you need to make a filter based on another field that has many ids(many2many)
yo need to make the domain as follows

https://www.odoo.com/fr_FR/forum/aide-1/question/problem-with-domain-on-view-how-to-filter-this-127579
in the python
many2many_field fields.Many2many('my_module')


in the XML
<field name="to_filter" domain="[('id', '=', many2many_field and many2many_field[0] and many2many_field[0][2] or False)]"/>


Remove a group from an existing menuitem
=========================================

https://www.odoo.com/forum/help-1/question/hide-menu-for-existing-group-18704
The idea is to allow a menuitem to be used for any group or an specific group

```xml
<record id="original_module.menu_id" model="ir.ui.menu">
    <field name="groups_id" eval="[(3,ref('my_new_group_id'))]"/>
</record>
```


Create filters and group by in view
======================================

It's pretty simple, in this example I'm going to use the account_invoice view.

```xml
<record id="view_account_invoice_filter_inherit" model="ir.ui.view">
    <field name="name">account.invoice.filter.inherit</field>
    <field name="model">account.invoice</field>
    <field name="inherit_id" ref="account.view_account_invoice_filter"/>
    <field name="arch" type="xml">
        <xpath expr="//search" position="inside">
            <filter name="l10n_pe_edi_document_type_invoice" string="Invoices" domain="[('l10n_pe_edi_document_type','=', '01')]"/>
            <filter name="l10n_pe_edi_document_type_ticket" string="Tickets" domain="[('l10n_pe_edi_document_type','=', '03')]"/>
        </xpath>
        <xpath expr="//group" position="inside">
            <filter name="journal_group" string="Journal" context="{'group_by':'journal_id'}"/>
        </xpath>
    </field>
</record>
```
What we do here is 2 thinks, we add a new filter by the document type, actually we add 2 of them.

The second part, in the group, it's meanth to group by the field I want it to be grouped, it's simple, but usually we miss this kind of examples.

How to add a favorite in odoo view?
======================================

This example is pretty simple, we are using a filter to add a favorite to the view.
Also, this favorite is the default one.

```xml
<record id="myfavorite_filter" model="ir.filters">
    <field name="name">My favorite</field>
    <field name="model_id">account.invoice</field>
    <field name="user_id" eval="False"/>
    <field name="is_default">True</field>
    <field name="domain" eval="[]"/>
    <field name="context">{'group_by':'journal_id'}</field>
</record>
```

I'm just grouping the journals by default, but it's pretty simple to make this filters
For more options, check odoo/odoo/addons/base/models/ir_filters.py
