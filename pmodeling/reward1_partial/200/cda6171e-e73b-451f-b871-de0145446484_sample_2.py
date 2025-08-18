import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions (activities)
site_analysis = Transition(label='Site Analysis')
structure_check = Transition(label='Structure Check')
modify_layout = Transition(label='Modify Layout')
install_hvac = Transition(label='Install HVAC')
setup_hydroponics = Transition(label='Setup Hydroponics')
prepare_nutrients = Transition(label='Prepare Nutrients')
select_seeds = Transition(label='Select Seeds')
automate_planting = Transition(label='Automate Planting')
deploy_sensors = Transition(label='Deploy Sensors')
pest_control = Transition(label='Pest Control')
optimize_energy = Transition(label='Optimize Energy')
recycle_water = Transition(label='Recycle Water')
automate_harvest = Transition(label='Automate Harvest')
package_crops = Transition(label='Package Crops')
coordinate_delivery = Transition(label='Coordinate Delivery')
analyze_data = Transition(label='Analyze Data')

# Define silent transitions
skip = SilentTransition()

# Define operators
xor = OperatorPOWL(operator=Operator.XOR, children=[pest_control, skip])
loop = OperatorPOWL(operator=Operator.LOOP, children=[optimize_energy, recycle_water])
partial_order = StrictPartialOrder(nodes=[site_analysis, structure_check, modify_layout, install_hvac, setup_hydroponics, prepare_nutrients, select_seeds, automate_planting, deploy_sensors, xor, loop, automate_harvest, package_crops, coordinate_delivery, analyze_data])
partial_order.order.add_edge(site_analysis, structure_check)
partial_order.order.add_edge(structure_check, modify_layout)
partial_order.order.add_edge(modify_layout, install_hvac)
partial_order.order.add_edge(install_hvac, setup_hydroponics)
partial_order.order.add_edge(setup_hydroponics, prepare_nutrients)
partial_order.order.add_edge(prepare_nutrients, select_seeds)
partial_order.order.add_edge(select_seeds, automate_planting)
partial_order.order.add_edge(automate_planting, deploy_sensors)
partial_order.order.add_edge(deploy_sensors, xor)
partial_order.order.add_edge(xor, loop)
partial_order.order.add_edge(loop, automate_harvest)
partial_order.order.add_edge(automate_harvest, package_crops)
partial_order.order.add_edge(package_crops, coordinate_delivery)
partial_order.order.add_edge(coordinate_delivery, analyze_data)

# Set the root
root = partial_order