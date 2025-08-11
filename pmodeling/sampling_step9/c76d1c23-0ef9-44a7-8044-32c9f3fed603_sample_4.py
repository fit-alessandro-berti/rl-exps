import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions for each activity
site_survey = Transition(label='Site Survey')
zoning_check = Transition(label='Zoning Check')
design_layout = Transition(label='Design Layout')
system_order = Transition(label='System Order')
structure_build = Transition(label='Structure Build')
install_hydroponics = Transition(label='Install Hydroponics')
calibrate_sensors = Transition(label='Calibrate Sensors')
select_crops = Transition(label='Select Crops')
plant_seeding = Transition(label='Plant Seeding')
monitor_growth = Transition(label='Monitor Growth')
manage_pests = Transition(label='Manage Pests')
schedule_harvest = Transition(label='Schedule Harvest')
package_produce = Transition(label='Package Produce')
local_delivery = Transition(label='Local Delivery')
analyze_data = Transition(label='Analyze Data')

# Define silent transitions for no actions
skip = SilentTransition()

# Define a loop for continuous monitoring and adaptive pest management
monitor_loop = OperatorPOWL(operator=Operator.LOOP, children=[monitor_growth, manage_pests])

# Define exclusive choice for scheduling harvest and local delivery
harvest_delivery_choice = OperatorPOWL(operator=Operator.XOR, children=[schedule_harvest, local_delivery])

# Define the root POWL model
root = StrictPartialOrder(nodes=[site_survey, zoning_check, design_layout, system_order, structure_build, install_hydroponics, calibrate_sensors, select_crops, plant_seeding, monitor_loop, harvest_delivery_choice, package_produce, analyze_data])
root.order.add_edge(site_survey, zoning_check)
root.order.add_edge(zoning_check, design_layout)
root.order.add_edge(design_layout, system_order)
root.order.add_edge(system_order, structure_build)
root.order.add_edge(structure_build, install_hydroponics)
root.order.add_edge(install_hydroponics, calibrate_sensors)
root.order.add_edge(calibrate_sensors, select_crops)
root.order.add_edge(select_crops, plant_seeding)
root.order.add_edge(plant_seeding, monitor_loop)
root.order.add_edge(monitor_loop, harvest_delivery_choice)
root.order.add_edge(harvest_delivery_choice, package_produce)
root.order.add_edge(package_produce, analyze_data)