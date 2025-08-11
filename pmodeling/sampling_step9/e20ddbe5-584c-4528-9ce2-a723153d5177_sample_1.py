import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions for each activity
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

# Define silent transitions
skip = SilentTransition()

# Define loop for pest control
pest_loop = OperatorPOWL(operator=Operator.LOOP, children=[pest_control, skip])

# Define choice for pest control and skip
pest_choice = OperatorPOWL(operator=Operator.XOR, children=[pest_control, skip])

# Define loop for monitoring and adjusting systems
monitor_loop = OperatorPOWL(operator=Operator.LOOP, children=[monitor_growth, adjust_systems])

# Define partial order
root = StrictPartialOrder(nodes=[site_analysis, load_test, sunlight_map, medium_select, hydro_design, procure_seeds, install_irrigation, setup_climate, create_schedule, pest_loop, pest_choice, monitor_loop, harvest_crops, package_produce, engage_community, host_workshops])
root.order.add_edge(site_analysis, load_test)
root.order.add_edge(site_analysis, sunlight_map)
root.order.add_edge(load_test, medium_select)
root.order.add_edge(load_test, hydro_design)
root.order.add_edge(medium_select, procure_seeds)
root.order.add_edge(medium_select, install_irrigation)
root.order.add_edge(hydro_design, setup_climate)
root.order.add_edge(setup_climate, create_schedule)
root.order.add_edge(create_schedule, pest_loop)
root.order.add_edge(create_schedule, pest_choice)
root.order.add_edge(pest_loop, pest_choice)
root.order.add_edge(pest_choice, monitor_loop)
root.order.add_edge(monitor_loop, adjust_systems)
root.order.add_edge(harvest_crops, package_produce)
root.order.add_edge(package_produce, engage_community)
root.order.add_edge(engage_community, host_workshops)