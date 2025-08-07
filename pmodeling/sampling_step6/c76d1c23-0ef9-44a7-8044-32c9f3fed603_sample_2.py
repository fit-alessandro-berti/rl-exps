from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the transitions for each activity
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

# Define the partial order
root = StrictPartialOrder(nodes=[
    site_survey, zoning_check, design_layout, system_order, structure_build, 
    install_hydroponics, calibrate_sensors, select_crops, plant_seeding, monitor_growth, 
    manage_pests, schedule_harvest, package_produce, local_delivery, analyze_data
])

# Add dependencies (if any)
# For example, the design layout should be done before system order:
root.order.add_edge(site_survey, design_layout)
root.order.add_edge(zoning_check, design_layout)
root.order.add_edge(design_layout, system_order)
root.order.add_edge(design_layout, structure_build)
root.order.add_edge(system_order, install_hydroponics)
root.order.add_edge(design_layout, calibrate_sensors)
root.order.add_edge(select_crops, plant_seeding)
root.order.add_edge(monitor_growth, manage_pests)
root.order.add_edge(schedule_harvest, package_produce)
root.order.add_edge(package_produce, local_delivery)
root.order.add_edge(analyze_data, local_delivery)

print(root)