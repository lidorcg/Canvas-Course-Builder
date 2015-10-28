import os
from CanvasAPy import OAuth
import CanvasAPy

token = OAuth.get_token_from_file('token')
api = CanvasAPy.CanvasAPI('0.0.0.0:3000', token)

lid = api.Accounts.get(1)

crs_name = ""

for x in os.listdir('.'):
    if os.path.isdir(x) and x != 'CanvasAPy':
        crs_name = x

crs = lid.Courses.new({'name': crs_name})

os.chdir(crs_name)

mdls = os.listdir('.')
mdls.sort()

for m in mdls:
    mdl = crs.Modules.new({'name': m[3:]})
    os.chdir(m)
    lsns = os.listdir('.')
    lsns.sort()
    for l in lsns:
        pg = mdl.Pages.new(l[3:])
    os.chdir('..')


# ToDo prettify the code a bit
# ToDo add logging
