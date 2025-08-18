import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions (activities) with their labels
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

# Define partial order nodes
milk_processing = StrictPartialOrder(nodes=[milk_sourcing, quality_testing, culture_prep, milk_pasteurize, curd_cutting, whey_draining, molding_cheese, pressing_blocks, salting_process])
aging = StrictPartialOrder(nodes=[aging_monitoring, flavor_profiling, packaging_design])
compliance = StrictPartialOrder(nodes=[compliance_check])
market = StrictPartialOrder(nodes=[market_research, direct_shipping])
feedback = StrictPartialOrder(nodes=[customer_feedback])
recipe = StrictPartialOrder(nodes=[recipe_adjust])

# Define partial order edges
milk_processing.order.add_edge(milk_sourcing, quality_testing)
milk_processing.order.add_edge(quality_testing, culture_prep)
milk_processing.order.add_edge(culture_prep, milk_pasteurize)
milk_processing.order.add_edge(milk_pasteurize, curd_cutting)
milk_processing.order.add_edge(curd_cutting, whey_draining)
milk_processing.order.add_edge(whey_draining, molding_cheese)
milk_processing.order.add_edge(molding_cheese, pressing_blocks)
milk_processing.order.add_edge(pressing_blocks, salting_process)

aging.order.add_edge(aging_monitoring, flavor_profiling)
aging.order.add_edge(flavor_profiling, packaging_design)

compliance.order.add_edge(compliance_check, skip)

market.order.add_edge(market_research, direct_shipping)

feedback.order.add_edge(customer_feedback, skip)

recipe.order.add_edge(recipe_adjust, skip)

# Define the root partial order
root = StrictPartialOrder(nodes=[milk_processing, aging, compliance, market, feedback, recipe])
root.order.add_edge(milk_processing, aging)
root.order.add_edge(milk_processing, compliance)
root.order.add_edge(milk_processing, market)
root.order.add_edge(milk_processing, feedback)
root.order.add_edge(milk_processing, recipe)