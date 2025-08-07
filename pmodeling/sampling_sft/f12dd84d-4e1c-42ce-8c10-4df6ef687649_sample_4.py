import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define all activities as POWL transitions
milk_sourcing     = Transition(label='Milk Sourcing')
quality_testing   = Transition(label='Quality Testing')
curd_processing   = Transition(label='Curd Processing')
salt_application  = Transition(label='Salt Application')
mold_inoculation  = Transition(label='Mold Inoculation')
press_molding     = Transition(label='Press Molding')
brine_soaking     = Transition(label='Brine Soaking')
aging_setup       = Transition(label='Aging Setup')
humidity_control  = Transition(label='Humidity Control')
microbial_check   = Transition(label='Microbial Check')
packaging_design  = Transition(label='Packaging Design')
label_printing    = Transition(label='Label Printing')
trace_logging     = Transition(label='Trace Logging')
distribution_plan = Transition(label='Distribution Plan')
customer_review   = Transition(label='Customer Review')
inventory_audit   = Transition(label='Inventory Audit')
sustainability_audit = Transition(label='Sustainability Audit')

# Build the loop for continuous aging and quality checks
# Body A: Humidity Control -> Microbial Check
body_a = StrictPartialOrder(nodes=[humidity_control, microbial_check])
body_a.order.add_edge(humidity_control, microbial_check)

# Body B: Trace Logging -> Customer Review
body_b = StrictPartialOrder(nodes=[trace_logging, customer_review])
body_b.order.add_edge(trace_logging, customer_review)

# Loop: do Body A, then either exit or do Body B and repeat
aging_loop = OperatorPOWL(operator=Operator.LOOP, children=[body_a, body_b])

# Build the main partial order
root = StrictPartialOrder(nodes=[
    milk_sourcing,
    quality_testing,
    curd_processing,
    salt_application,
    mold_inoculation,
    press_molding,
    brine_soaking,
    aging_loop,
    packaging_design,
    label_printing,
    distribution_plan,
    inventory_audit,
    sustainability_audit
])

# Define the control-flow edges
root.order.add_edge(milk_sourcing, quality_testing)
root.order.add_edge(quality_testing, curd_processing)
root.order.add_edge(curd_processing, salt_application)
root.order.add_edge(salt_application, mold_inoculation)
root.order.add_edge(mold_inoculation, press_molding)
root.order.add_edge(press_molding, brine_soaking)
root.order.add_edge(brine_soaking, aging_loop)
root.order.add_edge(aging_loop, packaging_design)
root.order.add_edge(packaging_design, label_printing)
root.order.add_edge(label_printing, distribution_plan)
root.order.add_edge(distribution_plan, inventory_audit)
root.order.add_edge(inventory_audit, sustainability_audit)