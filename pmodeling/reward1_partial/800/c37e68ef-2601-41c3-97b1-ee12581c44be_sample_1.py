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
xor1 = OperatorPOWL(operator=Operator.XOR, children=[milk_sourcing, quality_testing])
xor2 = OperatorPOWL(operator=Operator.XOR, children=[starter_prep, curd_cutting])
xor3 = OperatorPOWL(operator=Operator.XOR, children=[whey_draining, molding_press])
xor4 = OperatorPOWL(operator=Operator.XOR, children=[fermentation_control, aging_setup])
xor5 = OperatorPOWL(operator=Operator.XOR, children=[humidity_check, packaging_design])
xor6 = OperatorPOWL(operator=Operator.XOR, children=[label_approval, inventory_audit])
xor7 = OperatorPOWL(operator=Operator.XOR, children=[order_scheduling, market_delivery])
xor8 = OperatorPOWL(operator=Operator.XOR, children=[feedback_review, compliance_check])
xor9 = OperatorPOWL(operator=Operator.XOR, children=[marketing_sync, inventory_audit])

# Create the root of the POWL model
root = StrictPartialOrder(nodes=[xor1, xor2, xor3, xor4, xor5, xor6, xor7, xor8, xor9])

# Add dependencies between activities
root.order.add_edge(xor1, xor2)
root.order.add_edge(xor2, xor3)
root.order.add_edge(xor3, xor4)
root.order.add_edge(xor4, xor5)
root.order.add_edge(xor5, xor6)
root.order.add_edge(xor6, xor7)
root.order.add_edge(xor7, xor8)
root.order.add_edge(xor8, xor9)
root.order.add_edge(xor9, xor6)

# Print the root of the POWL model
print(root)