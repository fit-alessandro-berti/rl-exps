import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define activities
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

# Define relationships
cycle = OperatorPOWL(operator=Operator.CYCLE, children=[milk_sourcing, quality_testing, culture_prep, milk_pasteurize, curd_cutting, whey_draining, molding_cheese, pressing_blocks, salting_process, aging_monitoring, flavor_profiling, packaging_design, compliance_check])
feedback = OperatorPOWL(operator=Operator.XOR, children=[market_research, direct_shipping])
loop = OperatorPOWL(operator=Operator.LOOP, children=[feedback])
root = StrictPartialOrder(nodes=[cycle, loop])
root.order.add_edge(cycle, loop)

print(root)