import os
from CanvasAPy import OAuth
import CanvasAPy


def create_course(acc):
    crs_name = ''
    for x in os.listdir('.'):
        if os.path.isdir(x):
            crs_name = x
    crs = acc.Courses.new({'name': crs_name})
    os.chdir(crs_name)
    create_modules(crs)


def create_modules(crs):
    modules = os.listdir('.')
    modules.sort()
    for m in modules:
        mdl = crs.Modules.new({'name': m[3:]})
        os.chdir(m)
        create_pages(mdl)
    os.chdir('..')


def create_pages(mdl):
    lessons = os.listdir('.')
    lessons.sort()
    for l in lessons:
        pg = mdl.Pages.new({'title': l[3:]})
        os.chdir(l)
        create_units(pg)
        pg.content.update()
    os.chdir('..')


def create_units(pg):
    units = os.listdir('.')
    units.sort()
    page_body = ''
    for u in units:
        page_body += new_section(u[3:])
    pg.content['body'] = page_body
    os.chdir('..')


def new_section(unt):
    section = """
    <h1>{}</h1>
    <p>
        Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aliquam rutrum tristique tincidunt. Vestibulum ante ipsum
        primis in faucibus orci luctus et ultrices posuere cubilia Curae; Vestibulum sit amet augue bibendum, ultricies
        elit vitae, scelerisque ipsum. Vivamus justo dolor, mollis at porttitor in, suscipit quis est. Praesent porta semper
        massa, non semper nunc dictum quis. Nulla fringilla fringilla hendrerit. Etiam in metus non metus rutrum molestie.
        Curabitur consectetur finibus molestie. Quisque lorem nunc, blandit a sodales in, mollis at nibh. Maecenas faucibus
        felis vel mauris semper, in suscipit felis rhoncus. Vestibulum sed leo in augue accumsan pretium. Etiam varius est
        eget erat ultrices eleifend sed eu mauris. Nulla tincidunt enim arcu, in consectetur orci imperdiet quis. Nullam ac
        mauris neque. Ut nec hendrerit dolor. In hac habitasse platea dictumst.
    </p><br>
    """.format(unt)
    return section


token = OAuth.get_token_from_file('token')
api = CanvasAPy.CanvasAPI('0.0.0.0:3000', token)

my_account = api.Accounts.get(1)

create_course(my_account)

# ToDo add logging
