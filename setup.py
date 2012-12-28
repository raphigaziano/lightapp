#~ 
#~ try:
    #~ from setuptools import setup
#~ except ImportError:
    #~ from distutils.core import setuptools
#~ 
#~ config = {
    #~ 'name': 'lightapp',
    #~ 'version': '0.1.0',
    #~ 'author': 'Raphi',
    #~ 'author_email': 'r.gaziano@gmail.com',
    #~ 'packages': ['lightapp', 'lightapp.tests'],
    #~ 'scripts': [], # any script in the bin directory
    #~ 'url': None,
    #~ 'download_url': None,
    #~ 'license': 'LICENSE.txt',
    #~ 'description': 'TODO',
    #~ 'long_description': open('README.txt').read(),
    #~ 'install_requires': [
    #~ ]
#~ }
#~ 
#~ setup(**config)

# -*- coding: utf-8 -*-
import sys

from cx_Freeze import setup, Executable

base = None
if sys.platform == "win32":
    base = "Win32GUI"

setup(
        name = "lightapp",
        version = "0.1",
        description = "blaaa",
        #~ options = {"build_exe": {"includes": ["sip"]} },
        executables = [Executable("main.py",
                       targetName='LightApp.exe',
                       copyDependentFiles=True,
                       base = base)])


#~ import sys, os
#~ from cx_Freeze import setup, Executable
 #~ 
#~ #############################################################################
#~ # préparation des options 
 #~ 
#~ # chemins de recherche des modules
#~ path = sys.path + ["lightapp", ]
 #~ 
#~ # options d'inclusion/exclusion des modules
#~ includes = []
#~ excludes = []
#~ packages = []
 #~ 
#~ # copier les fichiers et/ou répertoires et leur contenu
#~ includefiles = [("")]
#~ if sys.platform == "linux2":
    #~ includefiles += [(r"")]
#~ elif sys.platform == "win32":
    #~ includefiles += [(r"")]
#~ else:
    #~ pass
 #~ 
#~ # inclusion éventuelle de bibliothèques supplémentaires
#~ binpathincludes = []
#~ if sys.platform == "linux2":
    #~ # pour que les bibliothèques de /usr/lib soient copiées aussi
    #~ binpathincludes += ["/usr/lib"]
 #~ 
#~ # construction du dictionnaire des options
#~ options = {"path": path,
           #~ "includes": includes,
           #~ "excludes": excludes,
           #~ "packages": packages,
           #~ "include_files": includefiles,
           #~ "bin_path_includes": binpathincludes
           #~ }
 #~ 
#~ #############################################################################
#~ # préparation des cibles
#~ base = None
#~ if sys.platform == "win32":
    #~ base = "Win32GUI"
 #~ 
#~ cible_1 = Executable(
    #~ script = "main.py",
    #~ base = base,
    #~ compress = True,
    #~ icon = None,
    #~ )
 #~ 
#~ #############################################################################
#~ # création du setup
#~ setup(
    #~ name = "lightapp",
    #~ version = "1",
    #~ description = "appli console lumière",
    #~ author = "Raphi",
    #~ options = {"build_exe": options},
    #~ executables = [cible_1]
    #~ )
