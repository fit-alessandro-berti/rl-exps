import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define activities
site_survey      = Transition(label='Site Survey')
energy_partner   = Transition(label='Energy Partner')
permit_filing    = Transition(label='Permit Filing')
hydro_unit       = Transition(label='Hydro Unit')
ai_setup         = Transition(label='AI Setup')
nutrient_plan    = Transition(label='Nutrient Plan')
system_install   = Transition(label='System Install')
community_meet   = Transition(label='Community Meet')
carbon_audit     = Transition(label='Carbon Audit')
logistics_plan   = Transition(label='Logistics Plan')
crop_testing     = Transition(label='Crop Testing')
data_analysis    = Transition(label='Data Analysis')
yield_adjust     = Transition(label='Yield Adjust')
quality_check    = Transition(label='Quality Check')
scale_review     = Transition(label='Scale Review')

# Define the iterative refinement loop
# A = Crop Testing -> Data Analysis -> Yield Adjust
A = StrictPartialOrder(nodes=[crop_testing, data_analysis, yield_adjust])
A.order.add_edge(crop_testing, data_analysis)
A.order.add_edge(data_analysis, yield_adjust)

# B = Quality Check -> Scale Review
B = StrictPartialOrder(nodes=[quality_check, scale_review])
B.order.add_edge(quality_check, scale_review)

# LOOP(A, B): do A, then either exit or do B then A again
loop = OperatorPOWL(operator=Operator.LOOP, children=[A, B])

# Build the overall partial order
root = StrictPartialOrder(nodes=[
    site_survey,
    energy_partner,
    permit_filing,
    hydro_unit,
    ai_setup,
    nutrient_plan,
    system_install,
    community_meet,
    carbon_audit,
    logistics_plan,
    loop
])

# Define the control-flow dependencies
root.order.add_edge(site_survey, energy_partner)
root.order.add_edge(energy_partner, permit_filing)
root.order.add_edge(permit_filing, hydro_unit)
root.order.add_edge(hydro_unit, ai_setup)
root.order.add_edge(ai_setup, nutrient_plan)
root.order.add_edge(nutrient_plan, system_install)
root.order.add_edge(system_install, community_meet)
root.order.add_edge(community_meet, carbon_audit)
root.order.add_edge(carbon_audit, logistics_plan)
root.order.add_edge(logistics_plan, loop)