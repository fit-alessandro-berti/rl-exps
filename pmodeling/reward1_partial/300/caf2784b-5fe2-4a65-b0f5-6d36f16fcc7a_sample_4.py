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

site_audit_loop = OperatorPOWL(operator=Operator.LOOP, children=[site_audit])
impact_study_loop = OperatorPOWL(operator=Operator.LOOP, children=[impact_study])
design_modules_loop = OperatorPOWL(operator=Operator.LOOP, children=[design_modules])
sensor_setup_loop = OperatorPOWL(operator=Operator.LOOP, children=[sensor_setup])
hydroponics_install_loop = OperatorPOWL(operator=Operator.LOOP, children=[hydroponics_install])
nutrient_test_loop = OperatorPOWL(operator=Operator.LOOP, children=[nutrient_test])
lighting_config_loop = OperatorPOWL(operator=Operator.LOOP, children=[lighting_config])
staff_training_loop = OperatorPOWL(operator=Operator.LOOP, children=[staff_training])
data_collection_loop = OperatorPOWL(operator=Operator.LOOP, children=[data_collection])
yield_analysis_loop = OperatorPOWL(operator=Operator.LOOP, children=[yield_analysis])
pest_control_loop = OperatorPOWL(operator=Operator.LOOP, children=[pest_control])
harvest_plan_loop = OperatorPOWL(operator=Operator.LOOP, children=[harvest_plan])
packaging_prep_loop = OperatorPOWL(operator=Operator.LOOP, children=[packaging_prep])
market_delivery_loop = OperatorPOWL(operator=Operator.LOOP, children=[market_delivery])
feedback_loop_loop = OperatorPOWL(operator=Operator.LOOP, children=[feedback_loop])

root = StrictPartialOrder(nodes=[
    site_audit_loop, impact_study_loop, design_modules_loop, sensor_setup_loop, 
    hydroponics_install_loop, nutrient_test_loop, lighting_config_loop, staff_training_loop, 
    data_collection_loop, yield_analysis_loop, pest_control_loop, harvest_plan_loop, 
    packaging_prep_loop, market_delivery_loop, feedback_loop_loop
])

root.order.add_edge(site_audit_loop, impact_study_loop)
root.order.add_edge(impact_study_loop, design_modules_loop)
root.order.add_edge(design_modules_loop, sensor_setup_loop)
root.order.add_edge(sensor_setup_loop, hydroponics_install_loop)
root.order.add_edge(hydroponics_install_loop, nutrient_test_loop)
root.order.add_edge(nutrient_test_loop, lighting_config_loop)
root.order.add_edge(lighting_config_loop, staff_training_loop)
root.order.add_edge(staff_training_loop, data_collection_loop)
root.order.add_edge(data_collection_loop, yield_analysis_loop)
root.order.add_edge(yield_analysis_loop, pest_control_loop)
root.order.add_edge(pest_control_loop, harvest_plan_loop)
root.order.add_edge(harvest_plan_loop, packaging_prep_loop)
root.order.add_edge(packaging_prep_loop, market_delivery_loop)
root.order.add_edge(market_delivery_loop, feedback_loop_loop)

print(root)