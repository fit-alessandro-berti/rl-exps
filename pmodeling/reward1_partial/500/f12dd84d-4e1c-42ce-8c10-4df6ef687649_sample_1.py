import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the POWL nodes
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

# Define the POWL operators
exclusive_choice = OperatorPOWL(operator=Operator.XOR, children=[quality_testing, curd_processing])
loop = OperatorPOWL(operator=Operator.LOOP, children=[salt_application, mold_inoculation, press_molding, brine_soaking, aging_setup, humidity_control, microbial_check])
partial_order = OperatorPOWL(operator=Operator.PARTIAL_ORDER, children=[packaging_design, label_printing, trace_logging, distribution_plan, customer_review, inventory_audit, sustainability_audit])
partial_order.order.add_edge(packaging_design, label_printing)
partial_order.order.add_edge(label_printing, trace_logging)
partial_order.order.add_edge(trace_logging, distribution_plan)
partial_order.order.add_edge(distribution_plan, customer_review)
partial_order.order.add_edge(customer_review, inventory_audit)
partial_order.order.add_edge(inventory_audit, sustainability_audit)

# Define the root of the POWL model
root = StrictPartialOrder(nodes=[milk_sourcing, exclusive_choice, loop, partial_order])
root.order.add_edge(milk_sourcing, exclusive_choice)
root.order.add_edge(exclusive_choice, loop)
root.order.add_edge(loop, partial_order)

# Print the root of the POWL model
print(root)