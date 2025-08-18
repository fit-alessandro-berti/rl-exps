import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the transitions (activities) with their labels
Provenance_Check = Transition(label='Provenance Check')
Material_Scan = Transition(label='Material Scan')
Wear_Analysis = Transition(label='Wear Analysis')
Image_Capture = Transition(label='Image Capture')
Pattern_Match = Transition(label='Pattern Match')
Ownership_Verify = Transition(label='Ownership Verify')
Ethics_Review = Transition(label='Ethics Review')
Carbon_Dating = Transition(label='Carbon Dating')
Restoration_Eval = Transition(label='Restoration Eval')
Report_Draft = Transition(label='Report Draft')
Stakeholder_Review = Transition(label='Stakeholder Review')
Archive_Data = Transition(label='Archive Data')
Exhibit_Approve = Transition(label='Exhibit Approve')
Condition_Monitor = Transition(label='Condition Monitor')
Final_Certification = Transition(label='Final Certification')

# Define the partial order structure
root = StrictPartialOrder(nodes=[
    Provenance_Check, Material_Scan, Wear_Analysis, Image_Capture, Pattern_Match,
    Ownership_Verify, Ethics_Review, Carbon_Dating, Restoration_Eval, Report_Draft,
    Stakeholder_Review, Archive_Data, Exhibit_Approve, Condition_Monitor, Final_Certification
])

# Define the dependencies between the activities
root.order.add_edge(Provenance_Check, Material_Scan)
root.order.add_edge(Material_Scan, Wear_Analysis)
root.order.add_edge(Wear_Analysis, Image_Capture)
root.order.add_edge(Image_Capture, Pattern_Match)
root.order.add_edge(Pattern_Match, Ownership_Verify)
root.order.add_edge(Ownership_Verify, Ethics_Review)
root.order.add_edge(Ethics_Review, Carbon_Dating)
root.order.add_edge(Carbon_Dating, Restoration_Eval)
root.order.add_edge(Restoration_Eval, Report_Draft)
root.order.add_edge(Report_Draft, Stakeholder_Review)
root.order.add_edge(Stakeholder_Review, Archive_Data)
root.order.add_edge(Archive_Data, Exhibit_Approve)
root.order.add_edge(Exhibit_Approve, Condition_Monitor)
root.order.add_edge(Condition_Monitor, Final_Certification)

# Print the final POWL model
print(root)