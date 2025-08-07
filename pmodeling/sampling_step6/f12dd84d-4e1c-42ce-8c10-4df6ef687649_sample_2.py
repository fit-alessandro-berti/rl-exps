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

# Define the partial order
root = StrictPartialOrder(nodes=[
    milk_sourcing,
    quality_testing,
    curd_processing,
    salt_application,
    mold_inoculation,
    press_molding,
    brine_soaking,
    aging_setup,
    humidity_control,
    microbial_check,
    packaging_design,
    label_printing,
    trace_logging,
    distribution_plan,
    customer_review,
    inventory_audit,
    sustainability_audit
])

# Add dependencies if necessary
# For example, if 'Milk Sourcing' is dependent on 'Quality Testing':
# root.order.add_edge(milk_sourcing, quality_testing)

# Now, 'root' is the final POWL model
print(root)