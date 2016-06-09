import os
import glob
print (os.getcwd())

# http://www.diveintopython3.net/comprehensions.html

examples_path = '/Dropbox/Advanced_python_course/week_2/examples'
os.makedirs(examples_path, exist_ok=True)

os.chdir(examples_path)
print (os.getcwd())

pathname = (os.path.join(examples_path, 'harblar.py'))

print (pathname)

splitted = os.path.split(pathname)

print (splitted[0])

hurr = os.path.splitext('hablar.py')

os.chdir('/Dropbox/Advanced_python_course/week_2/')

glob_xml = glob.glob('examples/*.xml')
glob_test = glob.glob('*test*.py')
glob_py = glob.glob('examples/*.py')

print (glob_py)


