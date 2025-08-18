from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

site_select = Transition(label='Site Select')
design_layout = Transition(label='Design Layout')
sensor_integrate = Transition(label='Sensor Integrate')
crop_choose = Transition(label='Crop Choose')
soil_prepare = Transition(label='Soil Prepare')
irrigation_setup = Transition(label='Irrigation Setup')
pest_control = Transition(label='Pest Control')
lighting_install = Transition(label='Lighting Install')
staff_train = Transition(label='Staff Train')
compliance_check = Transition(label='Compliance Check')
market_analyze = Transition(label='Market Analyze')
package_design = Transition(label='Package Design')
logistics_plan = Transition(label='Logistics Plan')
data_analyze = Transition(label='Data Analyze')
feedback_loop = Transition(label='Feedback Loop')

site_select_choice = OperatorPOWL(operator=Operator.XOR, children=[site_select, site_select])
design_layout_choice = OperatorPOWL(operator=Operator.XOR, children=[design_layout, design_layout])
sensor_integrate_choice = OperatorPOWL(operator=Operator.XOR, children=[sensor_integrate, sensor_integrate])
crop_choose_choice = OperatorPOWL(operator=Operator.XOR, children=[crop_choose, crop_choose])
soil_prepare_choice = OperatorPOWL(operator=Operator.XOR, children=[soil_prepare, soil_prepare])
irrigation_setup_choice = OperatorPOWL(operator=Operator.XOR, children=[irrigation_setup, irrigation_setup])
pest_control_choice = OperatorPOWL(operator=Operator.XOR, children=[pest_control, pest_control])
lighting_install_choice = OperatorPOWL(operator=Operator.XOR, children=[lighting_install, lighting_install])
staff_train_choice = OperatorPOWL(operator=Operator.XOR, children=[staff_train, staff_train])
compliance_check_choice = OperatorPOWL(operator=Operator.XOR, children=[compliance_check, compliance_check])
market_analyze_choice = OperatorPOWL(operator=Operator.XOR, children=[market_analyze, market_analyze])
package_design_choice = OperatorPOWL(operator=Operator.XOR, children=[package_design, package_design])
logistics_plan_choice = OperatorPOWL(operator=Operator.XOR, children=[logistics_plan, logistics_plan])
data_analyze_choice = OperatorPOWL(operator=Operator.XOR, children=[data_analyze, data_analyze])
feedback_loop_choice = OperatorPOWL(operator=Operator.XOR, children=[feedback_loop, feedback_loop])

root = StrictPartialOrder(nodes=[
    site_select_choice,
    design_layout_choice,
    sensor_integrate_choice,
    crop_choose_choice,
    soil_prepare_choice,
    irrigation_setup_choice,
    pest_control_choice,
    lighting_install_choice,
    staff_train_choice,
    compliance_check_choice,
    market_analyze_choice,
    package_design_choice,
    logistics_plan_choice,
    data_analyze_choice,
    feedback_loop_choice
])
root.order.add_edge(site_select_choice, design_layout_choice)
root.order.add_edge(design_layout_choice, sensor_integrate_choice)
root.order.add_edge(sensor_integrate_choice, crop_choose_choice)
root.order.add_edge(crop_choose_choice, soil_prepare_choice)
root.order.add_edge(soil_prepare_choice, irrigation_setup_choice)
root.order.add_edge(irrigation_setup_choice, pest_control_choice)
root.order.add_edge(pest_control_choice, lighting_install_choice)
root.order.add_edge(lighting_install_choice, staff_train_choice)
root.order.add_edge(staff_train_choice, compliance_check_choice)
root.order.add_edge(compliance_check_choice, market_analyze_choice)
root.order.add_edge(market_analyze_choice, package_design_choice)
root.order.add_edge(package_design_choice, logistics_plan_choice)
root.order.add_edge(logistics_plan_choice, data_analyze_choice)
root.order.add_edge(data_analyze_choice, feedback_loop_choice)