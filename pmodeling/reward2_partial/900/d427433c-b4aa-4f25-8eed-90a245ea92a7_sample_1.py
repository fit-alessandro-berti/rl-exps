import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the POWL transitions
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

# Define the POWL operators
xor1 = OperatorPOWL(operator=Operator.XOR, children=[milk_collection, quality_testing])
xor2 = OperatorPOWL(operator=Operator.XOR, children=[milk_blending, starter_culture])
xor3 = OperatorPOWL(operator=Operator.XOR, children=[fermentation_check, curd_cutting])
xor4 = OperatorPOWL(operator=Operator.XOR, children=[whey_separation, molding_press])
xor5 = OperatorPOWL(operator=Operator.XOR, children=[salting_stage, aging_control])
xor6 = OperatorPOWL(operator=Operator.XOR, children=[packaging_design, cold_shipping])
xor7 = OperatorPOWL(operator=Operator.XOR, children=[compliance_audit, blockchain_log])
xor8 = OperatorPOWL(operator=Operator.XOR, children=[market_pricing, order_fulfillment])
xor9 = OperatorPOWL(operator=Operator.XOR, children=[feedback_review, order_fulfillment])

# Define the POWL partial order
root = StrictPartialOrder(nodes=[xor1, xor2, xor3, xor4, xor5, xor6, xor7, xor8, xor9])
root.order.add_edge(xor1, xor2)
root.order.add_edge(xor2, xor3)
root.order.add_edge(xor3, xor4)
root.order.add_edge(xor4, xor5)
root.order.add_edge(xor5, xor6)
root.order.add_edge(xor6, xor7)
root.order.add_edge(xor7, xor8)
root.order.add_edge(xor8, xor9)
root.order.add_edge(xor9, xor9)

# Print the final result
print(root)