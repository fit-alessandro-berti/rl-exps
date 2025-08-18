import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions for each activity
milk_sourcing = Transition(label='Milk Sourcing')
culture_selection = Transition(label='Culture Selection')
milk_pasteurize = Transition(label='Milk Pasteurize')
curd_formation = Transition(label='Curd Formation')
whey_separation = Transition(label='Whey Separation')
mold_inoculate = Transition(label='Mold Inoculate')
cheese_pressing = Transition(label='Cheese Pressing')
aging_setup = Transition(label='Aging Setup')
humidity_control = Transition(label='Humidity Control')
flavor_testing = Transition(label='Flavor Testing')
packaging_design = Transition(label='Packaging Design')
label_approval = Transition(label='Label Approval')
order_forecast = Transition(label='Order Forecast')
regulation_audit = Transition(label='Regulation Audit')
waste_recycling = Transition(label='Waste Recycling')
market_delivery = Transition(label='Market Delivery')
customer_feedback = Transition(label='Customer Feedback')

# Define the loop for the aging process
aging_loop = OperatorPOWL(operator=Operator.LOOP, children=[aging_setup, humidity_control, mold_inoculate, cheese_pressing, flavor_testing])

# Define the XOR for the cheese production steps
production_xor = OperatorPOWL(operator=Operator.XOR, children=[aging_loop, waste_recycling])

# Define the XOR for the quality assurance steps
quality_assurance_xor = OperatorPOWL(operator=Operator.XOR, children=[flavor_testing, market_delivery])

# Define the XOR for the regulatory compliance steps
regulatory_compliance_xor = OperatorPOWL(operator=Operator.XOR, children=[regulation_audit, label_approval])

# Define the XOR for the order fulfillment steps
order_fulfillment_xor = OperatorPOWL(operator=Operator.XOR, children=[order_forecast, customer_feedback])

# Define the XOR for the waste recycling steps
waste_recycling_xor = OperatorPOWL(operator=Operator.XOR, children=[waste_recycling, market_delivery])

# Define the XOR for the packaging design steps
packaging_design_xor = OperatorPOWL(operator=Operator.XOR, children=[packaging_design, label_approval])

# Define the XOR for the customer feedback steps
customer_feedback_xor = OperatorPOWL(operator=Operator.XOR, children=[customer_feedback, market_delivery])

# Define the XOR for the milk sourcing steps
milk_sourcing_xor = OperatorPOWL(operator=Operator.XOR, children=[milk_sourcing, culture_selection])

# Define the XOR for the milk processing steps
milk_processing_xor = OperatorPOWL(operator=Operator.XOR, children=[milk_pasteurize, curd_formation, whey_separation])

# Define the XOR for the cheese production steps
cheese_production_xor = OperatorPOWL(operator=Operator.XOR, children=[milk_processing_xor, mold_inoculate, cheese_pressing, aging_loop])

# Define the XOR for the quality assurance steps
quality_assurance_xor = OperatorPOWL(operator=Operator.XOR, children=[flavor_testing, market_delivery])

# Define the XOR for the regulatory compliance steps
regulatory_compliance_xor = OperatorPOWL(operator=Operator.XOR, children=[regulation_audit, label_approval])

# Define the XOR for the order fulfillment steps
order_fulfillment_xor = OperatorPOWL(operator=Operator.XOR, children=[order_forecast, customer_feedback])

# Define the XOR for the waste recycling steps
waste_recycling_xor = OperatorPOWL(operator=Operator.XOR, children=[waste_recycling, market_delivery])

# Define the XOR for the packaging design steps
packaging_design_xor = OperatorPOWL(operator=Operator.XOR, children=[packaging_design, label_approval])

# Define the XOR for the customer feedback steps
customer_feedback_xor = OperatorPOWL(operator=Operator.XOR, children=[customer_feedback, market_delivery])

# Define the root node with all the XORs
root = StrictPartialOrder(nodes=[milk_sourcing_xor, milk_processing_xor, cheese_production_xor, quality_assurance_xor, regulatory_compliance_xor, order_fulfillment_xor, waste_recycling_xor, packaging_design_xor, customer_feedback_xor])
root.order.add_edge(milk_sourcing_xor, milk_processing_xor)
root.order.add_edge(milk_processing_xor, cheese_production_xor)
root.order.add_edge(cheese_production_xor, quality_assurance_xor)
root.order.add_edge(quality_assurance_xor, regulatory_compliance_xor)
root.order.add_edge(regulatory_compliance_xor, order_fulfillment_xor)
root.order.add_edge(order_fulfillment_xor, waste_recycling_xor)
root.order.add_edge(waste_recycling_xor, packaging_design_xor)
root.order.add_edge(packaging_design_xor, customer_feedback_xor)