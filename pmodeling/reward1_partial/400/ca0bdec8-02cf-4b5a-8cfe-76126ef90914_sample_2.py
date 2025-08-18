import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions for each activity
milk_sourcing = Transition(label='Milk Sourcing')
quality_testing = Transition(label='Quality Testing')
culture_prep = Transition(label='Culture Prep')
milk_pasturize = Transition(label='Milk Pasteurize')
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

# Define loop nodes
culture_loop = OperatorPOWL(operator=Operator.LOOP, children=[culture_prep, quality_testing])
aging_loop = OperatorPOWL(operator=Operator.LOOP, children=[aging_monitoring, flavor_profiling, packaging_design, compliance_check, market_research])
shipping_loop = OperatorPOWL(operator=Operator.LOOP, children=[direct_shipping, customer_feedback, recipe_adjust])

# Define partial order
root = StrictPartialOrder(nodes=[milk_sourcing, milk_pasturize, curd_cutting, whey_draining, molding_cheese, pressing_blocks, salting_process, culture_loop, aging_loop, shipping_loop])
root.order.add_edge(milk_sourcing, milk_pasturize)
root.order.add_edge(milk_pasturize, curd_cutting)
root.order.add_edge(curd_cutting, whey_draining)
root.order.add_edge(whey_draining, molding_cheese)
root.order.add_edge(molding_cheese, pressing_blocks)
root.order.add_edge(pressing_blocks, salting_process)
root.order.add_edge(salting_process, culture_loop)
root.order.add_edge(culture_loop, aging_loop)
root.order.add_edge(aging_loop, shipping_loop)

print(root)