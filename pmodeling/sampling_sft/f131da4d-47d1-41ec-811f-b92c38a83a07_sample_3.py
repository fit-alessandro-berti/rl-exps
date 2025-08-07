import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define all activities
milk_sourcing      = Transition(label='Milk Sourcing')
culture_selection  = Transition(label='Culture Selection')
milk_testing       = Transition(label='Milk Testing')
fermentation_start = Transition(label='Fermentation Start')
temperature_ctrl   = Transition(label='Temperature Control')
ph_monitoring      = Transition(label='pH Monitoring')
curd_cutting       = Transition(label='Curd Cutting')
whey_draining      = Transition(label='Whey Draining')
molding_cheese     = Transition(label='Molding Cheese')
salting_process    = Transition(label='Salting Process')
aging_setup        = Transition(label='Aging Setup')
quality_check      = Transition(label='Quality Check')
packaging_prep     = Transition(label='Packaging Prep')
label_design       = Transition(label='Label Design')
distribution_plan  = Transition(label='Distribution Plan')
retail_delivery    = Transition(label='Retail Delivery')
customer_feedback  = Transition(label='Customer Feedback')

# Loop for continuous aging and quality checks
aging_loop = OperatorPOWL(
    operator=Operator.LOOP,
    children=[aging_setup, quality_check]
)

# Build the overall partial order
root = StrictPartialOrder(nodes=[
    milk_sourcing,
    culture_selection,
    milk_testing,
    fermentation_start,
    temperature_ctrl,
    ph_monitoring,
    curd_cutting,
    whey_draining,
    molding_cheese,
    salting_process,
    aging_loop,
    packaging_prep,
    label_design,
    distribution_plan,
    retail_delivery,
    customer_feedback
])

# Define the control-flow dependencies
root.order.add_edge(milk_sourcing, culture_selection)
root.order.add_edge(milk_sourcing, milk_testing)
root.order.add_edge(culture_selection, fermentation_start)
root.order.add_edge(milk_testing, fermentation_start)
root.order.add_edge(fermentation_start, temperature_ctrl)
root.order.add_edge(fermentation_start, ph_monitoring)
root.order.add_edge(temperature_ctrl, curd_cutting)
root.order.add_edge(temperature_ctrl, whey_draining)
root.order.add_edge(ph_monitoring, curd_cutting)
root.order.add_edge(ph_monitoring, whey_draining)
root.order.add_edge(curd_cutting, molding_cheese)
root.order.add_edge(whey_draining, molding_cheese)
root.order.add_edge(molding_cheese, salting_process)
root.order.add_edge(salting_process, aging_setup)
root.order.add_edge(aging_setup, quality_check)
root.order.add_edge(aging_loop, packaging_prep)
root.order.add_edge(packaging_prep, label_design)
root.order.add_edge(label_design, distribution_plan)
root.order.add_edge(distribution_plan, retail_delivery)
root.order.add_edge(retail_delivery, customer_feedback)

# Close the loop: after feedback, the process can repeat
root.order.add_edge(customer_feedback, milk_sourcing)