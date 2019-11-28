from distutils.core import setup
from catkin_pkg.python_setup import generate_distutils_setup

d = generate_distutils_setup(
    packages=['pyarm'],
    scripts=['scripts/move_to_node.py',
             'scripts/pump_node.py',
		     'scripts/report_angles_node.py',
		     'scripts/report_coords_node.py',
		     'scripts/report_stopper_node.py',
		     'scripts/uarm_core.py',
		     'scripts/uarm_status_node.py',
		     'scripts/write_angles_node.py'],
    package_dir={'': 'src'}
)

setup(**d)
