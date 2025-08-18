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

# Define transitions for loop and exclusive choice
loop = OperatorPOWL(operator=Operator.LOOP, children=[starter_prep, curd_cutting, whey_draining, molding_press])
xor = OperatorPOWL(operator=Operator.XOR, children=[aging_setup, humidity_check])
xor2 = OperatorPOWL(operator=Operator.XOR, children=[packaging_design, label_approval])
xor3 = OperatorPOWL(operator=Operator.XOR, children=[inventory_audit, order_scheduling])
xor4 = OperatorPOWL(operator=Operator.XOR, children=[market_delivery, feedback_review])
xor5 = OperatorPOWL(operator=Operator.XOR, children=[compliance_check, marketing_sync])

# Define the root of the POWL model
root = StrictPartialOrder(nodes=[milk_sourcing, quality_testing, loop, xor, xor2, xor3, xor4, xor5])
root.order.add_edge(milk_sourcing, quality_testing)
root.order.add_edge(quality_testing, loop)
root.order.add_edge(loop, xor)
root.order.add_edge(xor, xor2)
root.order.add_edge(xor2, xor3)
root.order.add_edge(xor3, xor4)
root.order.add_edge(xor4, xor5)

print(root)