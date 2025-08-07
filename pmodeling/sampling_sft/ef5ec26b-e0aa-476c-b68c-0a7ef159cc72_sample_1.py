import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define all activities as transitions
site_survey    = Transition(label='Site Survey')
soil_testing   = Transition(label='Soil Testing')
stakeholder_meet = Transition(label='Stakeholder Meet')
resource_plan  = Transition(label='Resource Plan')
crop_selection = Transition(label='Crop Selection')
volunteer_signup = Transition(label='Volunteer Sign-up')
tech_setup     = Transition(label='Tech Setup')
irrigation_check = Transition(label='Irrigation Check')
data_collection = Transition(label='Data Collection')
growth_monitoring = Transition(label='Growth Monitoring')
conflict_mediate = Transition(label='Conflict Mediate')
workshop_prep  = Transition(label='Workshop Prep')
market_forecast = Transition(label='Market Forecast')
yield_analysis = Transition(label='Yield Analysis')
sustainability_audit = Transition(label='Sustainability Audit')
community_feedback = Transition(label='Community Feedback')
equipment_maintain = Transition(label='Equipment Maintain')
waste_manage   = Transition(label='Waste Manage')

# Build the monitoring & maintenance partial order
monitor_po = StrictPartialOrder(nodes=[
    data_collection, growth_monitoring, conflict_mediate,
    workshop_prep, market_forecast, yield_analysis,
    sustainability_audit, community_feedback,
    equipment_maintain, waste_manage
])
monitor_po.order.add_edge(data_collection, growth_monitoring)
monitor_po.order.add_edge(growth_monitoring, conflict_mediate)
monitor_po.order.add_edge(conflict_mediate, workshop_prep)
monitor_po.order.add_edge(workshop_prep, market_forecast)
monitor_po.order.add_edge(market_forecast, yield_analysis)
monitor_po.order.add_edge(yield_analysis, sustainability_audit)
monitor_po.order.add_edge(sustainability_audit, community_feedback)
monitor_po.order.add_edge(community_feedback, equipment_maintain)
monitor_po.order.add_edge(equipment_maintain, waste_manage)

# Loop for continuous monitoring
loop_monitor = OperatorPOWL(operator=Operator.LOOP, children=[monitor_po, monitor_po])

# Assemble the overall root partial order
root = StrictPartialOrder(nodes=[
    site_survey, soil_testing, stakeholder_meet,
    resource_plan, crop_selection, volunteer_signup,
    tech_setup, irrigation_check, loop_monitor
])
root.order.add_edge(site_survey, soil_testing)
root.order.add_edge(soil_testing, stakeholder_meet)
root.order.add_edge(stakeholder_meet, resource_plan)
root.order.add_edge(resource_plan, crop_selection)
root.order.add_edge(crop_selection, volunteer_signup)
root.order.add_edge(volunteer_signup, tech_setup)
root.order.add_edge(tech_setup, irrigation_check)
root.order.add_edge(irrigation_check, loop_monitor)

print(root)