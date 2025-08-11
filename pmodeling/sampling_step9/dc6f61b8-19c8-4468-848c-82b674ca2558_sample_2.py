import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions
site_survey = Transition(label='Site Survey')
energy_partner = Transition(label='Energy Partner')
permit_filing = Transition(label='Permit Filing')
hydro_unit = Transition(label='Hydro Unit')
ai_setup = Transition(label='AI Setup')
nutrient_plan = Transition(label='Nutrient Plan')
system_install = Transition(label='System Install')
crop_testing = Transition(label='Crop Testing')
data_analysis = Transition(label='Data Analysis')
community_meet = Transition(label='Community Meet')
yield_adjust = Transition(label='Yield Adjust')
carbon_audit = Transition(label='Carbon Audit')
logistics_plan = Transition(label='Logistics Plan')
quality_check = Transition(label='Quality Check')
scale_review = Transition(label='Scale Review')

# Define silent transitions
skip = SilentTransition()

# Define loops and choices
loop1 = OperatorPOWL(operator=Operator.LOOP, children=[energy_partner, permit_filing])
loop2 = OperatorPOWL(operator=Operator.LOOP, children=[hydro_unit, nutrient_plan])
loop3 = OperatorPOWL(operator=Operator.LOOP, children=[system_install, crop_testing])
loop4 = OperatorPOWL(operator=Operator.LOOP, children=[data_analysis, community_meet])
loop5 = OperatorPOWL(operator=Operator.LOOP, children=[yield_adjust, carbon_audit])
loop6 = OperatorPOWL(operator=Operator.LOOP, children=[logistics_plan, quality_check])
loop7 = OperatorPOWL(operator=Operator.LOOP, children=[scale_review, skip])

# Define root model
root = StrictPartialOrder(nodes=[loop1, loop2, loop3, loop4, loop5, loop6, loop7])
root.order.add_edge(loop1, loop2)
root.order.add_edge(loop2, loop3)
root.order.add_edge(loop3, loop4)
root.order.add_edge(loop4, loop5)
root.order.add_edge(loop5, loop6)
root.order.add_edge(loop6, loop7)

print(root)