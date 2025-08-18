import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions for each activity
milk_sourcing = Transition(label='Milk Sourcing')
quality_testing = Transition(label='Quality Testing')
curd_processing = Transition(label='Curd Processing')
salt_application = Transition(label='Salt Application')
mold_inoculation = Transition(label='Mold Inoculation')
press_molding = Transition(label='Press Molding')
brine_soaking = Transition(label='Brine Soaking')
aging_setup = Transition(label='Aging Setup')
humidity_control = Transition(label='Humidity Control')
microbial_check = Transition(label='Microbial Check')
packaging_design = Transition(label='Packaging Design')
label_printing = Transition(label='Label Printing')
trace_logging = Transition(label='Trace Logging')
distribution_plan = Transition(label='Distribution Plan')
customer_review = Transition(label='Customer Review')
inventory_audit = Transition(label='Inventory Audit')
sustainability_audit = Transition(label='Sustainability Audit')

# Define exclusive choices
xor1 = OperatorPOWL(operator=Operator.XOR, children=[quality_testing, salt_application])
xor2 = OperatorPOWL(operator=Operator.XOR, children=[mold_inoculation, press_molding])
xor3 = OperatorPOWL(operator=Operator.XOR, children=[brine_soaking, aging_setup])
xor4 = OperatorPOWL(operator=Operator.XOR, children=[humidity_control, microbial_check])
xor5 = OperatorPOWL(operator=Operator.XOR, children=[packaging_design, label_printing])
xor6 = OperatorPOWL(operator=Operator.XOR, children=[trace_logging, distribution_plan])
xor7 = OperatorPOWL(operator=Operator.XOR, children=[customer_review, inventory_audit])
xor8 = OperatorPOWL(operator=Operator.XOR, children=[sustainability_audit])

# Define partial order
root = StrictPartialOrder(nodes=[milk_sourcing, xor1, xor2, xor3, xor4, xor5, xor6, xor7, xor8])
root.order.add_edge(milk_sourcing, xor1)
root.order.add_edge(milk_sourcing, xor2)
root.order.add_edge(milk_sourcing, xor3)
root.order.add_edge(milk_sourcing, xor4)
root.order.add_edge(milk_sourcing, xor5)
root.order.add_edge(milk_sourcing, xor6)
root.order.add_edge(milk_sourcing, xor7)
root.order.add_edge(milk_sourcing, xor8)

# Print the root POWL model
print(root)