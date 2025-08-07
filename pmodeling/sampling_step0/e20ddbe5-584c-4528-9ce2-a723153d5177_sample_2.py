import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define activities
site_analysis = Transition(label='Site Analysis')
load_test = Transition(label='Load Test')
sunlight_map = Transition(label='Sunlight Map')
medium_select = Transition(label='Medium Select')
hydro_design = Transition(label='Hydro Design')
procure_seeds = Transition(label='Procure Seeds')
install_irrigation = Transition(label='Install Irrigation')
setup_climate = Transition(label='Setup Climate')
create_schedule = Transition(label='Create Schedule')
pest_control = Transition(label='Pest Control')
monitor_growth = Transition(label='Monitor Growth')
adjust_systems = Transition(label='Adjust Systems')
harvest_crops = Transition(label='Harvest Crops')
package_produce = Transition(label='Package Produce')
engage_community = Transition(label='Engage Community')
host_workshops = Transition(label='Host Workshops')

# Define operators
loop = OperatorPOWL(operator=Operator.LOOP, children=[pest_control, monitor_growth, adjust_systems])
xor = OperatorPOWL(operator=Operator.XOR, children=[harvest_crops, package_produce, engage_community, host_workshops])
xor2 = OperatorPOWL(operator=Operator.XOR, children=[sunlight_map, medium_select, hydro_design, procure_seeds, install_irrigation, setup_climate, create_schedule])
xor3 = OperatorPOWL(operator=Operator.XOR, children=[load_test, site_analysis, loop, xor2])

# Define root
root = StrictPartialOrder(nodes=[xor3, xor])
root.order.add_edge(xor3, xor)

print(root)