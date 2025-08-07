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

# Define transitions
skip = SilentTransition()

# Define loops and choices
loop1 = OperatorPOWL(operator=Operator.LOOP, children=[site_analysis, load_test, sunlight_map])
loop2 = OperatorPOWL(operator=Operator.LOOP, children=[medium_select, hydro_design])
loop3 = OperatorPOWL(operator=Operator.LOOP, children=[procure_seeds, install_irrigation, setup_climate])
loop4 = OperatorPOWL(operator=Operator.LOOP, children=[create_schedule, pest_control])
loop5 = OperatorPOWL(operator=Operator.LOOP, children=[monitor_growth, adjust_systems])
loop6 = OperatorPOWL(operator=Operator.LOOP, children=[harvest_crops, package_produce])
loop7 = OperatorPOWL(operator=Operator.LOOP, children=[engage_community, host_workshops])

# Define the root
root = StrictPartialOrder(nodes=[loop1, loop2, loop3, loop4, loop5, loop6, loop7])
root.order.add_edge(loop1, loop2)
root.order.add_edge(loop2, loop3)
root.order.add_edge(loop3, loop4)
root.order.add_edge(loop4, loop5)
root.order.add_edge(loop5, loop6)
root.order.add_edge(loop6, loop7)