import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define activities
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
skip = SilentTransition()

# Define process structure
loop_fermentation = OperatorPOWL(operator=Operator.LOOP, children=[fermentation_control, aging_setup, humidity_check])
loop_packing = OperatorPOWL(operator=Operator.LOOP, children=[packaging_design, label_approval])
loop_inventory = OperatorPOWL(operator=Operator.LOOP, children=[inventory_audit, order_scheduling, market_delivery])
loop_compliance = OperatorPOWL(operator=Operator.LOOP, children=[compliance_check, marketing_sync])
xor_marketing = OperatorPOWL(operator=Operator.XOR, children=[loop_inventory, loop_compliance])

root = StrictPartialOrder(nodes=[loop_fermentation, loop_packing, xor_marketing])
root.order.add_edge(loop_fermentation, xor_marketing)
root.order.add_edge(loop_packing, xor_marketing)
root.order.add_edge(loop_inventory, xor_marketing)
root.order.add_edge(loop_compliance, xor_marketing)

# Print the POWL model
print(root)