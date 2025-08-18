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

# Define the loop and choice nodes
loop = OperatorPOWL(operator=Operator.LOOP, children=[quality_testing, starter_prep, curd_cutting, whey_draining, molding_press, fermentation_control, aging_setup, humidity_check])
xor = OperatorPOWL(operator=Operator.XOR, children=[packaging_design, label_approval])
xor2 = OperatorPOWL(operator=Operator.XOR, children=[inventory_audit, order_scheduling])
xor3 = OperatorPOWL(operator=Operator.XOR, children=[market_delivery, feedback_review])
xor4 = OperatorPOWL(operator=Operator.XOR, children=[compliance_check, marketing_sync])
xor5 = OperatorPOWL(operator=Operator.XOR, children=[xor2, xor3])
xor6 = OperatorPOWL(operator=Operator.XOR, children=[xor4, xor5])

# Create the root POWL model
root = StrictPartialOrder(nodes=[loop, xor, xor2, xor3, xor4, xor5, xor6])
root.order.add_edge(loop, xor)
root.order.add_edge(xor, xor2)
root.order.add_edge(xor2, xor3)
root.order.add_edge(xor3, xor4)
root.order.add_edge(xor4, xor5)
root.order.add_edge(xor5, xor6)

print(root)