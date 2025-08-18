import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

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

skip = SilentTransition()

# Steps in the process
# Site Survey, Zoning Check, Design Layout, System Order, Structure Build
site_zoning = OperatorPOWL(operator=Operator.XOR, children=[site_survey, zoning_check])
design_order = OperatorPOWL(operator=Operator.XOR, children=[design_layout, system_order])
structure_build = OperatorPOWL(operator=Operator.XOR, children=[structure_build, skip])

# Install Hydroponics, Calibrate Sensors
install_calibrate = OperatorPOWL(operator=Operator.XOR, children=[install_hydroponics, calibrate_sensors])

# Select Crops, Plant Seeding, Monitor Growth
select_plant = OperatorPOWL(operator=Operator.XOR, children=[select_crops, plant_seeding, monitor_growth])

# Manage Pests, Schedule Harvest
manage_pest_schedule = OperatorPOWL(operator=Operator.XOR, children=[manage_pests, schedule_harvest])

# Package Produce, Local Delivery
package_delivery = OperatorPOWL(operator=Operator.XOR, children=[package_produce, local_delivery])

# Analyze Data
analyze_data = OperatorPOWL(operator=Operator.XOR, children=[analyze_data, skip])

# Final loop
loop = OperatorPOWL(operator=Operator.LOOP, children=[select_plant, manage_pest_schedule, package_delivery])

# Root of the process
root = StrictPartialOrder(nodes=[site_zoning, design_order, structure_build, install_calibrate, select_plant, manage_pest_schedule, package_delivery, analyze_data, loop])
root.order.add_edge(site_zoning, design_order)
root.order.add_edge(design_order, structure_build)
root.order.add_edge(structure_build, install_calibrate)
root.order.add_edge(install_calibrate, select_plant)
root.order.add_edge(select_plant, manage_pest_schedule)
root.order.add_edge(manage_pest_schedule, package_delivery)
root.order.add_edge(package_delivery, analyze_data)
root.order.add_edge(analyze_data, loop)