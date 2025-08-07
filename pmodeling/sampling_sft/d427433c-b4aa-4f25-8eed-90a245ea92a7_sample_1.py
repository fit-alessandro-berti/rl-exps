import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define the basic activities
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

# Build the loop for the cheese production cycle
production_loop = OperatorPOWL(operator=Operator.LOOP, children=[milk_collection,
                                                                 quality_testing,
                                                                 milk_blending,
                                                                 starter_culture,
                                                                 fermentation_check,
                                                                 curd_cutting,
                                                                 whey_separation,
                                                                 molding_press,
                                                                 salting_stage,
                                                                 aging_control])

# Build the pricing and feedback loop
pricing_loop = OperatorPOWL(operator=Operator.LOOP, children=[packaging_design,
                                                              cold_shipping,
                                                              compliance_audit,
                                                              blockchain_log,
                                                              market_pricing,
                                                              order_fulfillment,
                                                              feedback_review])

# Assemble the overall process as a partial order
root = StrictPartialOrder(nodes=[
    production_loop,
    pricing_loop
])
root.order.add_edge(production_loop, pricing_loop)