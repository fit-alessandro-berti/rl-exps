from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

site_survey = Transition(label='Site Survey')
permit_check = Transition(label='Permit Check')
hive_setup = Transition(label='Hive Setup')
community_meet = Transition(label='Community Meet')
hive_monitor = Transition(label='Hive Monitor')
pest_control = Transition(label='Pest Control')
honey_harvest = Transition(label='Honey Harvest')
data_logging = Transition(label='Data Logging')
workshop_plan = Transition(label='Workshop Plan')
supply_order = Transition(label='Supply Order')
volunteer_coord = Transition(label='Volunteer Coord')
regulation_review = Transition(label='Regulation Review')
pollination_map = Transition(label='Pollination Map')
apiary_audit = Transition(label='Apiary Audit')
feedback_gather = Transition(label='Feedback Gather')
waste_manage = Transition(label='Waste Manage')

skip = SilentTransition()

# Define the process steps
site_survey_step = OperatorPOWL(operator=Operator.SILENT, children=[site_survey])
permit_check_step = OperatorPOWL(operator=Operator.SILENT, children=[permit_check])
hive_setup_step = OperatorPOWL(operator=Operator.SILENT, children=[hive_setup])
community_meet_step = OperatorPOWL(operator=Operator.SILENT, children=[community_meet])
hive_monitor_step = OperatorPOWL(operator=Operator.SILENT, children=[hive_monitor])
pest_control_step = OperatorPOWL(operator=Operator.SILENT, children=[pest_control])
honey_harvest_step = OperatorPOWL(operator=Operator.SILENT, children=[honey_harvest])
data_logging_step = OperatorPOWL(operator=Operator.SILENT, children=[data_logging])
workshop_plan_step = OperatorPOWL(operator=Operator.SILENT, children=[workshop_plan])
supply_order_step = OperatorPOWL(operator=Operator.SILENT, children=[supply_order])
volunteer_coord_step = OperatorPOWL(operator=Operator.SILENT, children=[volunteer_coord])
regulation_review_step = OperatorPOWL(operator=Operator.SILENT, children=[regulation_review])
pollination_map_step = OperatorPOWL(operator=Operator.SILENT, children=[pollination_map])
apiary_audit_step = OperatorPOWL(operator=Operator.SILENT, children=[apiary_audit])
feedback_gather_step = OperatorPOWL(operator=Operator.SILENT, children=[feedback_gather])
waste_manage_step = OperatorPOWL(operator=Operator.SILENT, children=[waste_manage])

# Define the process as a strict partial order
root = StrictPartialOrder(nodes=[
    site_survey_step,
    permit_check_step,
    hive_setup_step,
    community_meet_step,
    hive_monitor_step,
    pest_control_step,
    honey_harvest_step,
    data_logging_step,
    workshop_plan_step,
    supply_order_step,
    volunteer_coord_step,
    regulation_review_step,
    pollination_map_step,
    apiary_audit_step,
    feedback_gather_step,
    waste_manage_step
])

# Define the dependencies between nodes
root.order.add_edge(site_survey_step, permit_check_step)
root.order.add_edge(permit_check_step, hive_setup_step)
root.order.add_edge(hive_setup_step, community_meet_step)
root.order.add_edge(community_meet_step, hive_monitor_step)
root.order.add_edge(hive_monitor_step, pest_control_step)
root.order.add_edge(pest_control_step, honey_harvest_step)
root.order.add_edge(honey_harvest_step, data_logging_step)
root.order.add_edge(data_logging_step, workshop_plan_step)
root.order.add_edge(workshop_plan_step, supply_order_step)
root.order.add_edge(supply_order_step, volunteer_coord_step)
root.order.add_edge(volunteer_coord_step, regulation_review_step)
root.order.add_edge(regulation_review_step, pollination_map_step)
root.order.add_edge(pollination_map_step, apiary_audit_step)
root.order.add_edge(apiary_audit_step, feedback_gather_step)
root.order.add_edge(feedback_gather_step, waste_manage_step)

print(root)