import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator
root = StrictPartialOrder()
site_survey = Transition('Site Survey')
zoning_check = Transition('Zoning Check')
design_layout = Transition('Design Layout')
system_order = Transition('System Order')
structure_build = Transition('Structure Build')
install_hydroponics = Transition('Install Hydroponics')
calibrate_sensors = Transition('Calibrate Sensors')
select_crops = Transition('Select Crops')
plant_seeding = Transition('Plant Seeding')
monitor_growth = Transition('Monitor Growth')
manage_pests = Transition('Manage Pests')
schedule_harvest = Transition('Schedule Harvest')
package_produce = Transition('Package Produce')
local_delivery = Transition('Local Delivery')
analyze_data = Transition('Analyze Data')

root.nodes = [site_survey, zoning_check, design_layout, system_order, structure_build, install_hydroponics, calibrate_sensors, select_crops, plant_seeding, monitor_growth, manage_pests, schedule_harvest, package_produce, local_delivery, analyze_data]

root.order.add_edge(site_survey, zoning_check)
root.order.add_edge(zoning_check, design_layout)
root.order.add_edge(design_layout, system_order)
root.order.add_edge(system_order, structure_build)
root.order.add_edge(structure_build, install_hydroponics)
root.order.add_edge(install_hydroponics, calibrate_sensors)
root.order.add_edge(calibrate_sensors, select_crops)
root.order.add_edge(select_crops, plant_seeding)
root.order.add_edge(plant_seeding, monitor_growth)
root.order.add_edge(monitor_growth, manage_pests)
root.order.add_edge(manage_pests, schedule_harvest)
root.order.add_edge(schedule_harvest, package_produce)
root.order.add_edge(package_produce, local_delivery)
root.order.add_edge(local_delivery, analyze_data)

print(root)