from distutils.core import setup
import py2exe

setup(windows=['quick_csv_plot.py'],options={'py2exe': {'dist_dir': 'py2exe', 'includes': ['wx', 'wx._xml']}})