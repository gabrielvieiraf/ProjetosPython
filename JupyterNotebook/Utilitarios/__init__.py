import os

# Packagers: Modifique a próxima linha se você armazenar os arquivos de modelo do notebook em outro local
DEFAULT_STATIC_FILES_PATH = os.path.join(os.path.dirname(__file__), "static")

# Inclua notebook /notebook/ e notebook/templates/.
# Isso torna possível que os usuários substituam um modelo por um arquivo herdado daquele template.
#
# Por exemplo, se você deseja substituir um bloco específico de notebook.html, pode
# pode criar um arquivo chamado notebook.html que herda de templates / notebook.html,
# e o último será resolvido corretamente para a base implementação.

DEFAULT_TEMPLATE_PATH_LIST = [
    os.path.dirname(__file__),
    os.path.join(os.path.dirname(__file__), "templates"),
]

del os

from .nbextensions import install_nbextension
from ._version import version_info, __version__
