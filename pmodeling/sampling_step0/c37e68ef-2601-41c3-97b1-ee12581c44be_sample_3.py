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

# Define the operators
loop_fermentation = OperatorPOWL(operator=Operator.LOOP, children=[fermentation_control, aging_setup, humidity_check])
xor_compliance = OperatorPOWL(operator=Operator.XOR, children=[compliance_check, feedback_review])
xor_marketing = OperatorPOWL(operator=Operator.XOR, children=[marketing_sync, order_scheduling])
xor_inventory = OperatorPOWL(operator=Operator.XOR, children=[inventory_audit, market_delivery])
xor_packing = OperatorPOWL(operator=Operator.XOR, children=[packaging_design, label_approval])

# Define the root node
root = StrictPartialOrder(nodes=[loop_fermentation, xor_compliance, xor_marketing, xor_inventory, xor_packing])

# Add edges to the root node
root.order.add_edge(loop_fermentation, xor_compliance)
root.order.add_edge(loop_fermentation, xor_marketing)
root.order.add_edge(loop_fermentation, xor_inventory)
root.order.add_edge(loop_fermentation, xor_packing)

# Return the root node
root