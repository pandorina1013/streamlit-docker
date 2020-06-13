import base64

import numpy as np
import pandas as pd
import streamlit as st

from PIL import Image


# streamlit start
st.title("Example Report: April 1")


'''
Author: Kenta Yamada

## Updates

- Create exmple report

---

## Details

### Create exmple report

This is test report.

------------------------

#### Example Chart

'''


chart_data = pd.DataFrame(
  np.random.randn(20, 3),
  columns=['a', 'b', 'c'])

options = st.multiselect(
  '',
  ['a', 'b', 'c'],
  ['a'])

st.area_chart(chart_data[options])

'''
---

## Next

- Create real report!
'''