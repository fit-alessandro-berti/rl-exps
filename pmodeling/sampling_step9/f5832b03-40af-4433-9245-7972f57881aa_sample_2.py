import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the activities
Site_Survey = Transition(label='Site Survey')
Design_Layout = Transition(label='Design Layout')
Legal_Review = Transition(label='Legal Review')
Tech_Sourcing = Transition(label='Tech Sourcing')
Structural_Build = Transition(label='Structural Build')
Climate_Setup = Transition(label='Climate Setup')
Irrigation_Install = Transition(label='Irrigation Install')
Sensor_Deploy = Transition(label='Sensor Deploy')
Crop_Select = Transition(label='Crop Select')
Nutrient_Prep = Transition(label='Nutrient Prep')
Waste_System = Transition(label='Waste System')
Automation_Config = Transition(label='Automation Config')
Trial_Growth = Transition(label='Trial Growth')
Data_Analysis = Transition(label='Data Analysis')
Quality_Audit = Transition(label='Quality Audit')
Stakeholder_Meet = Transition(label='Stakeholder Meet')
Compliance_Check = Transition(label='Compliance Check')

# Define the silent activities
skip = SilentTransition()

# Define the exclusive choice (XOR) for Tech Sourcing and Legal Review
tech_or_legal = OperatorPOWL(operator=Operator.XOR, children=[Tech_Sourcing, Legal_Review])

# Define the loop for Sensor Deploy and Irrigation Install
sensor_loop = OperatorPOWL(operator=Operator.LOOP, children=[Sensor_Deploy, Irrigation_Install])

# Define the loop for Automation Config and Trial Growth
automation_loop = OperatorPOWL(operator=Operator.LOOP, children=[Automation_Config, Trial_Growth])

# Define the loop for Data Analysis and Quality Audit
data_loop = OperatorPOWL(operator=Operator.LOOP, children=[Data_Analysis, Quality_Audit])

# Define the exclusive choice (XOR) for Stakeholder Meet and Compliance Check
stakeholder_or_compliance = OperatorPOWL(operator=Operator.XOR, children=[Stakeholder_Meet, Compliance_Check])

# Define the partial order
root = StrictPartialOrder(nodes=[Site_Survey, Design_Layout, tech_or_legal, Structural_Build, Climate_Setup, sensor_loop, Crop_Select, Nutrient_Prep, Waste_System, automation_loop, Trial_Growth, data_loop, stakeholder_or_compliance])
root.order.add_edge(Site_Survey, Design_Layout)
root.order.add_edge(Design_Layout, tech_or_legal)
root.order.add_edge(tech_or_legal, Structural_Build)
root.order.add_edge(Structural_Build, Climate_Setup)
root.order.add_edge(Climate_Setup, sensor_loop)
root.order.add_edge(sensor_loop, Crop_Select)
root.order.add_edge(Crop_Select, Nutrient_Prep)
root.order.add_edge(Nutrient_Prep, Waste_System)
root.order.add_edge(Waste_System, automation_loop)
root.order.add_edge(automation_loop, Trial_Growth)
root.order.add_edge(Trial_Growth, data_loop)
root.order.add_edge(data_loop, stakeholder_or_compliance)