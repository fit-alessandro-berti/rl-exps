from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the transitions
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

# Define the order
root.order.add_edge(milk_sourcing, quality_testing)
root.order.add_edge(quality_testing, curd_processing)
root.order.add_edge(curd_processing, salt_application)
root.order.add_edge(salt_application, mold_inoculation)
root.order.add_edge(mold_inoculation, press_molding)
root.order.add_edge(press_molding, brine_soaking)
root.order.add_edge(brine_soaking, aging_setup)
root.order.add_edge(aging_setup, humidity_control)
root.order.add_edge(humidity_control, microbial_check)
root.order.add_edge(microbial_check, packaging_design)
root.order.add_edge(packaging_design, label_printing)
root.order.add_edge(label_printing, trace_logging)
root.order.add_edge(trace_logging, distribution_plan)
root.order.add_edge(distribution_plan, customer_review)
root.order.add_edge(customer_review, inventory_audit)
root.order.add_edge(inventory_audit, sustainability_audit)

print(root)