import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the transitions (activities)
milk_sourcing = Transition(label='Milk Sourcing')
quality_testing = Transition(label='Quality Testing')
culture_prep = Transition(label='Culture Prep')
milk_pasteurize = Transition(label='Milk Pasteurize')
curd_cutting = Transition(label='Curd Cutting')
whey_draining = Transition(label='Whey Draining')
molding_cheese = Transition(label='Molding Cheese')
pressing_blocks = Transition(label='Pressing Blocks')
salting_process = Transition(label='Salting Process')
aging_monitoring = Transition(label='Aging Monitoring')
flavor_profiling = Transition(label='Flavor Profiling')
packaging_design = Transition(label='Packaging Design')
compliance_check = Transition(label='Compliance Check')
market_research = Transition(label='Market Research')
direct_shipping = Transition(label='Direct Shipping')
customer_feedback = Transition(label='Customer Feedback')
recipe_adjust = Transition(label='Recipe Adjust')

# Define the silent transitions (empty labels)
skip = SilentTransition()

# Define the loop node for aging monitoring
loop = OperatorPOWL(operator=Operator.LOOP, children=[aging_monitoring, skip])

# Define the exclusive choice for quality testing
xor = OperatorPOWL(operator=Operator.XOR, children=[flavor_profiling, skip])

# Define the root POWL model
root = StrictPartialOrder(nodes=[loop, xor])
root.order.add_edge(loop, xor)

# Print the root POWL model
print(root)