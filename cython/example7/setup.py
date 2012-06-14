#-----------------------------------------------------------------------------
# Imports
#-----------------------------------------------------------------------------
import distutils
from distutils.core import setup
from distutils.extension import Extension
from distutils.command.build_ext import build_ext
from distutils.command.sdist import sdist

import os
from os.path import join as pjoin

# TODO(hammer): Use setup.cfg to determine whether Cython is generating c or c++

#-----------------------------------------------------------------------------
# Flags
#-----------------------------------------------------------------------------
# ignore unused-function and strict-aliasing warnings, of which there
# will be many from the Cython generated code:
# note that this is only for gcc-style compilers
ignore_common_warnings = True

#-----------------------------------------------------------------------------
# Configuration
#-----------------------------------------------------------------------------

# buildutils.discover_settings(), init_settings() --> bundled_settings() or settings_from_prefix()
def init_settings():
  settings = {
    'libraries'     : [],
    'include_dirs'  : [],
    'library_dirs'  : [],
    'define_macros' : [],
  }

  # TODO(hammer): Allow the location to be configured
  settings['libraries'].append('calg')

  # suppress common warnings
  extra_flags = []
  if ignore_common_warnings:
    for warning in ('unused-function', 'strict-aliasing'):
      extra_flags.append('-Wno-'+warning)

  settings['extra_compile_args'] = extra_flags

  # include internal directories
  settings['include_dirs'] += ['.']

  return settings

COMPILER_SETTINGS = init_settings()

#-----------------------------------------------------------------------------
# Extra commands
#-----------------------------------------------------------------------------

# Configure, FetchCommand, TestCommand, GitRevisionCommand, CleanCommand, CheckSDist, CopyingBuild, CheckingBuildExt
class CheckSDist(sdist):
  """Custom sdist that ensures Cython has compiled all pyx files to c."""
  def initialize_options(self):
    sdist.initialize_options(self)
    self._pyxfiles = []
    for root, dirs, files in os.walk(''):
      for f in files:
        if f.endswith('.pyx'):
          self._pyxfiles.append(pjoin(root, f))

  def run(self):
    if 'cython' in cmdclass:
      self.run_command('cython')
    else:
      for pyxfile in self._pyxfiles:
        cfile = pyxfile[:-3]+'c'
        msg = "C source file '%s' not found."%(cfile)+\
        " Run 'setup.py cython' before sdist."
        assert os.path.isfile(cfile), msg
    sdist.run(self)

class CheckingBuildExt(build_ext):
  """Custom build_ext to get clearer report if Cython is neccessary."""
  def check_cython_extensions(self, extensions):
    for ext in extensions:
      for src in ext.sources:
        if not os.path.exists(src):
          fatal("""Cython-generated file '%s' not found.
          Cython is required to compile pyzmq from a development branch.
          Please install Cython or download a release package of pyzmq.
          """%src)

  def build_extensions(self):
    self.check_cython_extensions(self.extensions)
    self.check_extensions_list(self.extensions)
    for ext in self.extensions:
      self.build_extension(ext)

#-----------------------------------------------------------------------------
# Extensions
#-----------------------------------------------------------------------------

# New setup.py commands: test, clean, revision, configure, build, fetchbundle, cython, build_ext, sdist
# Set version, packages, extensions, package_data
cmdclass = {}

try:
  from Cython.Distutils import build_ext as build_ext_c
  cython = True
except ImportError:
  cython = False
  suffix = '.c'
  cmdclass['build_ext'] = CheckingBuildExt
else:
  suffix = '.pyx'

  class CythonCommand(build_ext_c):
    """Custom distutils command subclassed from Cython.Distutils.build_ext
    to compile pyx->c, and stop there. All this does is override the
    C-compile method build_extension() with a no-op."""
    description = "Compile Cython sources to C"
    def build_extension(self, ext):
      pass

  cmdclass['cython'] = CythonCommand
  cmdclass['build_ext'] = build_ext_c
  cmdclass['sdist'] = CheckSDist

modules = {'cqueue_demo': ['cqueue.pxd']}
extensions = []
for module, dependencies in modules.items():
  sources = [module + suffix]
  # Why include .pxd files as sources as well as package_data?
  if suffix == '.pyx':
    sources.extend(dependencies)
  ext = Extension(
    module,
    sources = sources,
    **COMPILER_SETTINGS
    )
  extensions.append(ext)

package_data = {'': ['cqueue.pxd']}

#-----------------------------------------------------------------------------
# Main setup
#-----------------------------------------------------------------------------

setup(
  name = 'cqueue_demo',
  version = '0.1.0',
  url = 'http://example.com',
  author = 'example',
  author_email = 'example@example.com',
  packages = [''],
  ext_modules = extensions,
  package_data = package_data,
  cmdclass = cmdclass,
)
