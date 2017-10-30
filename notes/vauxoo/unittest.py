"""
This one also don't require a full documentation, is just the notes that we see on the videos.
"""
##################COMMENTS





touch my-modules/openacademy/tests/openacademy_course_test.py

touch my-modules/openacademy/tests/__init__.py
vim   my-modules/openacademy/tests/__init__.py
    from . import openacademy_course_test.py

We need to re name the files, because it will not be processed if it does not start with test_

mv my-modules/openacademy/tests/openacademy_course_test.py my-modules/openacademy/tests/test_openacademy_course.py



echo """filetype plugin indent on
set tabstop=4
set shiftwidth=4
set expandtab
""" > ~/.vimrc

After creating the demo we must create a new database:
    createdb odoo_curso_wdemo

python /home/odoo/odoo/odoo.py -d odoo_curso_wdemo --addons-path=/home/odoo/my-modules/,/home/odoo/odoo/addons 
python /home/odoo/odoo/odoo.py -d odoo_curso_wdemo --addons-path=/home/odoo/my-modules/,/home/odoo/odoo/addons -i openacademy
python /home/odoo/odoo/odoo.py -d odoo_curso_wdemo --addons-path=/home/odoo/my-modules/,/home/odoo/odoo/addons -u  openacademy --test-enable --log-level=debug
python /home/odoo/odoo/odoo.py -d odoo_curso_wdemo --addons-path=/home/odoo/my-modules/,/home/odoo/odoo/addons -u  openacademy --test-enable --log-level=debug --stop-after-init
python /home/odoo/odoo/odoo.py -d odoo_curso_wdemo --addons-path=/home/odoo/my-modules/,/home/odoo/odoo/addons -u  openacademy --test-enable --log-level=info --stop-after-init



import pdb;pdb.set_trace() #what is this?
# -*- coding: utf-8 -*-
