from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the POWL nodes
milk_collection = Transition(label='Milk Collection')
quality_testing = Transition(label='Quality Testing')
milk_blending = Transition(label='Milk Blending')
starter_culture = Transition(label='Starter Culture')
fermentation_check = Transition(label='Fermentation Check')
curd_cutting = Transition(label='Curd Cutting')
whey_separation = Transition(label='Whey Separation')
molding_press = Transition(label='Molding Press')
salting_stage = Transition(label='Salting Stage')
aging_control = Transition(label='Aging Control')
packaging_design = Transition(label='Packaging Design')
cold_shipping = Transition(label='Cold Shipping')
compliance_audit = Transition(label='Compliance Audit')
blockchain_log = Transition(label='Blockchain Log')
market_pricing = Transition(label='Market Pricing')
order_fulfillment = Transition(label='Order Fulfillment')
feedback_review = Transition(label='Feedback Review')

# Define the POWL operations
xor1 = OperatorPOWL(operator=Operator.XOR, children=[quality_testing, starter_culture])
xor2 = OperatorPOWL(operator=Operator.XOR, children=[milk_blending, xor1])
xor3 = OperatorPOWL(operator=Operator.XOR, children=[curd_cutting, whey_separation])
xor4 = OperatorPOWL(operator=Operator.XOR, children=[molding_press, salting_stage])
xor5 = OperatorPOWL(operator=Operator.XOR, children=[aging_control, xor4])
xor6 = OperatorPOWL(operator=Operator.XOR, children=[packaging_design, xor5])
xor7 = OperatorPOWL(operator=Operator.XOR, children=[cold_shipping, xor6])
xor8 = OperatorPOWL(operator=Operator.XOR, children=[compliance_audit, xor7])
xor9 = OperatorPOWL(operator=Operator.XOR, children=[blockchain_log, xor8])
xor10 = OperatorPOWL(operator=Operator.XOR, children=[market_pricing, xor9])
xor11 = OperatorPOWL(operator=Operator.XOR, children=[order_fulfillment, xor10])
xor12 = OperatorPOWL(operator=Operator.XOR, children=[feedback_review, xor11])

# Define the POWL root
root = StrictPartialOrder(nodes=[milk_collection, xor12])
root.order.add_edge(milk_collection, xor12)

print(root)