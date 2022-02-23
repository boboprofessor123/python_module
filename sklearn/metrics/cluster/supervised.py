
# THIS FILE WAS AUTOMATICALLY GENERATED BY deprecated_modules.py
import sys
# mypy error: Module X has no attribute y (typically for C extensions)
from . import _supervised  # type: ignore
from ...externals._pep562 import Pep562
from ...utils.deprecation import _raise_dep_warning_if_not_pytest

deprecated_path = 'sklearn.metrics.cluster.supervised'
correct_import_path = 'sklearn.metrics.cluster'

_raise_dep_warning_if_not_pytest(deprecated_path, correct_import_path)

def __getattr__(name):
    return getattr(_supervised, name)

if not sys.version_info >= (3, 7):
    Pep562(__name__)