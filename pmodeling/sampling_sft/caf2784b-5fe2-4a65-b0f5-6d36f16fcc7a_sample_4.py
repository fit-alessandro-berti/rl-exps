import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define atomic activities
site_audit      = Transition(label='Site Audit')
impact_study    = Transition(label='Impact Study')
design_modules  = Transition(label='Design Modules')
sensor_setup    = Transition(label='Sensor Setup')
hydro_install   = Transition(label='Hydroponics Install')
nutrient_test   = Transition(label='Nutrient Test')
lighting_config = Transition(label='Lighting Config')
staff_training  = Transition(label='Staff Training')
data_collection = Transition(label='Data Collection')
yield_analysis  = Transition(label='Yield Analysis')
pest_control    = Transition(label='Pest Control')
harvest_plan    = Transition(label='Harvest Plan')
pack_prep       = Transition(label='Packaging Prep')
market_delivery = Transition(label='Market Delivery')
feedback_loop   = Transition(label='Feedback Loop')

# Build the loop body: Pest Control -> Harvest Plan -> Packaging Prep -> Market Delivery
body = StrictPartialOrder(nodes=[pest_control, harvest_plan, pack_prep, market_delivery])
body.order.add_edge(pest_control, harvest_plan)
body.order.add_edge(harvest_plan, pack_prep)
body.order.add_edge(pack_prep, market_delivery)

# Define the loop: after each delivery, do Feedback Loop then either exit or repeat the body
loop = OperatorPOWL(operator=Operator.LOOP, children=[body, feedback_loop])

# Assemble the overall partial order
root = StrictPartialOrder(nodes=[
    site_audit, impact_study, design_modules, sensor_setup,
    hydro_install, nutrient_test, lighting_config, staff_training,
    data_collection, yield_analysis, loop
])

# Define the control-flow dependencies
root.order.add_edge(site_audit, impact_study)
root.order.add_edge(impact_study, design_modules)
root.order.add_edge(design_modules, sensor_setup)
root.order.add_edge(sensor_setup, hydro_install)
root.order.add_edge(hydro_install, nutrient_test)
root.order.add_edge(nutrient_test, lighting_config)
root.order.add_edge(lighting_config, staff_training)
root.order.add_edge(staff_training, data_collection)
root.order.add_edge(data_collection, yield_analysis)
root.order.add_edge(yield_analysis, loop)