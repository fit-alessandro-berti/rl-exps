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

site_survey_loop = OperatorPOWL(operator=Operator.LOOP, children=[site_survey, zoning_check])
layout_loop = OperatorPOWL(operator=Operator.LOOP, children=[design_layout, system_order, structure_build])
hydroponics_loop = OperatorPOWL(operator=Operator.LOOP, children=[install_hydroponics, calibrate_sensors])
crop_loop = OperatorPOWL(operator=Operator.LOOP, children=[select_crops, plant_seeding, monitor_growth, manage_pests, schedule_harvest])
package_loop = OperatorPOWL(operator=Operator.LOOP, children=[package_produce, local_delivery])

root = StrictPartialOrder(nodes=[site_survey_loop, layout_loop, hydroponics_loop, crop_loop, package_loop])
root.order.add_edge(site_survey_loop, layout_loop)
root.order.add_edge(layout_loop, hydroponics_loop)
root.order.add_edge(hydroponics_loop, crop_loop)
root.order.add_edge(crop_loop, package_loop)

# Now, 'root' contains the POWL model for the urban vertical farm process.