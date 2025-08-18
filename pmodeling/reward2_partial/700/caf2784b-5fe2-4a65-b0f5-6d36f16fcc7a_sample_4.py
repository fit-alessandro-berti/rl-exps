import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the transitions (activities) in the process
site_audit = Transition(label='Site Audit')
impact_study = Transition(label='Impact Study')
design_modules = Transition(label='Design Modules')
sensor_setup = Transition(label='Sensor Setup')
hydroponics_install = Transition(label='Hydroponics Install')
nutrient_test = Transition(label='Nutrient Test')
lighting_config = Transition(label='Lighting Config')
staff_training = Transition(label='Staff Training')
data_collection = Transition(label='Data Collection')
yield_analysis = Transition(label='Yield Analysis')
pest_control = Transition(label='Pest Control')
harvest_plan = Transition(label='Harvest Plan')
packaging_prep = Transition(label='Packaging Prep')
market_delivery = Transition(label='Market Delivery')
feedback_loop = Transition(label='Feedback Loop')

# Define the partial order structure
root = StrictPartialOrder(nodes=[site_audit, impact_study, design_modules, sensor_setup, hydroponics_install, nutrient_test, lighting_config, staff_training, data_collection, yield_analysis, pest_control, harvest_plan, packaging_prep, market_delivery, feedback_loop])

# Define the order dependencies
root.order.add_edge(site_audit, impact_study)
root.order.add_edge(impact_study, design_modules)
root.order.add_edge(design_modules, sensor_setup)
root.order.add_edge(sensor_setup, hydroponics_install)
root.order.add_edge(hydroponics_install, nutrient_test)
root.order.add_edge(nutrient_test, lighting_config)
root.order.add_edge(lighting_config, staff_training)
root.order.add_edge(staff_training, data_collection)
root.order.add_edge(data_collection, yield_analysis)
root.order.add_edge(yield_analysis, pest_control)
root.order.add_edge(pest_control, harvest_plan)
root.order.add_edge(harvest_plan, packaging_prep)
root.order.add_edge(packaging_prep, market_delivery)
root.order.add_edge(market_delivery, feedback_loop)

# Print the root of the POWL model
print(root)