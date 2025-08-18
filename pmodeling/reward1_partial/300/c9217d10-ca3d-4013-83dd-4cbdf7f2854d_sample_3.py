import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

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

xor1 = OperatorPOWL(operator=Operator.XOR, children=[compliance_check, marketing_sync])
xor2 = OperatorPOWL(operator=Operator.XOR, children=[yield_analyze, supply_chain])
xor3 = OperatorPOWL(operator=Operator.XOR, children=[customer_engage, site_survey])

loop1 = OperatorPOWL(operator=Operator.LOOP, children=[climate_study, design_layout])
loop2 = OperatorPOWL(operator=Operator.LOOP, children=[system_install, crop_select])
loop3 = OperatorPOWL(operator=Operator.LOOP, children=[nutrient_plan, sensor_setup])
loop4 = OperatorPOWL(operator=Operator.LOOP, children=[automation_test, staff_train])

root = StrictPartialOrder(nodes=[loop1, loop2, loop3, loop4, xor1, xor2, xor3])
root.order.add_edge(loop1, xor1)
root.order.add_edge(loop2, xor2)
root.order.add_edge(loop3, xor3)
root.order.add_edge(loop4, xor1)
root.order.add_edge(xor1, xor2)
root.order.add_edge(xor2, xor3)