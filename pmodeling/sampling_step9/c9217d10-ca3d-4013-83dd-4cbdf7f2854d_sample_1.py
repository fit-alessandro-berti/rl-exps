import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define activities
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

# Define silent transitions
skip = SilentTransition()

# Define sub-processes
site_process = OperatorPOWL(operator=Operator.XOR, children=[site_survey, climate_study])
layout_process = OperatorPOWL(operator=Operator.XOR, children=[design_layout, system_install])
crop_process = OperatorPOWL(operator=Operator.XOR, children=[crop_select, nutrient_plan])
sensor_process = OperatorPOWL(operator=Operator.XOR, children=[sensor_setup, automation_test])
staff_process = OperatorPOWL(operator=Operator.XOR, children=[staff_train, compliance_check])
marketing_process = OperatorPOWL(operator=Operator.XOR, children=[marketing_sync, data_monitor])
yield_process = OperatorPOWL(operator=Operator.XOR, children=[yield_analyze, supply_chain])
customer_process = OperatorPOWL(operator=Operator.XOR, children=[customer_engage, skip])

# Define main process
root = StrictPartialOrder(nodes=[site_process, layout_process, crop_process, sensor_process, staff_process, marketing_process, yield_process, customer_process])
root.order.add_edge(site_process, layout_process)
root.order.add_edge(layout_process, crop_process)
root.order.add_edge(crop_process, sensor_process)
root.order.add_edge(sensor_process, staff_process)
root.order.add_edge(staff_process, marketing_process)
root.order.add_edge(marketing_process, yield_process)
root.order.add_edge(yield_process, customer_process)