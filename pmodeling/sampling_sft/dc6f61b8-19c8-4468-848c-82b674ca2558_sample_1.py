import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define activities
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
carbon_audit      = Transition(label='Carbon Audit')
quality_check     = Transition(label='Quality Check')
crop_testing      = Transition(label='Crop Testing')
scale_review      = Transition(label='Scale Review')

# Loop for iterative adjustments after yield testing
adjust_loop = OperatorPOWL(
    operator=Operator.LOOP,
    children=[yield_adjust, data_analysis]
)

# Build the partial order
root = StrictPartialOrder(nodes=[
    site_survey,
    energy_partner,
    permit_filing,
    hydro_unit,
    ai_setup,
    nutrient_plan,
    system_install,
    community_meet,
    logistics_plan,
    adjust_loop,
    carbon_audit,
    quality_check,
    crop_testing,
    scale_review
])

# Define the control-flow dependencies
root.order.add_edge(site_survey, energy_partner)
root.order.add_edge(energy_partner, permit_filing)
root.order.add_edge(permit_filing, hydro_unit)
root.order.add_edge(hydro_unit, ai_setup)
root.order.add_edge(ai_setup, nutrient_plan)
root.order.add_edge(nutrient_plan, system_install)
root.order.add_edge(system_install, community_meet)
root.order.add_edge(community_meet, logistics_plan)
root.order.add_edge(logistics_plan, crop_testing)
root.order.add_edge(crop_testing, adjust_loop)
root.order.add_edge(adjust_loop, quality_check)
root.order.add_edge(quality_check, carbon_audit)
root.order.add_edge(carbon_audit, scale_review)

print(root)