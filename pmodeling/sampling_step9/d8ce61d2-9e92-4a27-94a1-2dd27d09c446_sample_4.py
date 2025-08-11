import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

Initial_Audit = Transition(label='Initial Audit')
Artist_Review = Transition(label='Artist Review')
Material_Check = Transition(label='Material Check')
Condition_Scan = Transition(label='Condition Scan')
Ownership_Verify = Transition(label='Ownership Verify')
Appraisal_Update = Transition(label='Appraisal Update')
Restoration_Plan = Transition(label='Restoration Plan')
Restoration_Track = Transition(label='Restoration Track')
Logistics_Book = Transition(label='Logistics Book')
Shipping_Monitor = Transition(label='Shipping Monitor')
Customs_Clear = Transition(label='Customs Clear')
Legal_Compliance = Transition(label='Legal Compliance')
Ledger_Update = Transition(label='Ledger Update')
Exhibition_Setup = Transition(label='Exhibition Setup')
Public_Showcase = Transition(label='Public Showcase')
Archival_Prep = Transition(label='Archival Prep')
Final_Report = Transition(label='Final Report')

skip = SilentTransition()

# Define the POWL model
loop_ownership = OperatorPOWL(operator=Operator.LOOP, children=[Ownership_Verify, Appraisal_Update])
loop_condition = OperatorPOWL(operator=Operator.LOOP, children=[Condition_Scan, Restoration_Plan])
loop_artifact = OperatorPOWL(operator=Operator.LOOP, children=[Material_Check, Artist_Review])
loop_legal = OperatorPOWL(operator=Operator.LOOP, children=[Legal_Compliance, Customs_Clear])
loop_logistics = OperatorPOWL(operator=Operator.LOOP, children=[Logistics_Book, Shipping_Monitor])

xor_exhibition = OperatorPOWL(operator=Operator.XOR, children=[Public_Showcase, Exhibition_Setup])
xor_archival = OperatorPOWL(operator=Operator.XOR, children=[Archival_Prep, Final_Report])

root = StrictPartialOrder(nodes=[loop_ownership, loop_condition, loop_artifact, loop_legal, loop_logistics, xor_exhibition, xor_archival])
root.order.add_edge(loop_ownership, loop_condition)
root.order.add_edge(loop_condition, loop_artifact)
root.order.add_edge(loop_artifact, loop_legal)
root.order.add_edge(loop_legal, loop_logistics)
root.order.add_edge(loop_logistics, xor_exhibition)
root.order.add_edge(xor_exhibition, xor_archival)