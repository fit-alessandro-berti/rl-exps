from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the activities
site_survey = Transition(label='Site Survey')
permit_filing = Transition(label='Permit Filing')
load_testing = Transition(label='Load Testing')
soil_sampling = Transition(label='Soil Sampling')
water_testing = Transition(label='Water Testing')
system_design = Transition(label='System Design')
solar_setup = Transition(label='Solar Setup')
crop_planning = Transition(label='Crop Planning')
stakeholder_meet = Transition(label='Stakeholder Meet')
material_order = Transition(label='Material Order')
system_install = Transition(label='System Install')
environmental_audit = Transition(label='Environmental Audit')
growth_monitoring = Transition(label='Growth Monitoring')
pest_control = Transition(label='Pest Control')
market_launch = Transition(label='Market Launch')

# Define the workflow
loop1 = OperatorPOWL(operator=Operator.LOOP, children=[load_testing, system_design, solar_setup, material_order, system_install])
loop2 = OperatorPOWL(operator=Operator.LOOP, children=[soil_sampling, water_testing, crop_planning, stakeholder_meet])
loop3 = OperatorPOWL(operator=Operator.LOOP, children=[environmental_audit, growth_monitoring, pest_control])
xor = OperatorPOWL(operator=Operator.XOR, children=[site_survey, permit_filing])
xor2 = OperatorPOWL(operator=Operator.XOR, children=[loop1, loop2, loop3])

# Define the partial order
root = StrictPartialOrder(nodes=[xor, xor2])
root.order.add_edge(xor, xor2)
root.order.add_edge(loop1, loop2)
root.order.add_edge(loop2, loop3)

print(root)