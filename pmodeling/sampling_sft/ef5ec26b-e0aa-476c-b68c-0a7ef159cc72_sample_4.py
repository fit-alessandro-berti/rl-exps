import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define the basic activities
site_survey      = Transition(label='Site Survey')
stakeholder_meet = Transition(label='Stakeholder Meet')
resource_plan    = Transition(label='Resource Plan')
crop_selection   = Transition(label='Crop Selection')
volunteer_sign   = Transition(label='Volunteer Sign-up')
tech_setup       = Transition(label='Tech Setup')
irrigation_check = Transition(label='Irrigation Check')
data_collection  = Transition(label='Data Collection')
growth_monitor   = Transition(label='Growth Monitoring')
conflict_mediate = Transition(label='Conflict Mediate')
workshop_prep    = Transition(label='Workshop Prep')
market_forecast  = Transition(label='Market Forecast')
yield_analysis   = Transition(label='Yield Analysis')
sustainability   = Transition(label='Sustainability Audit')
community_feedback = Transition(label='Community Feedback')
equipment_maintain = Transition(label='Equipment Maintain')
waste_manage     = Transition(label='Waste Manage')

# Loop for continuous monitoring and data collection
monitor_loop = OperatorPOWL(operator=Operator.LOOP, children=[growth_monitor, data_collection])

# Build the partial order
root = StrictPartialOrder(nodes=[
    site_survey,
    stakeholder_meet,
    resource_plan,
    crop_selection,
    volunteer_sign,
    tech_setup,
    irrigation_check,
    monitor_loop,
    conflict_mediate,
    workshop_prep,
    market_forecast,
    yield_analysis,
    sustainability,
    community_feedback,
    equipment_maintain,
    waste_manage
])

# Define the control-flow dependencies
root.order.add_edge(site_survey, stakeholder_meet)
root.order.add_edge(stakeholder_meet, resource_plan)
root.order.add_edge(resource_plan, crop_selection)
root.order.add_edge(crop_selection, volunteer_sign)
root.order.add_edge(volunteer_sign, tech_setup)
root.order.add_edge(tech_setup, irrigation_check)
root.order.add_edge(irrigation_check, monitor_loop)
root.order.add_edge(monitor_loop, conflict_mediate)
root.order.add_edge(conflict_mediate, workshop_prep)
root.order.add_edge(workshop_prep, market_forecast)
root.order.add_edge(market_forecast, yield_analysis)
root.order.add_edge(yield_analysis, sustainability)
root.order.add_edge(sustainability, community_feedback)
root.order.add_edge(community_feedback, equipment_maintain)
root.order.add_edge(equipment_maintain, waste_manage)

# Close the loop for continuous monitoring and data collection
root.order.add_edge(monitor_loop, growth_monitor)
root.order.add_edge(monitor_loop, data_collection)