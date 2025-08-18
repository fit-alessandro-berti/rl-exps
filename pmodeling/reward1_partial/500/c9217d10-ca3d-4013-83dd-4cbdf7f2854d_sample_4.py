import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the activities
site_survey = Transition(label='Site Survey')
climate_study = Transition(label='Climate Study')
design_layout = Transition(label='Design Layout')
system_install = Transition(label='System Install')
crop_select = Transition(label='Crop Select')
nutrient_plan = Transition(label='Nutrient Plan')
sensor_setup = Transition(label='Sensor Setup')
automation_test = Transition(label='Automation Test')
staff_train = Transition(label='Staff Train')
compliance_check = Transition(label='Compliance Check')
marketing_sync = Transition(label='Marketing Sync')
data_monitor = Transition(label='Data Monitor')
yield_analyze = Transition(label='Yield Analyze')
supply_chain = Transition(label='Supply Chain')
customer_engage = Transition(label='Customer Engage')

# Define the process
site_survey_node = OperatorPOWL(operator=Operator.SILENT, children=[site_survey])
climate_study_node = OperatorPOWL(operator=Operator.SILENT, children=[climate_study])
design_layout_node = OperatorPOWL(operator=Operator.SILENT, children=[design_layout])
system_install_node = OperatorPOWL(operator=Operator.SILENT, children=[system_install])
crop_select_node = OperatorPOWL(operator=Operator.SILENT, children=[crop_select])
nutrient_plan_node = OperatorPOWL(operator=Operator.SILENT, children=[nutrient_plan])
sensor_setup_node = OperatorPOWL(operator=Operator.SILENT, children=[sensor_setup])
automation_test_node = OperatorPOWL(operator=Operator.SILENT, children=[automation_test])
staff_train_node = OperatorPOWL(operator=Operator.SILENT, children=[staff_train])
compliance_check_node = OperatorPOWL(operator=Operator.SILENT, children=[compliance_check])
marketing_sync_node = OperatorPOWL(operator=Operator.SILENT, children=[marketing_sync])
data_monitor_node = OperatorPOWL(operator=Operator.SILENT, children=[data_monitor])
yield_analyze_node = OperatorPOWL(operator=Operator.SILENT, children=[yield_analyze])
supply_chain_node = OperatorPOWL(operator=Operator.SILENT, children=[supply_chain])
customer_engage_node = OperatorPOWL(operator=Operator.SILENT, children=[customer_engage])

# Define the partial order
root = StrictPartialOrder(nodes=[
    site_survey_node,
    climate_study_node,
    design_layout_node,
    system_install_node,
    crop_select_node,
    nutrient_plan_node,
    sensor_setup_node,
    automation_test_node,
    staff_train_node,
    compliance_check_node,
    marketing_sync_node,
    data_monitor_node,
    yield_analyze_node,
    supply_chain_node,
    customer_engage_node
])

# Define the dependencies
root.order.add_edge(site_survey_node, climate_study_node)
root.order.add_edge(climate_study_node, design_layout_node)
root.order.add_edge(design_layout_node, system_install_node)
root.order.add_edge(system_install_node, crop_select_node)
root.order.add_edge(crop_select_node, nutrient_plan_node)
root.order.add_edge(nutrient_plan_node, sensor_setup_node)
root.order.add_edge(sensor_setup_node, automation_test_node)
root.order.add_edge(automation_test_node, staff_train_node)
root.order.add_edge(staff_train_node, compliance_check_node)
root.order.add_edge(compliance_check_node, marketing_sync_node)
root.order.add_edge(marketing_sync_node, data_monitor_node)
root.order.add_edge(data_monitor_node, yield_analyze_node)
root.order.add_edge(yield_analyze_node, supply_chain_node)
root.order.add_edge(supply_chain_node, customer_engage_node)

print(root)