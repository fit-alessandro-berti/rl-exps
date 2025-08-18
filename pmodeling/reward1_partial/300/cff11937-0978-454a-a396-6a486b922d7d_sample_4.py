from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

milk_sourcing = Transition(label='Milk Sourcing')
quality_testing = Transition(label='Quality Testing')
starter_culture = Transition(label='Starter Culture')
milk_fermentation = Transition(label='Milk Fermentation')
curd_cutting = Transition(label='Curd Cutting')
whey_draining = Transition(label='Whey Draining')
pressing_cheese = Transition(label='Pressing Cheese')
cave_aging = Transition(label='Cave Aging')
sample_tasting = Transition(label='Sample Tasting')
flavor_profiling = Transition(label='Flavor Profiling')
packaging_design = Transition(label='Packaging Design')
cold_storage = Transition(label='Cold Storage')
logistics_planning = Transition(label='Logistics Planning')
pop_up_sales = Transition(label='Pop-up Sales')
customer_feedback = Transition(label='Customer Feedback')
recipe_adjusting = Transition(label='Recipe Adjusting')

skip = SilentTransition()

# Milk Sourcing -> Quality Testing -> Starter Culture -> Milk Fermentation -> Curd Cutting -> Whey Draining -> Pressing Cheese -> Cave Aging
milk_sourcing_to_quality_testing = OperatorPOWL(operator=Operator.PARALLEL, children=[milk_sourcing, quality_testing])
quality_testing_to_starter_culture = OperatorPOWL(operator=Operator.PARALLEL, children=[quality_testing, starter_culture])
starter_culture_to_milk_fermentation = OperatorPOWL(operator=Operator.PARALLEL, children=[starter_culture, milk_fermentation])
milk_fermentation_to_curd_cutting = OperatorPOWL(operator=Operator.PARALLEL, children=[milk_fermentation, curd_cutting])
curd_cutting_to_whey_draining = OperatorPOWL(operator=Operator.PARALLEL, children=[curd_cutting, whey_draining])
whey_draining_to_pressing_cheese = OperatorPOWL(operator=Operator.PARALLEL, children=[whey_draining, pressing_cheese])
pressing_cheese_to_cave_aging = OperatorPOWL(operator=Operator.PARALLEL, children=[pressing_cheese, cave_aging])

# Sample Tasting -> Flavor Profiling -> Packaging Design -> Cold Storage -> Logistics Planning
sample_tasting_to_flavor_profiling = OperatorPOWL(operator=Operator.PARALLEL, children=[sample_tasting, flavor_profiling])
flavor_profiling_to_packaging_design = OperatorPOWL(operator=Operator.PARALLEL, children=[flavor_profiling, packaging_design])
packaging_design_to_cold_storage = OperatorPOWL(operator=Operator.PARALLEL, children=[packaging_design, cold_storage])
cold_storage_to_logistics_planning = OperatorPOWL(operator=Operator.PARALLEL, children=[cold_storage, logistics_planning])

# Pop-up Sales -> Customer Feedback -> Recipe Adjusting
pop_up_sales_to_customer_feedback = OperatorPOWL(operator=Operator.PARALLEL, children=[pop_up_sales, customer_feedback])
customer_feedback_to_recipe_adjusting = OperatorPOWL(operator=Operator.PARALLEL, children=[customer_feedback, recipe_adjusting])

root = StrictPartialOrder(nodes=[
    milk_sourcing_to_quality_testing, 
    quality_testing_to_starter_culture, 
    starter_culture_to_milk_fermentation, 
    milk_fermentation_to_curd_cutting, 
    curd_cutting_to_whey_draining, 
    whey_draining_to_pressing_cheese, 
    pressing_cheese_to_cave_aging, 
    sample_tasting_to_flavor_profiling, 
    flavor_profiling_to_packaging_design, 
    packaging_design_to_cold_storage, 
    cold_storage_to_logistics_planning, 
    pop_up_sales_to_customer_feedback, 
    customer_feedback_to_recipe_adjusting
])
root.order.add_edge(milk_sourcing_to_quality_testing, quality_testing_to_starter_culture)
root.order.add_edge(quality_testing_to_starter_culture, starter_culture_to_milk_fermentation)
root.order.add_edge(starter_culture_to_milk_fermentation, milk_fermentation_to_curd_cutting)
root.order.add_edge(milk_fermentation_to_curd_cutting, curd_cutting_to_whey_draining)
root.order.add_edge(curd_cutting_to_whey_draining, whey_draining_to_pressing_cheese)
root.order.add_edge(whey_draining_to_pressing_cheese, pressing_cheese_to_cave_aging)
root.order.add_edge(sample_tasting_to_flavor_profiling, flavor_profiling_to_packaging_design)
root.order.add_edge(flavor_profiling_to_packaging_design, packaging_design_to_cold_storage)
root.order.add_edge(packaging_design_to_cold_storage, cold_storage_to_logistics_planning)
root.order.add_edge(pop_up_sales_to_customer_feedback, customer_feedback_to_recipe_adjusting)