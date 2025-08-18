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

site_survey_node = OperatorPOWL(operator=Operator.SILENT, children=[site_survey, zoning_check])
design_layout_node = OperatorPOWL(operator=Operator.SILENT, children=[design_layout, system_order, structure_build, install_hydroponics])
calibrate_sensors_node = OperatorPOWL(operator=Operator.SILENT, children=[calibrate_sensors, select_crops, plant_seeding])
monitor_growth_node = OperatorPOWL(operator=Operator.SILENT, children=[monitor_growth, manage_pests, schedule_harvest])
package_produce_node = OperatorPOWL(operator=Operator.SILENT, children=[package_produce, local_delivery])
analyze_data_node = OperatorPOWL(operator=Operator.SILENT, children=[analyze_data])

root = StrictPartialOrder(nodes=[site_survey_node, design_layout_node, calibrate_sensors_node, monitor_growth_node, package_produce_node, analyze_data_node])
root.order.add_edge(site_survey_node, design_layout_node)
root.order.add_edge(design_layout_node, calibrate_sensors_node)
root.order.add_edge(calibrate_sensors_node, monitor_growth_node)
root.order.add_edge(monitor_growth_node, package_produce_node)
root.order.add_edge(package_produce_node, analyze_data_node)