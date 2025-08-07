import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define atomic activities
site_survey     = Transition(label='Site Survey')
permit_check    = Transition(label='Permit Check')
hive_setup      = Transition(label='Hive Setup')
community_meet  = Transition(label='Community Meet')
volunteer_coord = Transition(label='Volunteer Coord')
hive_monitor    = Transition(label='Hive Monitor')
pest_control    = Transition(label='Pest Control')
honey_harvest   = Transition(label='Honey Harvest')
data_logging    = Transition(label='Data Logging')
workshop_plan   = Transition(label='Workshop Plan')
supply_order    = Transition(label='Supply Order')
regulation_review = Transition(label='Regulation Review')
feedback_gather = Transition(label='Feedback Gather')
waste_manage    = Transition(label='Waste Manage')
apiary_audit    = Transition(label='Apiary Audit')
pollination_map = Transition(label='Pollination Map')

# Build the monitoring & maintenance branch: Hive Monitor -> Pest Control -> Honey Harvest -> Data Logging
monitoring = StrictPartialOrder(nodes=[hive_monitor, pest_control, honey_harvest, data_logging])
monitoring.order.add_edge(hive_monitor, pest_control)
monitoring.order.add_edge(pest_control, honey_harvest)
monitoring.order.add_edge(honey_harvest, data_logging)

# Build the supply chain branch: Supply Order -> Workshop Plan -> Regulation Review -> Feedback Gather -> Waste Manage
supply_chain = StrictPartialOrder(nodes=[supply_order, workshop_plan, regulation_review, feedback_gather, waste_manage])
supply_chain.order.add_edge(supply_order, workshop_plan)
supply_chain.order.add_edge(workshop_plan, regulation_review)
supply_chain.order.add_edge(regulation_review, feedback_gather)
supply_chain.order.add_edge(feedback_gather, waste_manage)

# Build the core coordination branch: Site Survey -> Permit Check -> Hive Setup -> Community Meet -> Monitoring
coordination = StrictPartialOrder(nodes=[site_survey, permit_check, hive_setup, community_meet, monitoring])
coordination.order.add_edge(site_survey, permit_check)
coordination.order.add_edge(permit_check, hive_setup)
coordination.order.add_edge(hive_setup, community_meet)
coordination.order.add_edge(community_meet, monitoring)

# Build the top‐level partial order: start -> core coordination -> supply chain -> apiary audit -> pollination map
root = StrictPartialOrder(nodes=[site_survey, supply_order, regulation_review, feedback_gather, waste_manage, monitoring, hive_setup, community_meet, apiary_audit, pollination_map])
root.order.add_edge(site_survey, supply_order)
root.order.add_edge(supply_order, regulation_review)
root.order.add_edge(regulation_review, feedback_gather)
root.order.add_edge(feedback_gather, waste_manage)
root.order.add_edge(waste_manage, hive_setup)
root.order.add_edge(hive_setup, community_meet)
root.order.add_edge(community_meet, monitoring)
root.order.add_edge(monitoring, apiary_audit)
root.order.add_edge(apiary_audit, pollination_map)