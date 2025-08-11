import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define activities
Site_Survey = Transition(label='Site Survey')
Soil_Testing = Transition(label='Soil Testing')
Stakeholder_Meet = Transition(label='Stakeholder Meet')
Resource_Plan = Transition(label='Resource Plan')
Crop_Selection = Transition(label='Crop Selection')
Volunteer_Sign_up = Transition(label='Volunteer Sign-up')
Tech_Setup = Transition(label='Tech Setup')
Irrigation_Check = Transition(label='Irrigation Check')
Data_Collection = Transition(label='Data Collection')
Growth_Monitoring = Transition(label='Growth Monitoring')
Conflict_Mediate = Transition(label='Conflict Mediate')
Workshop_Prep = Transition(label='Workshop Prep')
Market_Forecast = Transition(label='Market Forecast')
Yield_Analysis = Transition(label='Yield Analysis')
Sustainability_Audit = Transition(label='Sustainability Audit')
Community_Feedback = Transition(label='Community Feedback')
Equipment_Maintain = Transition(label='Equipment Maintain')
Waste_Manage = Transition(label='Waste Manage')

# Define silent activities
skip = SilentTransition()

# Define loop nodes
loop1 = OperatorPOWL(operator=Operator.LOOP, children=[Site_Survey, Soil_Testing])
loop2 = OperatorPOWL(operator=Operator.LOOP, children=[Resource_Plan, Crop_Selection])
loop3 = OperatorPOWL(operator=Operator.LOOP, children=[Volunteer_Sign_up, Tech_Setup])
loop4 = OperatorPOWL(operator=Operator.LOOP, children=[Irrigation_Check, Data_Collection])
loop5 = OperatorPOWL(operator=Operator.LOOP, children=[Growth_Monitoring, Conflict_Mediate])
loop6 = OperatorPOWL(operator=Operator.LOOP, children=[Workshop_Prep, Market_Forecast])
loop7 = OperatorPOWL(operator=Operator.LOOP, children=[Yield_Analysis, Sustainability_Audit])
loop8 = OperatorPOWL(operator=Operator.LOOP, children=[Community_Feedback, Equipment_Maintain])
loop9 = OperatorPOWL(operator=Operator.LOOP, children=[Waste_Manage])

# Define XOR nodes
xor1 = OperatorPOWL(operator=Operator.XOR, children=[loop1, skip])
xor2 = OperatorPOWL(operator=Operator.XOR, children=[loop2, skip])
xor3 = OperatorPOWL(operator=Operator.XOR, children=[loop3, skip])
xor4 = OperatorPOWL(operator=Operator.XOR, children=[loop4, skip])
xor5 = OperatorPOWL(operator=Operator.XOR, children=[loop5, skip])
xor6 = OperatorPOWL(operator=Operator.XOR, children=[loop6, skip])
xor7 = OperatorPOWL(operator=Operator.XOR, children=[loop7, skip])
xor8 = OperatorPOWL(operator=Operator.XOR, children=[loop8, skip])
xor9 = OperatorPOWL(operator=Operator.XOR, children=[loop9, skip])

# Define root node
root = StrictPartialOrder(nodes=[xor1, xor2, xor3, xor4, xor5, xor6, xor7, xor8, xor9])
root.order.add_edge(xor1, xor2)
root.order.add_edge(xor2, xor3)
root.order.add_edge(xor3, xor4)
root.order.add_edge(xor4, xor5)
root.order.add_edge(xor5, xor6)
root.order.add_edge(xor6, xor7)
root.order.add_edge(xor7, xor8)
root.order.add_edge(xor8, xor9)