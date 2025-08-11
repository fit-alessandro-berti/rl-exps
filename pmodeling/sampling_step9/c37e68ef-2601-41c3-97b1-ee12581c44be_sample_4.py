import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the POWL model for the artisan cheese production process
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

# Define the POWL model
loop_fermentation = OperatorPOWL(operator=Operator.LOOP, children=[fermentation_control])
loop_aging = OperatorPOWL(operator=Operator.LOOP, children=[aging_setup])
xor_compliance = OperatorPOWL(operator=Operator.XOR, children=[compliance_check, SilentTransition()])
xor_marketing = OperatorPOWL(operator=Operator.XOR, children=[marketing_sync, SilentTransition()])
xor_inventory = OperatorPOWL(operator=Operator.XOR, children=[inventory_audit, SilentTransition()])

# Define the partial order
root = StrictPartialOrder(nodes=[milk_sourcing, quality_testing, starter_prep, curd_cutting, whey_draining, molding_press, loop_fermentation, loop_aging, packaging_design, label_approval, order_scheduling, market_delivery, feedback_review, xor_compliance, xor_marketing, xor_inventory])
root.order.add_edge(milk_sourcing, quality_testing)
root.order.add_edge(quality_testing, starter_prep)
root.order.add_edge(starter_prep, curd_cutting)
root.order.add_edge(curd_cutting, whey_draining)
root.order.add_edge(whey_draining, molding_press)
root.order.add_edge(molding_press, loop_fermentation)
root.order.add_edge(loop_fermentation, loop_aging)
root.order.add_edge(loop_aging, packaging_design)
root.order.add_edge(packaging_design, label_approval)
root.order.add_edge(label_approval, order_scheduling)
root.order.add_edge(order_scheduling, market_delivery)
root.order.add_edge(market_delivery, feedback_review)
root.order.add_edge(feedback_review, xor_compliance)
root.order.add_edge(feedback_review, xor_marketing)
root.order.add_edge(xor_compliance, xor_inventory)
root.order.add_edge(xor_marketing, xor_inventory)

# Print the final result
print(root)