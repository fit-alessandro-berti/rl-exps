import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions for each activity
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

# Define silent transitions
skip = SilentTransition()

# Define the process
loop1 = OperatorPOWL(operator=Operator.LOOP, children=[quality_testing, milk_pasteurize])
loop2 = OperatorPOWL(operator=Operator.LOOP, children=[molding_cheese, pressing_blocks])
loop3 = OperatorPOWL(operator=Operator.LOOP, children=[salting_process, aging_monitoring])
loop4 = OperatorPOWL(operator=Operator.LOOP, children=[flavor_profiling, packaging_design])
loop5 = OperatorPOWL(operator=Operator.LOOP, children=[compliance_check, market_research])
loop6 = OperatorPOWL(operator=Operator.LOOP, children=[direct_shipping, customer_feedback])
loop7 = OperatorPOWL(operator=Operator.LOOP, children=[recipe_adjust, milk_sourcing])

# Define the root node
root = StrictPartialOrder(nodes=[milk_sourcing, culture_prep, loop1, loop2, loop3, loop4, loop5, loop6, loop7])
root.order.add_edge(milk_sourcing, culture_prep)
root.order.add_edge(culture_prep, loop1)
root.order.add_edge(loop1, quality_testing)
root.order.add_edge(quality_testing, milk_pasteurize)
root.order.add_edge(milk_pasteurize, loop2)
root.order.add_edge(loop2, molding_cheese)
root.order.add_edge(molding_cheese, pressing_blocks)
root.order.add_edge(pressing_blocks, loop3)
root.order.add_edge(loop3, salting_process)
root.order.add_edge(salting_process, aging_monitoring)
root.order.add_edge(aging_monitoring, loop4)
root.order.add_edge(loop4, flavor_profiling)
root.order.add_edge(flavor_profiling, packaging_design)
root.order.add_edge(packaging_design, loop5)
root.order.add_edge(loop5, compliance_check)
root.order.add_edge(compliance_check, market_research)
root.order.add_edge(market_research, loop6)
root.order.add_edge(loop6, direct_shipping)
root.order.add_edge(direct_shipping, customer_feedback)
root.order.add_edge(customer_feedback, loop7)
root.order.add_edge(loop7, recipe_adjust)
root.order.add_edge(recipe_adjust, milk_sourcing)