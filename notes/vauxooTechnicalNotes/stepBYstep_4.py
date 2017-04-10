"""
Grettings:
The dinamic of this document will change, and probably a change will be made to the older files... 
First change: everything is on english now... provably will change it or something... we don't know jet...
Second: Bugs as been moved to another file, because is useless to have the bugs on each file, so we are putting all those lovely bugs on one bag :)
Third: We estart adding the #commit because we really need to know what we commited and where
    #commitDocker <fileName> 
    
Last: The EOD(end of day) at the...well at the end of the day.
Forth: Useful commands is going to be moved to another file, and will have a commads by day. It's going to be moved at the end of the videos, so right now it stays on this document.
The section Comments by time is going to stay, it's somehow useful...until now at least
Step by step is is the main reason of this document, so right now this comment is to high light it....


This new and shinning  brackets means that we are updating a line for another new line...
IN EXAMPLE!
    <this OldLabel/>
    uuu[
        <this newLabel>
    uuu]
The lines before the brackets mean that they are the old ones, the brackets on the inside means that is the new one :).
"""
##################COMMENTS BY TIME
<0:10> comentario sobre cuales son las propiedades de los botones

##################STEP BY STEP SECTION
@workflows
@workflows.workflowAlmost
"""We just add a new decorator for this comments, before each block we need to add what field, property or class it will create
#vim /home/odoo/my-modules/openacademy/model/openacademy_session.py
+++[    
    #workflows
    state = fields.Selection([
        ('draft', "Draft"),
        ('confirmed', "Confirmed"),
        ('done', "Done"),
    ], default='draft')
+++]
+++[Each one of this decorators are part of a label we use to navigate. Remember the Undefined and the Backlog on Vauxoo? well, this is a way they are done :).    
    #at the EOF
    #According to Nhomar, we need to change the @api.one to @api.multi, we don't know why just jet, but that explains why the code on Moy's videos is diferent sometime with the code on the current documentation.

    @api.multi
    def action_draft(self):
        self.state = 'draft'

    @api.multi
    def action_confirm(self):
        self.state = 'confirmed'

    @api.multi
    def action_done(self):
        self.state = 'done'
+++]

#vim /home/odoo/my-modules/openacademy/view/openacademy_session_view.xml

<form string="Session Form">
+++[
<header>
    <!--Work Flow-->
    <button name="action_draft" type="object"
        string="Reset to draft"
        states="confirmed,done"/>
    <button name="action_confirm" type="object"
        string="Confirm" states="draft"
        class="oe_highlight"/>
        <button name="action_done" type="object"
            string="Mark as done" states="confirmed"
            class="oe_highlight"/>
        <field name="state" widget="statusbar"/>
</header>
+++]
"""


@workflows.workflow
"""
#vim /home/odoo/my-modules/openacademy/__openerp__.py
'data': [
+++[
'views/session_workflow.xml',
+++]



#vim /home/odoo/my-modules/openacademy/model/openacademy_session.py
], default='draft')
ooo[
    ])
ooo]

#vim /home/odoo/my-modules/openacademy/view/openacademy_session_view.xml
<button name="action_draft" type="object"
<button name="action_confirm" type="object"
<button name="action_done" type="object"

ooo[
    <button name="draft" type="workflow"
    <button name="confirm" type="workflow"
    <button name="done" type="workflow"
ooo]

---ass! we can see, there are two changes, on the name, there is no 'action', and on the type there is no object, there are workflows now.
---This round of comments are sponsored by Arturo of the future...by the time you are reading this he might be 'Arturo from the past', but, that's just a concept.
---ok, this is Arturo from the future, the one in the morning after the previous note.... be sure that the names of each button are the same on the functions we are calling on the workflow/file.xml and I'm guessig here, but they must be relationed with the py names...just guessing here....
---jajajaja *laughts in spanish*...this is Arturo from the more future that the comment before me... so, in <2:03:45> Moy is about to explain why the f*ck is not going to work the little red button, you remember him? the one that makes the transition between (o-Draft->Confirmed->Done-o)...yeah I actually watched 2 hour of the video to find this comment of Moy, so future Arturo, be kind to this(now old to you) version of you...

---this step is a middle step between what moy says in the video and what actually we must do according to the backend odoo tutorial

#mkdir /home/odoo/my-modules/openacademy/workflow
#touch /home/odoo/my-modules/openacademy/workflow/openacademy_session_workflow.xml
#vim   /home/odoo/my-modules/openacademy/workflow/openacademy_session_workflow.xml

---we add all this to the new file
++[
<?xml version="1.0" encoding="UTF-8"?>
<openerp>
    <data>
        <record model="workflow" id="wkf_session">
            <field name="name">OpenAcademy sessions workflow</field>
            <field name="osv">openacademy.session</field>
            <field name="on_create">True</field>
        </record>

        <record model="workflow.activity" id="draft">
            <field name="name">Draft</field>
            <field name="wkf_id" ref="wkf_session"/>
            <field name="flow_start" eval="True"/>
            <field name="kind">function</field>
            <field name="action">action_draft()</field>
        </record>
        <record model="workflow.activity" id="confirmed">
            <field name="name">Confirmed</field>
            <field name="wkf_id" ref="wkf_session"/>
            <field name="kind">function</field>
            <field name="action">action_confirm()</field>
        </record>
        <record model="workflow.activity" id="done">
            <field name="name">Done</field>
            <field name="wkf_id" ref="wkf_session"/>
            <field name="kind">function</field>
            <field name="action">action_done()</field>
        </record>

        <record model="workflow.transition" id="session_draft_to_confirmed">
            <field name="act_from" ref="draft"/>
            <field name="act_to" ref="confirmed"/>
            <field name="signal">confirm</field>
        </record>
        <record model="workflow.transition" id="session_confirmed_to_draft">
            <field name="act_from" ref="confirmed"/>
            <field name="act_to" ref="draft"/>
            <field name="signal">draft</field>
        </record>
        <record model="workflow.transition" id="session_done_to_draft">
            <field name="act_from" ref="done"/>
            <field name="act_to" ref="draft"/>
            <field name="signal">draft</field>
        </record>
        <record model="workflow.transition" id="session_confirmed_to_done">
            <field name="act_from" ref="confirmed"/>
            <field name="act_to" ref="done"/>
            <field name="signal">done</field>
        </record>
    </data>
</openerp>
+++]

#It's not too much to explain here, except this:
    if you can see, each label record has a name,those id exist on their python file:
        draft,confirmed,done where declared before on the other exercise, so be careful of naming this.
        the transitions appers to be 
"""

#GIT COMMIT 'Workflow'
#DOCKER COMMIT

###At this point we fixed the previous code, and is 'working' right now.
#moving on
#funny thing, when you trigger 2 alerts the app goes nuts...just for the record...


@workflows.automaticTransitions
"""
#vim   /home/odoo/my-modules/openacademy/workflow/openacademy_session_workflow.xml
+++[#EOF
<!--Automatic Transition-->
<record model="workflow.transition" id="session_auto_confirm_half_filled">
    <field name="act_from" ref="draft"/>
    <field name="act_to" ref="confirmed"/>
    <field name="condition">taken_seats &gt; 50</field>
</record>
+++]

"""
@workflows.serverActions
"""
#vim   /home/odoo/my-modules/openacademy/workflow/openacademy_session_workflow.xml
---ok... we are going to update every line of those who are "workflow.activity" with this two new blocks for each.

ooo[
        <record model="ir.actions.server" id="set_session_to_draft">
            <field name="name">Set session to Draft</field>
            <field name="model_id" ref="model_openacademy_session"/>
            <field name="code">
                model.search([('id', 'in', context['active_ids'])]).action_draft()
            </field>
        </record>
        <record model="workflow.activity" id="draft">
            <field name="name">Draft</field>
            <field name="wkf_id" ref="wkf_session"/>
            <field name="flow_start" eval="True"/>
            <field name="kind">dummy</field>
            <field name="action"></field>
            <field name="action_id" ref="set_session_to_draft"/>
        </record>

        <record model="ir.actions.server" id="set_session_to_confirmed">
            <field name="name">Set session to Confirmed</field>
            <field name="model_id" ref="model_openacademy_session"/>
            <field name="code">
                model.search([('id', 'in', context['active_ids'])]).action_confirm()
            </field>
        </record>
        <record model="workflow.activity" id="confirmed">
            <field name="name">Confirmed</field>
            <field name="wkf_id" ref="wkf_session"/>
            <field name="kind">dummy</field>
            <field name="action"></field>
            <field name="action_id" ref="set_session_to_confirmed"/>
        </record>

        <record model="ir.actions.server" id="set_session_to_done">
            <field name="name">Set session to Done</field>
            <field name="model_id" ref="model_openacademy_session"/>
            <field name="code">
                model.search([('id', 'in', context['active_ids'])]).action_done()
            </field>
        </record>
        <record model="workflow.activity" id="done">
            <field name="name">Done</field>
            <field name="wkf_id" ref="wkf_session"/>
            <field name="kind">dummy</field>
            <field name="action"></field>
            <field name="action_id" ref="set_session_to_done"/>
        </record>
ooo]

---Testet and working :)... and that happends when we are big boys, we try to walk alone and we fuck a whole day... at least we almost finish chapter 4...part 1...
"""

@security
@security.accessRights
"""
#mkdir /home/odoo/my-modules/openacademy/security
#touch /home/odoo/my-modules/openacademy/security/ir.model.access.csv
#vim   /home/odoo/my-modules/openacademy/security/ir.model.access.csv
+++[
id,name,model_id/id,group_id/id,perm_read,perm_write,perm_create,perm_unlink
course_manager,course manager,model_openacademy_course,group_manager,1,1,1,1
session_manager,session manager,model_openacademy_session,group_manager,1,1,1,1
course_read_all,course all,model_openacademy_course,,1,0,0,0
session_read_all,session all,model_openacademy_session,,1,0,0,0
+++]


#vim   /home/odoo/my-modules/openacademy/__openerp__.py
'data':[
+++[
    'security/ir.model.access.csv',
+++]

#touch  /home/odoo/my-modules/openacademy/security/security.xml
#vim    /home/odoo/my-modules/openacademy/security/security.xml
+++[
<?xml version="1.0" encoding="UTF-8"?>
<openerp>
    <data>
        <record id="group_manager" model="res.groups">
            <field name="name">OpenAcademy / Manager</field>
        </record>
    </data>
</openerp>
+++]
"""
@security.recordRules
"""
#vim    /home/odoo/my-modules/openacademy/security/security.xml
+++[
    <record id="only_responsible_can_modify" model="ir.rule">
        <field name="name">Only Responsible can modify Course</field>
        <field name="model_id" ref="model_openacademy_course"/>
        <field name="groups" eval="[(4, ref('openacademy.group_manager'))]"/>
        <field name="perm_read" eval="0"/>
        <field name="perm_write" eval="1"/>
        <field name="perm_create" eval="0"/>
        <field name="perm_unlink" eval="1"/>
        <field name="domain_force">
            ['|', ('responsible_id','=',False),
                  ('responsible_id','=',user.id)]
        </field>
    </record>
+++]
To know where the 4 in groups comes...check V4.2 <0:58>
"""



@wizards
@wizards.defining
"""
#mkdir /home/odoo/my-modules/openacademy/wizard
#touch /home/odoo/my-modules/openacademy/wizard/openacademy_wizard.py
#touch /home/odoo/my-modules/openacademy/wizard/__init__.py
#vim /home/odoo/my-modules/openacademy/wizard/openacademy_wizard.py
+++[
# -*- coding: utf-8 -*-

from openerp import models, fields, api

class Wizard(models.TransientModel):
    _name = 'openacademy.wizard'

    session_id = fields.Many2one('openacademy.session',
        string="Session", required=True)
    attendee_ids = fields.Many2many('res.partner', string="Attendees")
+++]



#vim   /home/odoo/my-modules/openacademy/__init__.py
+++[
from . import wizard
+++]
#vim   /home/odoo/my-modules/openacademy/wizard/__init__.py
+++[
from . import openacademy_wizard
+++]
"""
@wizards.launching
"""
#touch   /home/odoo/my-modules/openacademy/view/openacademy_wizard_view.xml
#nano   /home/odoo/my-modules/openacademy/view/openacademy_wizard_view.xml
+++[
<?xml version="1.0" encoding="UTF-8"?>
<openerp>
    <data>
        <record model="ir.ui.view" id="wizard_form_view">
            <field name="name">wizard.form</field>
            <field name="model">openacademy.wizard</field>
            <field name="arch" type="xml">
                <form string="Add Attendees">
                    <group>
                        <field name="session_id"/>
                        <field name="attendee_ids"/>
                    </group>
                </form>
            </field>
        </record>
        <act_window id="launch_session_wizard"
                    name="Add Attendees"
                    src_model="openacademy.session"
                    res_model="openacademy.wizard"
                    view_mode="form"
                    target="new"
                    key2="client_action_multi"
        />
    </data>
</openerp>
+++]

#nano /home/odoo/my-modules/openacademy/__openerp__.py
data:[
+++[
'view/openacademy_wizard_view.xml',

+++]
"""
@wizards.launching.addingButtons
"""
#nano   /home/odoo/my-modules/openacademy/view/openacademy_wizard_view.xml
+++[
<footer>
        <button name="subscribe" type="object"
        string="Subscribe" class="oe_highlight"/>
        or
        <button special="cancel" string="Cancel"/>
    </footer>
</form>
+++]

#vim /home/odoo/my-modules/openacademy/wizard/openacademy_wizard.py
+++[
    @api.multi
    def subscribe(self):
        self.session_id.attendee_ids |= self.attendee_ids
        return {}
+++]
"""
@wizards.launching.addingMultipleAttendees
"""
#vim /home/odoo/my-modules/openacademy/wizard/openacademy_wizard.py

    session_id = fields.Many2one('openacademy.session',
        string="Session", required=True)
ooo[
    def _default_sessions(self):
        return self.env['openacademy.session'].browse(self._context.get('active_ids'))

    session_ids = fields.Many2many('openacademy.session',
        string="Sessions", required=True, default=_default_sessions)
    attendee_ids = fields.Many2many('res.partner', string="Attendees")
ooo]

  @api.multi
    def subscribe(self):
        self.session_id.attendee_ids |= self.attendee_ids
        return {}

ooo[
    @api.multi
    def subscribe(self):
        for session in self.session_ids:
            session.attendee_ids |= self.attendee_ids
        return {}
ooo]






"""
Future me,please follow the last two tutorials, the security and wizard, they are really easy to do.



##################USEFUL COMMANDS SECTION
ln -sf
on vid 2 <0:22:00> we can see the best way to do this :D
##################BUGS SECTION
#2017-02-02 17:47:10,971 889 ERROR odoo_curso openerp.sql_db: bad query: UPDATE "im_chat_presence" SET "status"='away',"last_poll"='2017-02-02 17:47:10',"write_uid"=1,"write_date"=(now() at time zone 'UTC') WHERE id IN (1)
#Traceback (most recent call last):
#  File "/home/odoo/odoo/openerp/sql_db.py", line 234, in execute
#    res = self._obj.execute(query, params)
#TransactionRollbackError: could not serialize access due to concurrent update
"""
We currently don't know what the hell is this...we will keep you posted...
"""

2017-02-03 01:48:38,437 141 INFO odoo_curso openerp.addons.report.models.report: You need Wkhtmltopdf to print a pdf version of the reports.
2017-02-03 01:48:38,556 141 INFO odoo_curso openerp.http: HTTP Configuring static files
2017-02-03 01:48:38,626 141 CRITICAL odoo_curso openerp.service.server: Failed to initialize database `odoo_curso`.
---we  need to read more in the errors not the error itself....
SOLUTION
sudo add-apt-repository ppa:pov/wkhtmltopdf
sudo apt-get update
sudo apt-get install wkhtmltopdf 

---rgrep utf-9 and modify the one with the fkn problem...30 minutes was the time of this, and my rejection to adopt rgrep...thanks little problem, is now my base searcher of bugs....



# Line 1 : No matching record found for external id 'group_manager' in field 'Group'


_______________________-
2017-02-03 19:03:32,541 1377 ERROR odoo_curso openerp.sql_db: bad query: delete from wkf_workitem where id=1491
Traceback (most recent call last):
  File "/home/odoo/odoo/openerp/sql_db.py", line 234, in execute
    res = self._obj.execute(query, params)
TransactionRollbackError: could not serialize access due to concurrent update

This bug is because we were making updates on the actions of the draft-->done and that....we really don't know, probably some old relation between versions and caused this crash
