import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define activities
site_survey    = Transition(label='Site Survey')
stakeholder_meet = Transition(label='Stakeholder Meet')
resource_plan  = Transition(label='Resource Plan')
crop_selection = Transition(label='Crop Selection')
volunteer_sign = Transition(label='Volunteer Sign-up')
tech_setup     = Transition(label='Tech Setup')
irrigation_chk = Transition(label='Irrigation Check')
data_collect   = Transition(label='Data Collection')
growth_monit   = Transition(label='Growth Monitoring')
conflict_med   = Transition(label='Conflict Mediate')
workshop_prep  = Transition(label='Workshop Prep')
market_forest  = Transition(label='Market Forecast')
yield_analysis = Transition(label='Yield Analysis')
sustain_audit  = Transition(label='Sustainability Audit')
community_feed = Transition(label='Community Feedback')
equipment_maint= Transition(label='Equipment Maintain')
waste_manage   = Transition(label='Waste Manage')

# Loop for continuous monitoring & maintenance
monitor_loop = OperatorPOWL(operator=Operator.LOOP, children=[growth_monit, conflict_med])

# Build the partial order
root = StrictPartialOrder(nodes=[
    site_survey, stakeholder_meet, resource_plan, crop_selection,
    volunteer_sign, tech_setup, irrigation_chk, data_collect,
    monitor_loop, workshop_prep, market_forest, yield_analysis,
    sustain_audit, community_feed, equipment_maint, waste_manage
])

# Define the control-flow dependencies
root.order.add_edge(site_survey, stakeholder_meet)
root.order.add_edge(stakeholder_meet, resource_plan)
root.order.add_edge(resource_plan, crop_selection)
root.order.add_edge(crop_selection, volunteer_sign)
root.order.add_edge(volunteer_sign, tech_setup)
root.order.add_edge(tech_setup, irrigation_chk)
root.order.add_edge(tech_setup, data_collect)
root.order.add_edge(irrigation_chk, monitor_loop)
root.order.add_edge(data_collect, monitor_loop)
root.order.add_edge(monitor_loop, workshop_prep)
root.order.add_edge(workshop_prep, market_forest)
root.order.add_edge(market_forest, yield_analysis)
root.order.add_edge(yield_analysis, sustain_audit)
root.order.add_edge(sustain_audit, community_feed)
root.order.add_edge(community_feed, equipment_maint)
root.order.add_edge(equipment_maint, waste_manage)

print(root)