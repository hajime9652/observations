from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.elastic2 import elastic2


def test_elastic2():
  """Test module elastic2.py by downloading
   elastic2.csv and testing shape of
   extracted data has 9 rows and 2 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = elastic2(test_path)
  try:
    assert x_train.shape == (9, 2)
  except:
    shutil.rmtree(test_path)
    raise()
