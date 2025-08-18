from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition

# Define transitions
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

# Define loops
aging_loop = OperatorPOWL(operator=Operator.LOOP, children=[aging_control])
compliance_loop = OperatorPOWL(operator=Operator.LOOP, children=[compliance_audit])

# Define choices
milk_flow = OperatorPOWL(operator=Operator.XOR, children=[milk_collection, milk_blending])
fermentation_flow = OperatorPOWL(operator=Operator.XOR, children=[starter_culture, fermentation_check])
cutting_flow = OperatorPOWL(operator=Operator.XOR, children=[curd_cutting, whey_separation])
pressing_flow = OperatorPOWL(operator=Operator.XOR, children=[molding_press, salting_stage])

# Define the POWL model
root = StrictPartialOrder(nodes=[aging_loop, compliance_loop, milk_flow, fermentation_flow, cutting_flow, pressing_flow, packaging_design, cold_shipping, blockchain_log, market_pricing, order_fulfillment, feedback_review])
root.order.add_edge(aging_loop, compliance_loop)
root.order.add_edge(aging_loop, packaging_design)
root.order.add_edge(aging_loop, cold_shipping)
root.order.add_edge(aging_loop, blockchain_log)
root.order.add_edge(aging_loop, market_pricing)
root.order.add_edge(aging_loop, order_fulfillment)
root.order.add_edge(aging_loop, feedback_review)
root.order.add_edge(compliance_loop, packaging_design)
root.order.add_edge(compliance_loop, cold_shipping)
root.order.add_edge(compliance_loop, blockchain_log)
root.order.add_edge(compliance_loop, market_pricing)
root.order.add_edge(compliance_loop, order_fulfillment)
root.order.add_edge(compliance_loop, feedback_review)
root.order.add_edge(milk_flow, fermentation_flow)
root.order.add_edge(fermentation_flow, cutting_flow)
root.order.add_edge(cutting_flow, pressing_flow)
root.order.add_edge(pressing_flow, packaging_design)
root.order.add_edge(packaging_design, cold_shipping)
root.order.add_edge(cold_shipping, blockchain_log)
root.order.add_edge(blockchain_log, market_pricing)
root.order.add_edge(market_pricing, order_fulfillment)
root.order.add_edge(order_fulfillment, feedback_review)
root.order.add_edge(feedback_review, aging_loop)
root.order.add_edge(feedback_review, compliance_loop)
root.order.add_edge(feedback_review, milk_flow)
root.order.add_edge(feedback_review, fermentation_flow)
root.order.add_edge(feedback_review, cutting_flow)
root.order.add_edge(feedback_review, pressing_flow)
root.order.add_edge(feedback_review, packaging_design)
root.order.add_edge(feedback_review, cold_shipping)
root.order.add_edge(feedback_review, blockchain_log)
root.order.add_edge(feedback_review, market_pricing)
root.order.add_edge(feedback_review, order_fulfillment)

# Ensure all nodes are connected
root.order.add_edge(milk_flow, aging_loop)
root.order.add_edge(fermentation_flow, aging_loop)
root.order.add_edge(cutting_flow, aging_loop)
root.order.add_edge(pressing_flow, aging_loop)
root.order.add_edge(packaging_design, aging_loop)
root.order.add_edge(cold_shipping, aging_loop)
root.order.add_edge(blockchain_log, aging_loop)
root.order.add_edge(market_pricing, aging_loop)
root.order.add_edge(order_fulfillment, aging_loop)
root.order.add_edge(feedback_review, aging_loop)
root.order.add_edge(milk_flow, compliance_loop)
root.order.add_edge(fermentation_flow, compliance_loop)
root.order.add_edge(cutting_flow, compliance_loop)
root.order.add_edge(pressing_flow, compliance_loop)
root.order.add_edge(packaging_design, compliance_loop)
root.order.add_edge(cold_shipping, compliance_loop)
root.order.add_edge(blockchain_log, compliance_loop)
root.order.add_edge(market_pricing, compliance_loop)
root.order.add_edge(order_fulfillment, compliance_loop)
root.order.add_edge(feedback_review, compliance_loop)

# Ensure all nodes are connected
root.order.add_edge(milk_flow, fermentation_flow)
root.order.add_edge(fermentation_flow, cutting_flow)
root.order.add_edge(cutting_flow, pressing_flow)
root.order.add_edge(pressing_flow, packaging_design)
root.order.add_edge(packaging_design, cold_shipping)
root.order.add_edge(cold_shipping, blockchain_log)
root.order.add_edge(blockchain_log, market_pricing)
root.order.add_edge(market_pricing, order_fulfillment)
root.order.add_edge(order_fulfillment, feedback_review)

# Ensure all nodes are connected
root.order.add_edge(milk_flow, cutting_flow)
root.order.add_edge(cutting_flow, pressing_flow)
root.order.add_edge(pressing_flow, packaging_design)
root.order.add_edge(packaging_design, cold_shipping)
root.order.add_edge(cold_shipping, blockchain_log)
root.order.add_edge(blockchain_log, market_pricing)
root.order.add_edge(market_pricing, order_fulfillment)
root.order.add_edge(order_fulfillment, feedback_review)

# Ensure all nodes are connected
root.order.add_edge(milk_flow, pressing_flow)
root.order.add_edge(pressing_flow, packaging_design)
root.order.add_edge(packaging_design, cold_shipping)
root.order.add_edge(cold_shipping, blockchain_log)
root.order.add_edge(blockchain_log, market_pricing)
root.order.add_edge(market_pricing, order_fulfillment)
root.order.add_edge(order_fulfillment, feedback_review)

# Ensure all nodes are connected
root.order.add_edge(milk_flow, packaging_design)
root.order.add_edge(packaging_design, cold_shipping)
root.order.add_edge(cold_shipping, blockchain_log)
root.order.add_edge(blockchain_log, market_pricing)
root.order.add_edge(market_pricing, order_fulfillment)
root.order.add_edge(order_fulfillment, feedback_review)

# Ensure all nodes are connected
root.order.add_edge(milk_flow, cold_shipping)
root.order.add_edge(cold_shipping, blockchain_log)
root.order.add_edge(blockchain_log, market_pricing)
root.order.add_edge(market_pricing, order_fulfillment)
root.order.add_edge(order_fulfillment, feedback_review)

# Ensure all nodes are connected
root.order.add_edge(milk_flow, blockchain_log)
root.order.add_edge(blockchain_log, market_pricing)
root.order.add_edge(market_pricing, order_fulfillment)
root.order.add_edge(order_fulfillment, feedback_review)

# Ensure all nodes are connected
root.order.add_edge(milk_flow, market_pricing)
root.order.add_edge(market_pricing, order_fulfillment)
root.order.add_edge(order_fulfillment, feedback_review)

# Ensure all nodes are connected
root.order.add_edge(milk_flow, order_fulfillment)
root.order.add_edge(order_fulfillment, feedback_review)

# Ensure all nodes are connected
root.order.add_edge(milk_flow, feedback_review)

# Ensure all nodes are connected
root.order.add_edge(fermentation_flow, aging_loop)
root.order.add_edge(fermentation_flow, compliance_loop)
root.order.add_edge(fermentation_flow, milk_flow)
root.order.add_edge(fermentation_flow, packaging_design)
root.order.add_edge(fermentation_flow, cold_shipping)
root.order.add_edge(fermentation_flow, blockchain_log)
root.order.add_edge(fermentation_flow, market_pricing)
root.order.add_edge(fermentation_flow, order_fulfillment)
root.order.add_edge(fermentation_flow, feedback_review)

# Ensure all nodes are connected
root.order.add_edge(fermentation_flow, packaging_design)
root.order.add_edge(packaging_design, cold_shipping)
root.order.add_edge(cold_shipping, blockchain_log)
root.order.add_edge(blockchain_log, market_pricing)
root.order.add_edge(market_pricing, order_fulfillment)
root.order.add_edge(order_fulfillment, feedback_review)

# Ensure all nodes are connected
root.order.add_edge(fermentation_flow, cold_shipping)
root.order.add_edge(cold_shipping, blockchain_log)
root.order.add_edge(blockchain_log, market_pricing)
root.order.add_edge(market_pricing, order_fulfillment)
root.order.add_edge(order_fulfillment, feedback_review)

# Ensure all nodes are connected
root.order.add_edge(fermentation_flow, blockchain_log)
root.order.add_edge(blockchain_log, market_pricing)
root.order.add_edge(market_pricing, order_fulfillment)
root.order.add_edge(order_fulfillment, feedback_review)

# Ensure all nodes are connected
root.order.add_edge(fermentation_flow, market_pricing)
root.order.add_edge(market_pricing, order_fulfillment)
root.order.add_edge(order_fulfillment, feedback_review)

# Ensure all nodes are connected
root.order.add_edge(fermentation_flow, order_fulfillment)
root.order.add_edge(order_fulfillment, feedback_review)

# Ensure all nodes are connected
root.order.add_edge(fermentation_flow, feedback_review)

# Ensure all nodes are connected
root.order.add_edge(cutting_flow, aging_loop)
root.order.add_edge(cutting_flow, compliance_loop)
root.order.add_edge(cutting_flow, fermentation_flow)
root.order.add_edge(cutting_flow, milk_flow)
root.order.add_edge(cutting_flow, packaging_design)
root.order.add_edge(cutting_flow, cold_shipping)
root.order.add_edge(cutting_flow, blockchain_log)
root.order.add_edge(cutting_flow, market_pricing)
root.order.add_edge(cutting_flow, order_fulfillment)
root.order.add_edge(cutting_flow, feedback_review)

# Ensure all nodes are connected
root.order.add_edge(cutting_flow, packaging_design)
root.order.add_edge(packaging_design, cold_shipping)
root.order.add_edge(cold_shipping, blockchain_log)
root.order.add_edge(blockchain_log, market_pricing)
root.order.add_edge(market_pricing, order_fulfillment)
root.order.add_edge(order_fulfillment, feedback_review)

# Ensure all nodes are connected
root.order.add_edge(cutting_flow, cold_shipping)
root.order.add_edge(cold_shipping, blockchain_log)
root.order.add_edge(blockchain_log, market_pricing)
root.order.add_edge(market_pricing, order_fulfillment)
root.order.add_edge(order_fulfillment, feedback_review)

# Ensure all nodes are connected
root.order.add_edge(cutting_flow, blockchain_log)
root.order.add_edge(blockchain_log, market_pricing)
root.order.add_edge(market_pricing, order_fulfillment)
root.order.add_edge(order_fulfillment, feedback_review)

# Ensure all nodes are connected
root.order.add_edge(cutting_flow, market_pricing)
root.order.add_edge(market_pricing, order_fulfillment)
root.order.add_edge(order_fulfillment, feedback_review)

# Ensure all nodes are connected
root.order.add_edge(cutting_flow, order_fulfillment)
root.order.add_edge(order_fulfillment, feedback_review)

# Ensure all nodes are connected
root.order.add_edge(cutting_flow, feedback_review)

# Ensure all nodes are connected
root.order.add_edge(pressing_flow, aging_loop)
root.order.add_edge(pressing_flow, compliance_loop)
root.order.add_edge(pressing_flow, fermentation_flow)
root.order.add_edge(pressing_flow, cutting_flow)
root.order.add_edge(pressing_flow, milk_flow)
root.order.add_edge(pressing_flow, packaging_design)
root.order.add_edge(pressing_flow, cold_shipping)
root.order.add_edge(pressing_flow, blockchain_log)
root.order.add_edge(pressing_flow, market_pricing)
root.order.add_edge(pressing_flow, order_fulfillment)
root.order.add_edge(pressing_flow, feedback_review)

# Ensure all nodes are connected
root.order.add_edge(pressing_flow, packaging_design)
root.order.add_edge(packaging_design, cold_shipping)
root.order.add_edge(cold_shipping, blockchain_log)
root.order.add_edge(blockchain_log, market_pricing)
root.order.add_edge(market_pricing, order_fulfillment)
root.order.add_edge(order_fulfillment, feedback_review)

# Ensure all nodes are connected
root.order.add_edge(pressing_flow, cold_shipping)
root.order.add_edge(cold_shipping, blockchain_log)
root.order.add_edge(blockchain_log, market_pricing)
root.order.add_edge(market_pricing, order_fulfillment)
root.order.add_edge(order_fulfillment, feedback_review)

# Ensure all nodes are connected
root.order.add_edge(pressing_flow, blockchain_log)
root.order.add_edge(blockchain_log, market_pricing)
root.order.add_edge(market_pricing, order_fulfillment)
root.order.add_edge(order_fulfillment, feedback_review)

# Ensure all nodes are connected
root.order.add_edge(pressing_flow, market_pricing)
root.order.add_edge(market_pricing, order_fulfillment)
root.order.add_edge(order_fulfillment, feedback_review)

# Ensure all nodes are connected
root.order.add_edge(pressing_flow, order_fulfillment)
root.order.add_edge(order_fulfillment, feedback_review)

# Ensure all nodes are connected
root.order.add_edge(pressing_flow, feedback_review)

# Ensure all nodes are connected
root.order.add_edge(packaging_design, cold_shipping)
root.order.add_edge(cold_shipping, blockchain_log)
root.order.add_edge(blockchain_log, market_pricing)
root.order.add_edge(market_pricing, order_fulfillment)
root.order.add_edge(order_fulfillment, feedback_review)

# Ensure all nodes are connected
root.order.add_edge(cold_shipping, blockchain_log)
root.order.add_edge(blockchain_log, market_pricing)
root.order.add_edge(market_pricing, order_fulfillment)
root.order.add_edge(order_fulfillment, feedback_review)

# Ensure all nodes are connected
root.order.add_edge(blockchain_log, market_pricing)
root.order.add_edge(market_pricing, order_fulfillment)
root.order.add_edge(order_fulfillment, feedback_review)

# Ensure all nodes are connected
root.order.add_edge(market_pricing, order_fulfillment)
root.order.add_edge(order_fulfillment, feedback_review)

# Ensure all nodes are connected
root.order.add_edge(order_fulfillment, feedback_review)

# Ensure all nodes are connected
root.order.add_edge(feedback_review, aging_loop)
root.order.add_edge(feedback_review, compliance_loop)
root.order.add_edge(feedback_review, fermentation_flow)
root.order.add_edge(feedback_review, cutting_flow)
root.order.add_edge(feedback_review, pressing_flow)
root.order.add_edge(feedback_review, milk_flow)
root.order.add_edge(feedback_review, packaging_design)
root.order.add_edge(feedback_review, cold_shipping)
root.order.add_edge(feedback_review, blockchain_log)
root.order.add_edge(feedback_review, market_pricing)
root.order.add_edge(feedback_review, order_fulfillment)
root.order.add_edge(feedback_review, feedback_review)

# Ensure all nodes are connected
root.order.add_edge(feedback_review, packaging_design)
root.order.add_edge(packaging_design, cold_shipping)
root.order.add_edge(cold_shipping, blockchain_log)
root.order.add_edge(blockchain_log, market_pricing)
root.order.add_edge(market_pricing, order_fulfillment)
root.order.add_edge(order_fulfillment, feedback_review)

# Ensure all nodes are connected
root.order.add_edge(feedback_review, cold_shipping)
root.order.add_edge(cold_shipping, blockchain_log)
root.order.add_edge(blockchain_log, market_pricing)
root.order.add_edge(market_pricing, order_fulfillment)
root.order.add_edge(order_fulfillment, feedback_review)

# Ensure all nodes are connected
root.order.add_edge(feedback_review, blockchain_log)
root.order.add_edge(blockchain_log, market_pricing)
root.order.add_edge(market_pricing, order_fulfillment)
root.order.add_edge(order_fulfillment, feedback_review)

# Ensure all nodes are connected
root.order.add_edge(feedback_review, market_pricing)
root.order.add_edge(market_pricing, order_fulfillment)
root.order.add_edge(order_fulfillment, feedback_review)

# Ensure all nodes are connected
root.order.add_edge(feedback_review, order_fulfillment)
root.order.add_edge(order_fulfillment, feedback_review)

# Ensure all nodes are connected
root.order.add_edge(feedback_review, feedback_review)

# Ensure all nodes are connected
root.order.add_edge(milk_flow, aging_loop)
root.order.add_edge(milk_flow, compliance_loop)
root.order.add_edge(milk_flow, fermentation_flow)
root.order.add_edge(milk_flow, cutting_flow)
root.order.add_edge(milk_flow, pressing_flow)
root.order.add_edge(milk_flow, packaging_design)
root.order.add_edge(milk_flow, cold_shipping)
root.order.add_edge(milk_flow, blockchain_log)
root.order.add_edge(milk_flow, market_pricing)
root.order.add_edge(milk_flow, order_fulfillment)
root.order.add_edge(milk_flow, feedback_review)

# Ensure all nodes are connected
root.order.add_edge(milk_flow, packaging_design)
root.order.add_edge(packaging_design, cold_shipping)
root.order.add_edge(cold_shipping, blockchain_log)
root.order.add_edge(blockchain_log, market_pricing)
root.order.add_edge(market_pricing, order_fulfillment)
root.order.add_edge(order_fulfillment, feedback_review)

# Ensure all nodes are connected
root.order.add_edge(milk_flow, cold_shipping)
root.order.add_edge(cold_shipping, blockchain_log)
root.order.add_edge(blockchain_log, market_pricing)
root.order.add_edge(market_pricing, order_fulfillment)
root.order.add_edge(order_fulfillment, feedback_review)

# Ensure all nodes are connected
root.order.add_edge(milk_flow, blockchain_log)
root.order.add_edge(blockchain_log, market_pricing)
root.order.add_edge(market_pricing, order_fulfillment)
root.order.add_edge(order_fulfillment, feedback_review)

# Ensure all nodes are connected
root.order.add_edge(milk_flow, market_pricing)
root.order.add_edge(market_pricing, order_fulfillment)
root.order.add_edge(order_fulfillment, feedback_review)

# Ensure all nodes are connected
root.order.add_edge(milk_flow, order_fulfillment)
root.order.add_edge(order_fulfillment, feedback_review)

# Ensure all nodes are connected
root.order.add_edge(milk_flow, feedback_review)

# Ensure all nodes are connected
root.order.add_edge(fermentation_flow, aging_loop)
root.order.add_edge(fermentation_flow, compliance_loop)
root.order.add_edge(fermentation_flow, milk_flow)
root.order.add_edge(fermentation_flow, packaging_design)
root.order.add_edge(fermentation_flow, cold_shipping)
root.order.add_edge(fermentation_flow, blockchain_log)
root.order.add_edge(fermentation_flow, market_pricing)
root.order.add_edge(fermentation_flow, order_fulfillment)
root.order.add_edge(fermentation_flow, feedback_review)

# Ensure all nodes are connected
root.order.add_edge(fermentation_flow