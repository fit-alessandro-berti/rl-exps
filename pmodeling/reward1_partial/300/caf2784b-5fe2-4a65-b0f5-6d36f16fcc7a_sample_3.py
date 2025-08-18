import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the transitions for each activity
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

# Define the exclusive choice between two activities
xor = OperatorPOWL(operator=Operator.XOR, children=[impact_study, site_audit])

# Define the loop node for the modular system design
loop = OperatorPOWL(operator=Operator.LOOP, children=[design_modules, sensor_setup])

# Define the partial order with the transitions and their dependencies
root = StrictPartialOrder(nodes=[loop, hydroponics_install, nutrient_test, lighting_config, staff_training, data_collection, yield_analysis, pest_control, harvest_plan, packaging_prep, market_delivery, feedback_loop])
root.order.add_edge(loop, hydroponics_install)
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