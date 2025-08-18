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

# Define the POWL model
loop_fermentation = OperatorPOWL(operator=Operator.LOOP, children=[fermentation_control, aging_setup, humidity_check])
loop_storage = OperatorPOWL(operator=Operator.LOOP, children=[molding_press, whey_draining, curd_cutting])

xor_fermentation_control = OperatorPOWL(operator=Operator.XOR, children=[quality_testing, starter_prep])
xor_inventory_audit = OperatorPOWL(operator=Operator.XOR, children=[order_scheduling, market_delivery])

xor_feedback_review = OperatorPOWL(operator=Operator.XOR, children=[compliance_check, marketing_sync])

root = StrictPartialOrder(nodes=[milk_sourcing, xor_fermentation_control, loop_fermentation, xor_inventory_audit, xor_feedback_review])
root.order.add_edge(milk_sourcing, xor_fermentation_control)
root.order.add_edge(xor_fermentation_control, loop_fermentation)
root.order.add_edge(loop_fermentation, xor_inventory_audit)
root.order.add_edge(xor_inventory_audit, xor_feedback_review)
root.order.add_edge(xor_feedback_review, loop_storage)