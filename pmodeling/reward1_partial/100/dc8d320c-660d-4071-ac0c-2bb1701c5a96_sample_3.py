import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the transitions (activities)
Artifact_Intake = Transition(label='Artifact Intake')
Provenance_Check = Transition(label='Provenance Check')
Material_Testing = Transition(label='Material Testing')
Historical_Review = Transition(label='Historical Review')
Expert_Interview = Transition(label='Expert Interview')
Condition_Audit = Transition(label='Condition Audit')
Digital_Catalog = Transition(label='Digital Catalog')
Forgery_Detection = Transition(label='Forgery Detection')
Legal_Compliance = Transition(label='Legal Compliance')
Restoration_Plan = Transition(label='Restoration Plan')
Valuation_Report = Transition(label='Valuation Report')
Market_Analysis = Transition(label='Market Analysis')
Final_Approval = Transition(label='Final Approval')
Sale_Preparation = Transition(label='Sale Preparation')
Client_Notification = Transition(label='Client Notification')

# Define the control flow
xor1 = OperatorPOWL(operator=Operator.XOR, children=[Final_Approval, Client_Notification])
xor2 = OperatorPOWL(operator=Operator.XOR, children=[Artifact_Intake, Provenance_Check, Material_Testing, Historical_Review, Expert_Interview, Condition_Audit, Digital_Catalog, Forgeries_Detection, Legal_Compliance, Restoration_Plan, Valuation_Report, Market_Analysis])
loop1 = OperatorPOWL(operator=Operator.LOOP, children=[xor2])
xor3 = OperatorPOWL(operator=Operator.XOR, children=[loop1, xor1])

# Create the root node
root = StrictPartialOrder(nodes=[xor3])

# Add dependencies
root.order.add_edge(xor3, xor1)
root.order.add_edge(xor2, xor3)

# Print the root node
print(root)