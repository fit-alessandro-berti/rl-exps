import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define activities
site_survey      = Transition(label='Site Survey')
permit_check     = Transition(label='Permit Check')
hive_setup       = Transition(label='Hive Setup')
community_meet   = Transition(label='Community Meet')
volunteer_coord  = Transition(label='Volunteer Coord')
hive_monitor     = Transition(label='Hive Monitor')
pest_control     = Transition(label='Pest Control')
honey_harvest    = Transition(label='Honey Harvest')
data_logging     = Transition(label='Data Logging')
workshop_plan    = Transition(label='Workshop Plan')
supply_order     = Transition(label='Supply Order')
regulation_review= Transition(label='Regulation Review')
pollination_map  = Transition(label='Pollination Map')
apiary_audit     = Transition(label='Apiary Audit')
feedback_gather  = Transition(label='Feedback Gather')
waste_manage     = Transition(label='Waste Manage')

# Loop: Hive Monitor -> Pest Control, repeated until exit
loop_monitor_pest = OperatorPOWL(operator=Operator.LOOP, children=[hive_monitor, pest_control])

# Build the partial order
root = StrictPartialOrder(nodes=[
    site_survey, permit_check, hive_setup,
    community_meet, volunteer_coord,
    loop_monitor_pest,
    honey_harvest, data_logging,
    workshop_plan, supply_order,
    regulation_review, pollination_map,
    apiary_audit, feedback_gather,
    waste_manage
])

# Define the control-flow dependencies
root.order.add_edge(site_survey, permit_check)
root.order.add_edge(permit_check, hive_setup)
root.order.add_edge(hive_setup, community_meet)
root.order.add_edge(community_meet, volunteer_coord)
root.order.add_edge(volunteer_coord, loop_monitor_pest)
root.order.add_edge(loop_monitor_pest, honey_harvest)
root.order.add_edge(loop_monitor_pest, data_logging)
root.order.add_edge(honey_harvest, workshop_plan)
root.order.add_edge(honey_harvest, supply_order)
root.order.add_edge(data_logging, regulation_review)
root.order.add_edge(data_logging, pollination_map)
root.order.add_edge(workshop_plan, apiary_audit)
root.order.add_edge(supply_order, apiary_audit)
root.order.add_edge(regulation_review, apiary_audit)
root.order.add_edge(pollination_map, apiary_audit)
root.order.add_edge(apiary_audit, feedback_gather)
root.order.add_edge(apiary_audit, waste_manage)

# Print the root model for verification
print(root)