"""
Not too much to add, this last part is kinda easy.
We add a plain Comments section.
"""
##################COMMENTS


##################STEP BY STEP SECTION
#We are kinda...confused...so most of chapter 5 it isn't on the terminal...es on the graphic interface...sooo..here we go

add a new directory i18n


Adding a language
#Settings-->
    #Load a Translation(select the one you need)
#Reload the server.


Changing language to a user
On setting-->Users
    Select the one you need
        Edit
            Preferences
                Select the language you need


:q
Updating the terms of the application
On settings--> Sync terms

How to create my own dictionary and edditing existing terms
On settings--> Translated Terms
    -->Advanced search (translated field + contains + openacademy)

Once you modified all the fields you can import/export that file:
On settings--> Translations
    Export Translation
        (Select the language you need),
        (Select the file format to export),
        (Write the name of the modules you want to export)

About this... we had a problem... we really don't know what happend... so really we need this to add it to the bug section but we at this point.... it all happend when we follow all the above steps...if we
    just add in the importation, then we can actually make it work.

Instead of making a GUI translation, you can export that module translation and edit the plain text. I'm not going to add those steps here...

The next step is adding the _ function that makes the translations.... we... we actually don't know how it works right now, so, I own you an explanation for later.....


On every python file on model we search for the  string messages and then... just do this:
    message = "this untranslated text" --->message = _("this untranslated text")
Also you need to add it on the openerp import.
Once this is done the translate messages will appear on the "Sync terms" and under "Translated terms"...

Sorry if you are reading this and at this point and forward it doesn't make any sense... but we are in a hurry.




@Reporting
@Reporting.printedReports
"""
#Edit __openerp__.py
+
'report/openacademy_session_report.xml',


#create and edit /report/openacademy_session_report.xml
<openerp>
    <data>
        <report
            id="report_session"
            model="openacademy.session"
            string="Session Report"
            name="openacademy.report_session_view"
            file="openacademy.report_session"
            report_type="qweb-pdf" />

        <template id="report_session_view">
            <t t-call="report.html_container">
                <t t-foreach="docs" t-as="doc">
                    <t t-call="report.external_layout">
                        <div class="page">
                            <h2 t-field="doc.name"/>
                            <p>From <span t-field="doc.start_date"/> to <span t-field="doc.end_date"/></p>
                            <h3>Attendees:</h3>
                            <ul>
                                <t t-foreach="doc.attendee_ids" t-as="attendee">
                                    <li><span t-field="attendee.name"/></li>
                                </t>
                            </ul>
                        </div>
                    </t>
                </t>
            </t>
        </template>
    </data>
</openerp>
"""


#####NOTE BIG NOTE HERE!
"""
ok, so this is the story, by defauld wkhtmltopdf install the old 9.9 version, so you need to install the newer version... if you are new to source... you need this link.
http://askubuntu.com/questions/556667/how-to-install-wkhtmltopdf-0-12-1-on-ubuntu-server
sudo apt-get install xvfb
wget http://download.gna.org/wkhtmltopdf/0.12/0.12.2.1/wkhtmltox-0.12.2.1_linux-trusty-amd64.deb
sudo dpkg -i wkhtmltox-0.12.2.1_linux-trusty-amd64.deb
In case there is an error, use the next command
sudo apt-get -f install
"""




"""
Then we add this to the same file....

<?xml version="1.0" encoding="UTF-8"?>
<openerp>
    <data>
        <!--paper format-->
        <record id="paperformat_us" model="report.paperformat">
            <field name="name">US Letter</field>
            <field name="default" eval="True" />
            <field name="format">Letter</field>
            <field name="page_height">0</field>
            <field name="page_width">0</field>
            <field name="orientation">Portrait</field>
            <field name="margin_top">40</field>
            <field name="margin_bottom">20</field>
            <field name="margin_left">7</field>
            <field name="margin_right">7</field>
            <field name="header_line" eval="False" />
            <field name="header_spacing">35</field>
            <field name="dpi">90</field>
        </record>
        <!--report definition-->
        <report
            id="report_session"
            model="openacademy.session"
            string="Session Report"
            name="openacademy.report_session_view"
            file="openacademy.report_session"
            report_type="qweb-pdf"
        />
        <!--adding paperformat to the report action itself-->
        <record id="report_session" model="ir.actions.report.xml">
            <field name="paperformat_id" ref="openacademy.paperformat_us"/>
        </record><!--report template-->
        <template id="report_session_view">
            <t t-call="report.html_container">
                <t t-foreach="docs" t-as="doc">
                    <t t-call="report.external_layout">
                        <div class="page">
                            <h2 t-field="doc.name"/>
                            <h2 t-field="doc.course_id.name"/>
                            <p>From <span t-field="doc.start_date"/> to <span
                                t-field="doc.end_date"/></p>
                            <h3>Attendees:</h3>
                            <ul>
                                <t t-foreach="doc.attendee_ids" t-as="attendee">
                                    <li><span t-field="attendee.name"/>
                                        <ul>
                                            <li><span t-field="attendee.email"/></li>
                                        </ul>
                                    </li>
                                </t>
                            </ul>
                        </div>
                    </t>
                </t>
            </t>
        </template>
    </data>
</openerp>
"""

@Reporting.dashboards
"""
#vim view/__openerp__.py
'depends':['base','board'],

'views/openacademy_session_board.xml',


<?xml version="1.0"?>
<openerp>
    <data>
        <record model="ir.actions.act_window" id="act_session_graph">
            <field name="name">Attendees by course</field>
            <field name="res_model">openacademy.session</field>
            <field name="view_type">form</field>
            <field name="view_mode">graph</field>
            <field name="view_id"
                   ref="openacademy.openacademy_session_graph_view"/>
        </record>
        <record model="ir.actions.act_window" id="act_session_calendar">
            <field name="name">Sessions</field>
            <field name="res_model">openacademy.session</field>
            <field name="view_type">form</field>
            <field name="view_mode">calendar</field>
            <field name="view_id" ref="openacademy.session_calendar_view"/>
        </record>
        <record model="ir.actions.act_window" id="act_course_list">
            <field name="name">Courses</field>
            <field name="res_model">openacademy.course</field>
            <field name="view_type">form</field>
            <field name="view_mode">tree,form</field>
        </record>

<record model="ir.ui.view" id="board_session_form">
            <field name="name">Session Dashboard Form</field>
            <field name="model">board.board</field>
            <!--<field name="type">form</field>-->
            <field name="arch" type="xml">
                <form string="Session Dashboard">
                    <board style="2-1">
                        <column>
                            <action
                                string="Attendees by course"
                                name="%(act_session_graph)d"
                                height="150"
                                width="510"/>
                            <action
                                string="Sessions"
                                name="%(act_session_calendar)d"/>
                        </column>
                        <column>
                            <action
                                string="Courses"
                                name="%(act_course_list)d"/>
                        </column>
                    </board>
                </form>
            </field>
        </record>
    <record model="ir.actions.act_window" id="open_board_session">
          <field name="name">Session Dashboard</field>
          <field name="res_model">board.board</field>
          <field name="view_type">form</field>
          <field name="view_mode">form</field>
          <field name="usage">menu</field>
          <field name="view_id" ref="board_session_form"/>
        </record>

        <menuitem
            name="Session Dashboard" parent="base.menu_reporting_dashboard"
            action="open_board_session"
            sequence="1"
            id="menu_board_session"/>

   </data>
</openerp>

"""

@webService
"""
mkdir my-modules/webservices
touch my-modules/web_services/ws_test.py
vim my-modules/web_services/ws_test.py


import xmlrpclib
import functools

HOST = 'localhost'
PORT = 8069
DB = 'odoo_curso'

USER = 'admin'
PASS = 'admin'
ROOT = 'http://%s:%d/xmlrpc/' % (HOST,PORT)

# 1. Login
uid = xmlrpclib.ServerProxy(ROOT + 'common').login(DB,USER,PASS)
print "Logged in as %s (uid:%d)" % (USER,uid)

call = functools.partial(
    xmlrpclib.ServerProxy(ROOT + 'object').execute,
    DB, uid, PASS)

# 2. Read the sessions
model = 'openacademy.session'
domain = []
method_name = 'search_read'
sessions = call(model, method_name, domain, ['name', 'seats', 'taken_seats'])
print "sessions",sessions




for session in sessions:
    print "Session %s (%s seats), taken seats %d" % (session['name'], session['seats'], session['taken_seats'])

method_name = 'search'
domain = [('name', '=', 'Curso Odoo 1')]#change me each time you need to add another course, it appears the constrain is not working...or it was part of session?
course_ids = call('openacademy.course', method_name, domain)
course_id = course_ids[0]
print "course_ids",course_ids


#method_name = 'create'
#course_id = call('openacademy.course', method_name, {'name': 'Curso Odoo 1'})




method_name = 'create'
responsible_id = call('res.partner', 'search', [('name', '=', 'Vauxoo')])[0]
print "responsible_id", responsible_id
new_sesion_id = call(model, method_name, {
    'name': 'Sesion from ws',
    'instructor_id': responsible_id,
    'course_id': course_id,
        #'attendee_ids': [(4, responsible_id)],
        'attendee_ids': [(4, 7), (4, 3)],
     })
print "new_sesion_id",new_sesion_id


"""


##################USEFUL COMMANDS SECTION

##################BUGS SECTION
2017-02-06 17:11:03,489 96 ERROR None openerp.http: Exception during JSON request handling.
Traceback (most recent call last):
  File "/home/odoo/odoo/openerp/http.py", line 544, in _handle_exception
    return super(JsonRequest, self)._handle_exception(exception)
  File "/home/odoo/odoo/openerp/http.py", line 1422, in _dispatch_nodb
    func, arguments = self.nodb_routing_map.bind_to_environ(request.httprequest.environ).match()
  File "/usr/local/lib/python2.7/dist-packages/werkzeug/routing.py", line 1430, in match
    raise NotFound()
NotFound: 404: Not Found
