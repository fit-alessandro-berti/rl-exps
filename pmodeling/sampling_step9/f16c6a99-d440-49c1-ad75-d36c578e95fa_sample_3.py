import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

Site_Survey = Transition(label='Site Survey')
Design_Layout = Transition(label='Design Layout')
Sensor_Deploy = Transition(label='Sensor Deploy')
Crop_Select = Transition(label='Crop Select')
System_Install = Transition(label='System Install')
Energy_Setup = Transition(label='Energy Setup')
Water_Cycle = Transition(label='Water Cycle')
Pest_Control = Transition(label='Pest Control')
Regulatory_Check = Transition(label='Regulatory Check')
Staff_Training = Transition(label='Staff Training')
Data_Configure = Transition(label='Data Configure')
Supply_Plan = Transition(label='Supply Plan')
Harvest_Schedule = Transition(label='Harvest Schedule')
Quality_Audit = Transition(label='Quality Audit')
Market_Launch = Transition(label='Market Launch')
Feedback_Loop = Transition(label='Feedback Loop')

skip = SilentTransition()

site_survey_loop = OperatorPOWL(operator=Operator.LOOP, children=[Site_Survey, Design_Layout])
design_layout_loop = OperatorPOWL(operator=Operator.LOOP, children=[Sensor_Deploy, Crop_Select, System_Install])
sensor_deploy_loop = OperatorPOWL(operator=Operator.LOOP, children=[Energy_Setup, Water_Cycle, Pest_Control])
energy_setup_loop = OperatorPOWL(operator=Operator.LOOP, children=[Regulatory_Check, Staff_Training, Data_Configure])
regulatory_check_loop = OperatorPOWL(operator=Operator.LOOP, children=[Supply_Plan, Harvest_Schedule, Quality_Audit])
supply_plan_loop = OperatorPOWL(operator=Operator.LOOP, children=[Market_Launch, Feedback_Loop])

root = StrictPartialOrder(nodes=[site_survey_loop, design_layout_loop, sensor_deploy_loop, energy_setup_loop, regulatory_check_loop, supply_plan_loop])
root.order.add_edge(site_survey_loop, design_layout_loop)
root.order.add_edge(design_layout_loop, sensor_deploy_loop)
root.order.add_edge(sensor_deploy_loop, energy_setup_loop)
root.order.add_edge(energy_setup_loop, regulatory_check_loop)
root.order.add_edge(regulatory_check_loop, supply_plan_loop)