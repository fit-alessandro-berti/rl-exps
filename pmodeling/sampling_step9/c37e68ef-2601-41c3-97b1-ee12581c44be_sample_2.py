import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions for each activity
milk_sourcing = Transition(label='Milk Sourcing')
quality_testing = Transition(label='Quality Testing')
starter_prep = Transition(label='Starter Prep')
curd_cutting = Transition(label='Curd Cutting')
whey_draining = Transition(label='Whey Draining')
molding_press = Transition(label='Molding Press')
fermentation_control = Transition(label='Fermentation Control')
aging_setup = Transition(label='Aging Setup')
humidity_check = Transition(label='Humidity Check')
packaging_design = Transition(label='Packaging Design')
label_approval = Transition(label='Label Approval')
inventory_audit = Transition(label='Inventory Audit')
order_scheduling = Transition(label='Order Scheduling')
market_delivery = Transition(label='Market Delivery')
feedback_review = Transition(label='Feedback Review')
compliance_check = Transition(label='Compliance Check')
marketing_sync = Transition(label='Marketing Sync')

# Define silent transitions
skip = SilentTransition()

# Define loop nodes for repetitive activities
fermentation_loop = OperatorPOWL(operator=Operator.LOOP, children=[fermentation_control, humidity_check])
aging_loop = OperatorPOWL(operator=Operator.LOOP, children=[aging_setup, humidity_check])

# Define exclusive choice nodes for branching activities
market_delivery_choice = OperatorPOWL(operator=Operator.XOR, children=[market_delivery, skip])

# Define the POWL model
root = StrictPartialOrder(nodes=[milk_sourcing, quality_testing, starter_prep, curd_cutting, whey_draining, molding_press, fermentation_loop, aging_loop, packaging_design, label_approval, inventory_audit, order_scheduling, market_delivery_choice, feedback_review, compliance_check, marketing_sync])
root.order.add_edge(milk_sourcing, quality_testing)
root.order.add_edge(quality_testing, starter_prep)
root.order.add_edge(starter_prep, curd_cutting)
root.order.add_edge(curd_cutting, whey_draining)
root.order.add_edge(whey_draining, molding_press)
root.order.add_edge(molding_press, fermentation_loop)
root.order.add_edge(fermentation_loop, aging_loop)
root.order.add_edge(aging_loop, packaging_design)
root.order.add_edge(packaging_design, label_approval)
root.order.add_edge(label_approval, inventory_audit)
root.order.add_edge(inventory_audit, order_scheduling)
root.order.add_edge(order_scheduling, market_delivery_choice)
root.order.add_edge(market_delivery_choice, feedback_review)
root.order.add_edge(feedback_review, compliance_check)
root.order.add_edge(compliance_check, marketing_sync)