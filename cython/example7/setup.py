from distutils.core import setup
from distutils.extension import Extension
from distutils.command.sdist import sdist

class CythonSDist(sdist):
  def run(self):
    self.run_command('cython')
    sdist.run(self)

cmdclass = {}
try:
  from Cython.Distutils import build_ext
  cython = True
except ImportError:
  cython = False
  suffix = '.c'
else:
  suffix = '.pyx'
  class CythonCommand(build_ext):
    def build_extension(self, ext):
      pass
  cmdclass['cython'] = CythonCommand
  cmdclass['build_ext'] = build_ext
  cmdclass['sdist'] = CythonSDist

COMPILER_SETTINGS = {'libraries': ['calg']}
modules = {'cqueue_demo': ['cqueue.pxd']}
extensions = []
for module, dependencies in modules.items():
  sources = [module + suffix]
  if suffix == '.pyx':
    sources.extend(dependencies)
  ext = Extension(
    module,
    sources = sources,
    **COMPILER_SETTINGS
    )
  extensions.append(ext)

package_data = {'': ['cqueue.pxd']}

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
