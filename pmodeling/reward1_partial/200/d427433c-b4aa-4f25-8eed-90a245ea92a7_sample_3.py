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

# Define silent transitions
skip = SilentTransition()

# Define loops and XORs for the process
milk_collection_loop = OperatorPOWL(operator=Operator.LOOP, children=[milk_collection, quality_testing, milk_blending])
starter_culture_loop = OperatorPOWL(operator=Operator.LOOP, children=[starter_culture, fermentation_check, curd_cutting, whey_separation, molding_press, salting_stage, aging_control])
packaging_loop = OperatorPOWL(operator=Operator.LOOP, children=[packaging_design, cold_shipping, compliance_audit, blockchain_log])
pricing_loop = OperatorPOWL(operator=Operator.LOOP, children=[market_pricing, order_fulfillment, feedback_review])

# Define the root POWL model
root = StrictPartialOrder(nodes=[milk_collection_loop, starter_culture_loop, packaging_loop, pricing_loop])
root.order.add_edge(milk_collection_loop, starter_culture_loop)
root.order.add_edge(starter_culture_loop, packaging_loop)
root.order.add_edge(packaging_loop, pricing_loop)