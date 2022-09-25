#%%
import matplotlib.pyplot as plt

from psychrochart import PsychroChart, load_config

# Load default style:
chart_default = PsychroChart("ashrae")
ax = chart_default.plot()
ax.get_figure()
#%%