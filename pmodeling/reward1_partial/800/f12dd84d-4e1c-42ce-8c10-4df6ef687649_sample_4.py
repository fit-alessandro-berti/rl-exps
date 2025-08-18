import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the transitions (activities) in the process
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

# Define the control flow operators
# Exclusive choice between quality testing and curd processing
xor_quality_curd = OperatorPOWL(operator=Operator.XOR, children=[quality_testing, curd_processing])

# Loop for aging setup
loop_aging_setup = OperatorPOWL(operator=Operator.LOOP, children=[aging_setup, humidity_control, microbial_check])

# Loop for mold inoculation and press molding
loop_mold_press = OperatorPOWL(operator=Operator.LOOP, children=[mold_inoculation, press_molding])

# Loop for brine soaking
loop_brine_soaking = OperatorPOWL(operator=Operator.LOOP, children=[brine_soaking, salt_application])

# Define the root POWL model
root = StrictPartialOrder(nodes=[milk_sourcing, xor_quality_curd, loop_aging_setup, loop_mold_press, loop_brine_soaking, packaging_design, label_printing, trace_logging, distribution_plan, customer_review, inventory_audit, sustainability_audit])
root.order.add_edge(milk_sourcing, xor_quality_curd)
root.order.add_edge(xor_quality_curd, loop_aging_setup)
root.order.add_edge(loop_aging_setup, loop_mold_press)
root.order.add_edge(loop_mold_press, loop_brine_soaking)
root.order.add_edge(loop_brine_soaking, packaging_design)
root.order.add_edge(packaging_design, label_printing)
root.order.add_edge(label_printing, trace_logging)
root.order.add_edge(trace_logging, distribution_plan)
root.order.add_edge(distribution_plan, customer_review)
root.order.add_edge(customer_review, inventory_audit)
root.order.add_edge(inventory_audit, sustainability_audit)

# Print the root POWL model
print(root)