import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the activities
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

# Define the process
loop1 = OperatorPOWL(operator=Operator.LOOP, children=[quality_testing, starter_prep, curd_cutting, whey_draining, molding_press])
xor1 = OperatorPOWL(operator=Operator.XOR, children=[fermentation_control, humidity_check])
loop2 = OperatorPOWL(operator=Operator.LOOP, children=[packaging_design, label_approval])
xor2 = OperatorPOWL(operator=Operator.XOR, children=[inventory_audit, order_scheduling])
loop3 = OperatorPOWL(operator=Operator.LOOP, children=[market_delivery, feedback_review])
xor3 = OperatorPOWL(operator=Operator.XOR, children=[compliance_check, marketing_sync])

# Define the partial order
root = StrictPartialOrder(nodes=[loop1, xor1, loop2, xor2, loop3, xor3])
root.order.add_edge(loop1, xor1)
root.order.add_edge(xor1, loop2)
root.order.add_edge(loop2, xor2)
root.order.add_edge(xor2, loop3)
root.order.add_edge(loop3, xor3)

# Print the root node
print(root)