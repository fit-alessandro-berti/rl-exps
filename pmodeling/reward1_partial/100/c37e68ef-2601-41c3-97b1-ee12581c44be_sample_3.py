import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the transitions
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
xor = OperatorPOWL(operator=Operator.XOR, children=[milk_sourcing, quality_testing])
xor = OperatorPOWL(operator=Operator.XOR, children=[starter_prep, quality_testing])
xor = OperatorPOWL(operator=Operator.XOR, children=[curd_cutting, starter_prep])
xor = OperatorPOWL(operator=Operator.XOR, children=[whey_draining, curd_cutting])
xor = OperatorPOWL(operator=Operator.XOR, children=[molding_press, whey_draining])
xor = OperatorPOWL(operator=Operator.XOR, children=[fermentation_control, molding_press])
xor = OperatorPOWL(operator=Operator.XOR, children=[aging_setup, fermentation_control])
xor = OperatorPOWL(operator=Operator.XOR, children=[humidity_check, aging_setup])
xor = OperatorPOWL(operator=Operator.XOR, children=[packaging_design, humidity_check])
xor = OperatorPOWL(operator=Operator.XOR, children=[label_approval, packaging_design])
xor = OperatorPOWL(operator=Operator.XOR, children=[inventory_audit, label_approval])
xor = OperatorPOWL(operator=Operator.XOR, children=[order_scheduling, inventory_audit])
xor = OperatorPOWL(operator=Operator.XOR, children=[market_delivery, order_scheduling])
xor = OperatorPOWL(operator=Operator.XOR, children=[feedback_review, market_delivery])
xor = OperatorPOWL(operator=Operator.XOR, children=[compliance_check, feedback_review])
xor = OperatorPOWL(operator=Operator.XOR, children=[marketing_sync, compliance_check])

# Define the root of the POWL model
root = StrictPartialOrder(nodes=[xor])
root.order.add_edge(xor, xor)