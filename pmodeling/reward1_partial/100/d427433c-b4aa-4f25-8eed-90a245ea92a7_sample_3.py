import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions for each activity
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

# Define loops and choices
milk_cycle = OperatorPOWL(operator=Operator.LOOP, children=[milk_collection, quality_testing, milk_blending, starter_culture, fermentation_check, curd_cutting, whey_separation, molding_press, salting_stage])
aging_control_loop = OperatorPOWL(operator=Operator.LOOP, children=[aging_control])
packaging_design_loop = OperatorPOWL(operator=Operator.LOOP, children=[packaging_design])
cold_shipping_loop = OperatorPOWL(operator=Operator.LOOP, children=[cold_shipping])
compliance_audit_loop = OperatorPOWL(operator=Operator.LOOP, children=[compliance_audit])
blockchain_log_loop = OperatorPOWL(operator=Operator.LOOP, children=[blockchain_log])
market_pricing_loop = OperatorPOWL(operator=Operator.LOOP, children=[market_pricing])
order_fulfillment_loop = OperatorPOWL(operator=Operator.LOOP, children=[order_fulfillment])
feedback_review_loop = OperatorPOWL(operator=Operator.LOOP, children=[feedback_review])

# Define exclusive choices
milk_cycle_choice = OperatorPOWL(operator=Operator.XOR, children=[milk_cycle, aging_control_loop])
packaging_design_choice = OperatorPOWL(operator=Operator.XOR, children=[packaging_design_loop, cold_shipping_loop])
compliance_audit_choice = OperatorPOWL(operator=Operator.XOR, children=[compliance_audit_loop, blockchain_log_loop])
market_pricing_choice = OperatorPOWL(operator=Operator.XOR, children=[market_pricing_loop, order_fulfillment_loop])
feedback_review_choice = OperatorPOWL(operator=Operator.XOR, children=[feedback_review_loop, market_pricing_choice])

# Define root node
root = StrictPartialOrder(nodes=[milk_cycle_choice, packaging_design_choice, compliance_audit_choice, market_pricing_choice, feedback_review_choice])
root.order.add_edge(milk_cycle_choice, packaging_design_choice)
root.order.add_edge(packaging_design_choice, compliance_audit_choice)
root.order.add_edge(compliance_audit_choice, market_pricing_choice)
root.order.add_edge(market_pricing_choice, feedback_review_choice)