import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define all transitions
site_survey       = Transition(label='Site Survey')
energy_partner    = Transition(label='Energy Partner')
permit_filing     = Transition(label='Permit Filing')
hydro_unit        = Transition(label='Hydro Unit')
ai_setup          = Transition(label='AI Setup')
nutrient_plan     = Transition(label='Nutrient Plan')
system_install    = Transition(label='System Install')
community_meet    = Transition(label='Community Meet')
logistics_plan    = Transition(label='Logistics Plan')
yield_adjust      = Transition(label='Yield Adjust')
data_analysis     = Transition(label='Data Analysis')
quality_check     = Transition(label='Quality Check')
carbon_audit      = Transition(label='Carbon Audit')
scale_review      = Transition(label='Scale Review')
crop_testing      = Transition(label='Crop Testing')

# Define the loop for continuous monitoring and adjustments
# A: yield testing, data analysis, quality check
A = StrictPartialOrder(nodes=[yield_adjust, data_analysis, quality_check])
# B: carbon audit, scale review
B = StrictPartialOrder(nodes=[carbon_audit, scale_review])
# LOOP: do A, then optionally do B and repeat
monitor_loop = OperatorPOWL(operator=Operator.LOOP, children=[A, B])

# Build the overall partial order
root = StrictPartialOrder(nodes=[
    site_survey, energy_partner, permit_filing, hydro_unit, ai_setup,
    nutrient_plan, system_install, community_meet, logistics_plan,
    crop_testing, monitor_loop, data_analysis, quality_check,
    carbon_audit, scale_review
])

# Add the control-flow edges
root.order.add_edge(site_survey, energy_partner)
root.order.add_edge(site_survey, permit_filing)
root.order.add_edge(energy_partner, hydro_unit)
root.order.add_edge(permit_filing, hydro_unit)
root.order.add_edge(hydro_unit, ai_setup)
root.order.add_edge(ai_setup, nutrient_plan)
root.order.add_edge(hydro_unit, system_install)
root.order.add_edge(system_install, community_meet)
root.order.add_edge(community_meet, logistics_plan)
root.order.add_edge(logistics_plan, crop_testing)
root.order.add_edge(crop_testing, monitor_loop)
root.order.add_edge(monitor_loop, data_analysis)
root.order.add_edge(monitor_loop, quality_check)
root.order.add_edge(monitor_loop, carbon_audit)
root.order.add_edge(monitor_loop, scale_review)