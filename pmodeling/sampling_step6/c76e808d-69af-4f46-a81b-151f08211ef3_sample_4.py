import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the transitions for each activity
milk_sourcing = Transition(label='Milk Sourcing')
culture_selection = Transition(label='Culture Selection')
milk_testing = Transition(label='Milk Testing')
curd_formation = Transition(label='Curd Formation')
whey_separation = Transition(label='Whey Separation')
molding_cheese = Transition(label='Molding Cheese')
salting_process = Transition(label='Salting Process')
aging_setup = Transition(label='Aging Setup')
env_monitoring = Transition(label='Env Monitoring')
flavor_profiling = Transition(label='Flavor Profiling')
packaging_design = Transition(label='Packaging Design')
blockchain_entry = Transition(label='Blockchain Entry')
quality_audit = Transition(label='Quality Audit')
retail_sync = Transition(label='Retail Sync')
transport_prep = Transition(label='Transport Prep')
delivery_tracking = Transition(label='Delivery Tracking')
customer_feedback = Transition(label='Customer Feedback')

# Define the partial order structure
root = StrictPartialOrder(nodes=[
    milk_sourcing,
    culture_selection,
    milk_testing,
    curd_formation,
    whey_separation,
    molding_cheese,
    salting_process,
    aging_setup,
    env_monitoring,
    flavor_profiling,
    packaging_design,
    blockchain_entry,
    quality_audit,
    retail_sync,
    transport_prep,
    delivery_tracking,
    customer_feedback
])
# Since there are no dependencies between activities in this process, the order is implicit and not explicitly defined in the code above.