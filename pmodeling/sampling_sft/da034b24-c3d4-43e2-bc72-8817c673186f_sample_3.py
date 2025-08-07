import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define activities
site_survey       = Transition(label='Site Survey')
permit_check      = Transition(label='Permit Check')
hive_setup        = Transition(label='Hive Setup')
community_meet    = Transition(label='Community Meet')
volunteer_coord   = Transition(label='Volunteer Coord')
workshop_plan     = Transition(label='Workshop Plan')
hive_monitor      = Transition(label='Hive Monitor')
pest_control      = Transition(label='Pest Control')
honey_harvest     = Transition(label='Honey Harvest')
data_logging      = Transition(label='Data Logging')
regulation_review = Transition(label='Regulation Review')
apiary_audit      = Transition(label='Apiary Audit')
pollination_map   = Transition(label='Pollination Map')
feedback_gather   = Transition(label='Feedback Gather')
supply_order      = Transition(label='Supply Order')
waste_manage      = Transition(label='Waste Manage')

# Loop for continuous monitoring and maintenance
monitor_loop = OperatorPOWL(operator=Operator.LOOP, children=[hive_monitor, pest_control])

# Build the partial order
root = StrictPartialOrder(nodes=[
    site_survey, permit_check, hive_setup, community_meet, volunteer_coord, workshop_plan,
    monitor_loop,
    regulation_review, apiary_audit, pollination_map, feedback_gather,
    supply_order, waste_manage
])

# Define the control-flow dependencies
root.order.add_edge(site_survey, permit_check)
root.order.add_edge(permit_check, hive_setup)
root.order.add_edge(hive_setup, community_meet)
root.order.add_edge(community_meet, volunteer_coord)
root.order.add_edge(volunteer_coord, workshop_plan)

root.order.add_edge(workshop_plan, monitor_loop)

root.order.add_edge(monitor_loop, regulation_review)
root.order.add_edge(regulation_review, apiary_audit)
root.order.add_edge(apiary_audit, pollination_map)
root.order.add_edge(pollination_map, feedback_gather)

root.order.add_edge(feedback_gather, supply_order)
root.order.add_edge(supply_order, waste_manage)

# Optional honey harvesting at the end
root.order.add_edge(monitor_loop, honey_harvest)
root.order.add_edge(honey_harvest, data_logging)

print(root)