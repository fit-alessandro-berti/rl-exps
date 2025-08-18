import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the transitions (activities)
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

# Define the control-flow operators
xor1 = OperatorPOWL(operator=Operator.XOR, children=[site_survey, permit_filing])
xor2 = OperatorPOWL(operator=Operator.XOR, children=[load_testing, soil_sampling])
xor3 = OperatorPOWL(operator=Operator.XOR, children=[water_testing, system_design])
xor4 = OperatorPOWL(operator=Operator.XOR, children=[solar_setup, crop_planning])
xor5 = OperatorPOWL(operator=Operator.XOR, children=[stakeholder_meet, material_order])
xor6 = OperatorPOWL(operator=Operator.XOR, children=[system_install, environmental_audit])
xor7 = OperatorPOWL(operator=Operator.XOR, children=[growth_monitoring, pest_control])
xor8 = OperatorPOWL(operator=Operator.XOR, children=[market_launch, SilentTransition()])  # SilentTransition() represents a loop exit

# Define the partial order
root = StrictPartialOrder(nodes=[xor1, xor2, xor3, xor4, xor5, xor6, xor7, xor8])
root.order.add_edge(xor1, xor2)
root.order.add_edge(xor2, xor3)
root.order.add_edge(xor3, xor4)
root.order.add_edge(xor4, xor5)
root.order.add_edge(xor5, xor6)
root.order.add_edge(xor6, xor7)
root.order.add_edge(xor7, xor8)