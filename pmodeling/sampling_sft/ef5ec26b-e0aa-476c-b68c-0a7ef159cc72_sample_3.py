import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions for each activity
site_survey       = Transition(label='Site Survey')
soil_testing      = Transition(label='Soil Testing')
stakeholder_meet  = Transition(label='Stakeholder Meet')
resource_plan     = Transition(label='Resource Plan')
crop_selection    = Transition(label='Crop Selection')
volunteer_sign_up = Transition(label='Volunteer Sign-up')
tech_setup        = Transition(label='Tech Setup')
irrigation_check  = Transition(label='Irrigation Check')
data_collection   = Transition(label='Data Collection')
growth_monitoring = Transition(label='Growth Monitoring')
conflict_mediate  = Transition(label='Conflict Mediate')
workshop_prep     = Transition(label='Workshop Prep')
market_forecast   = Transition(label='Market Forecast')
yield_analysis    = Transition(label='Yield Analysis')
sustainability_audit = Transition(label='Sustainability Audit')
community_feedback = Transition(label='Community Feedback')
equipment_maintain = Transition(label='Equipment Maintain')
waste_manage      = Transition(label='Waste Manage')

# Define the monitoring loop: repeat Data Collection -> Growth Monitoring until exit
monitor_loop = OperatorPOWL(
    operator=Operator.LOOP,
    children=[data_collection, growth_monitoring]
)

# Build the top-level partial order
root = StrictPartialOrder(nodes=[
    site_survey,
    soil_testing,
    stakeholder_meet,
    resource_plan,
    crop_selection,
    volunteer_sign_up,
    tech_setup,
    irrigation_check,
    monitor_loop,
    conflict_mediate,
    workshop_prep,
    market_forecast,
    yield_analysis,
    sustainability_audit,
    community_feedback,
    equipment_maintain,
    waste_manage
])

# Define the control-flow dependencies
root.order.add_edge(site_survey,      soil_testing)
root.order.add_edge(soil_testing,     stakeholder_meet)
root.order.add_edge(stakeholder_meet, resource_plan)
root.order.add_edge(resource_plan,    crop_selection)
root.order.add_edge(crop_selection,   volunteer_sign_up)
root.order.add_edge(volunteer_sign_up, tech_setup)
root.order.add_edge(tech_setup,       irrigation_check)
root.order.add_edge(irrigation_check, monitor_loop)

# Monitoring loop body
root.order.add_edge(monitor_loop, conflict_mediate)
root.order.add_edge(monitor_loop, workshop_prep)
root.order.add_edge(monitor_loop, market_forecast)

# After monitoring, do the analysis and sustainability audit
root.order.add_edge(conflict_mediate, yield_analysis)
root.order.add_edge(conflict_mediate, sustainability_audit)
root.order.add_edge(workshop_prep, yield_analysis)
root.order.add_edge(workshop_prep, sustainability_audit)
root.order.add_edge(market_forecast, yield_analysis)
root.order.add_edge(market_forecast, sustainability_audit)

# After all analyses, do the feedback, maintenance, and waste management
root.order.add_edge(yield_analysis, community_feedback)
root.order.add_edge(yield_analysis, equipment_maintain)
root.order.add_edge(yield_analysis, waste_manage)
root.order.add_edge(sustainability_audit, community_feedback)
root.order.add_edge(sustainability_audit, equipment_maintain)
root.order.add_edge(sustainability_audit, waste_manage)

# Final transitions after all activities
root.order.add_edge(community_feedback, waste_manage)
root.order.add_edge(equipment_maintain, waste_manage)