import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

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

site_audit_choice = OperatorPOWL(operator=Operator.XOR, children=[site_audit, impact_study])
design_modules_choice = OperatorPOWL(operator=Operator.XOR, children=[design_modules, sensor_setup])
hydroponics_install_choice = OperatorPOWL(operator=Operator.XOR, children=[hydroponics_install, nutrient_test])
lighting_config_choice = OperatorPOWL(operator=Operator.XOR, children=[lighting_config, staff_training])
data_collection_choice = OperatorPOWL(operator=Operator.XOR, children=[data_collection, yield_analysis])
pest_control_choice = OperatorPOWL(operator=Operator.XOR, children=[pest_control, harvest_plan])
packaging_prep_choice = OperatorPOWL(operator=Operator.XOR, children=[packaging_prep, market_delivery])
feedback_loop_choice = OperatorPOWL(operator=Operator.XOR, children=[feedback_loop, feedback_loop])

root = StrictPartialOrder(nodes=[
    site_audit_choice,
    design_modules_choice,
    hydroponics_install_choice,
    lighting_config_choice,
    data_collection_choice,
    pest_control_choice,
    packaging_prep_choice,
    feedback_loop_choice
])

root.order.add_edge(site_audit_choice, design_modules_choice)
root.order.add_edge(design_modules_choice, hydroponics_install_choice)
root.order.add_edge(hydroponics_install_choice, lighting_config_choice)
root.order.add_edge(lighting_config_choice, data_collection_choice)
root.order.add_edge(data_collection_choice, pest_control_choice)
root.order.add_edge(pest_control_choice, packaging_prep_choice)
root.order.add_edge(packaging_prep_choice, feedback_loop_choice)
root.order.add_edge(feedback_loop_choice, feedback_loop_choice)