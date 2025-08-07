import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
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
data_collect    = Transition(label='Data Collection')
yield_analysis  = Transition(label='Yield Analysis')
pest_control    = Transition(label='Pest Control')
harvest_plan    = Transition(label='Harvest Plan')
packaging_prep  = Transition(label='Packaging Prep')
market_delivery = Transition(label='Market Delivery')
feedback_loop   = Transition(label='Feedback Loop')

# Loop for iterative yield analysis and pest control
loop_body = StrictPartialOrder(nodes=[pest_control, yield_analysis])
loop_body.order.add_edge(pest_control, yield_analysis)

# Loop: do Data Collection, then either exit or do loop_body and repeat
loop = OperatorPOWL(operator=Operator.LOOP, children=[data_collect, loop_body])

# Build the overall partial order
root = StrictPartialOrder(nodes=[
    site_audit, impact_study, design_modules, sensor_setup,
    hydro_install, nutrient_test, lighting_config, staff_training,
    loop, feedback_loop, packaging_prep, market_delivery
])

# Define the control-flow dependencies
root.order.add_edge(site_audit, impact_study)
root.order.add_edge(impact_study, design_modules)
root.order.add_edge(design_modules, sensor_setup)
root.order.add_edge(sensor_setup, hydro_install)
root.order.add_edge(hydro_install, nutrient_test)
root.order.add_edge(nutrient_test, lighting_config)
root.order.add_edge(lighting_config, staff_training)
root.order.add_edge(staff_training, loop)
root.order.add_edge(loop, feedback_loop)
root.order.add_edge(feedback_loop, packaging_prep)
root.order.add_edge(packaging_prep, market_delivery)

# Final feedback loop back to the start
root.order.add_edge(market_delivery, site_audit)