from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the activities
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

# Define the partial order
root = StrictPartialOrder(
    nodes=[
        milk_sourcing,
        quality_testing,
        culture_prep,
        milk_pasteurize,
        curd_cutting,
        whey_draining,
        molding_cheese,
        pressing_blocks,
        salting_process,
        aging_monitoring,
        flavor_profiling,
        packaging_design,
        compliance_check,
        market_research,
        direct_shipping,
        customer_feedback,
        recipe_adjust
    ],
    order={
        (milk_sourcing, quality_testing): 1,
        (milk_sourcing, culture_prep): 1,
        (milk_sourcing, milk_pasteurize): 1,
        (quality_testing, curd_cutting): 1,
        (quality_testing, whey_draining): 1,
        (culture_prep, molding_cheese): 1,
        (milk_pasteurize, curd_cutting): 1,
        (milk_pasteurize, whey_draining): 1,
        (curd_cutting, molding_cheese): 1,
        (whey_draining, molding_cheese): 1,
        (molding_cheese, pressing_blocks): 1,
        (molding_cheese, salting_process): 1,
        (pressing_blocks, salting_process): 1,
        (salting_process, aging_monitoring): 1,
        (aging_monitoring, flavor_profiling): 1,
        (flavor_profiling, packaging_design): 1,
        (packaging_design, compliance_check): 1,
        (compliance_check, market_research): 1,
        (market_research, direct_shipping): 1,
        (direct_shipping, customer_feedback): 1,
        (customer_feedback, recipe_adjust): 1,
        (recipe_adjust, milk_sourcing): 1
    }
)