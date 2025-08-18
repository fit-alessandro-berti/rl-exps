import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions for each activity
artifact_intake = Transition(label='Artifact Intake')
visual_scan = Transition(label='Visual Scan')
material_test = Transition(label='Material Test')
radiocarbon_check = Transition(label='Radiocarbon Check')
provenance_search = Transition(label='Provenance Search')
archive_review = Transition(label='Archive Review')
expert_consult = Transition(label='Expert Consult')
microscope_exam = Transition(label='Microscope Exam')
infrared_scan = Transition(label='Infrared Scan')
legal_verify = Transition(label='Legal Verify')
condition_report = Transition(label='Condition Report')
digital_catalog = Transition(label='Digital Catalog')
ownership_audit = Transition(label='Ownership Audit')
restoration_plan = Transition(label='Restoration Plan')
final_approval = Transition(label='Final Approval')
authentication_cert = Transition(label='Authentication Cert')

# Define silent transitions (empty labels)
skip = SilentTransition()

# Define exclusive choice nodes
choice1 = OperatorPOWL(operator=Operator.XOR, children=[artifact_intake, skip])
choice2 = OperatorPOWL(operator=Operator.XOR, children=[visual_scan, skip])
choice3 = OperatorPOWL(operator=Operator.XOR, children=[material_test, skip])
choice4 = OperatorPOWL(operator=Operator.XOR, children=[radiocarbon_check, skip])
choice5 = OperatorPOWL(operator=Operator.XOR, children=[provenance_search, skip])
choice6 = OperatorPOWL(operator=Operator.XOR, children=[archive_review, skip])
choice7 = OperatorPOWL(operator=Operator.XOR, children=[expert_consult, skip])
choice8 = OperatorPOWL(operator=Operator.XOR, children=[microscope_exam, skip])
choice9 = OperatorPOWL(operator=Operator.XOR, children=[infrared_scan, skip])
choice10 = OperatorPOWL(operator=Operator.XOR, children=[legal_verify, skip])
choice11 = OperatorPOWL(operator=Operator.XOR, children=[condition_report, skip])
choice12 = OperatorPOWL(operator=Operator.XOR, children=[digital_catalog, skip])
choice13 = OperatorPOWL(operator=Operator.XOR, children=[ownership_audit, skip])
choice14 = OperatorPOWL(operator=Operator.XOR, children=[restoration_plan, skip])

# Define loop nodes
loop1 = OperatorPOWL(operator=Operator.LOOP, children=[final_approval, skip])
loop2 = OperatorPOWL(operator=Operator.LOOP, children=[authentication_cert, skip])

# Construct the POWL model
root = StrictPartialOrder(
    nodes=[choice1, choice2, choice3, choice4, choice5, choice6, choice7, choice8, choice9, choice10, choice11,
           choice12, choice13, choice14, loop1, loop2],
    order={
        choice1: [choice2, choice3, choice4, choice5, choice6, choice7, choice8, choice9, choice10, choice11,
                  choice12, choice13, choice14, loop1, loop2],
        choice2: [choice3, choice4, choice5, choice6, choice7, choice8, choice9, choice10, choice11,
                  choice12, choice13, choice14, loop1, loop2],
        choice3: [choice4, choice5, choice6, choice7, choice8, choice9, choice10, choice11,
                  choice12, choice13, choice14, loop1, loop2],
        choice4: [choice5, choice6, choice7, choice8, choice9, choice10, choice11,
                  choice12, choice13, choice14, loop1, loop2],
        choice5: [choice6, choice7, choice8, choice9, choice10, choice11,
                  choice12, choice13, choice14, loop1, loop2],
        choice6: [choice7, choice8, choice9, choice10, choice11,
                  choice12, choice13, choice14, loop1, loop2],
        choice7: [choice8, choice9, choice10, choice11,
                  choice12, choice13, choice14, loop1, loop2],
        choice8: [choice9, choice10, choice11,
                  choice12, choice13, choice14, loop1, loop2],
        choice9: [choice10, choice11,
                  choice12, choice13, choice14, loop1, loop2],
        choice10: [choice11,
                  choice12, choice13, choice14, loop1, loop2],
        choice11: [choice12, choice13, choice14, loop1, loop2],
        choice12: [choice13, choice14, loop1, loop2],
        choice13: [choice14, loop1, loop2],
        choice14: [loop1, loop2],
        loop1: [authentication_cert],
        loop2: [final_approval]
    }
)

# Add edges to the order
root.order.add_edge(choice1, choice2)
root.order.add_edge(choice1, choice3)
root.order.add_edge(choice1, choice4)
root.order.add_edge(choice1, choice5)
root.order.add_edge(choice1, choice6)
root.order.add_edge(choice1, choice7)
root.order.add_edge(choice1, choice8)
root.order.add_edge(choice1, choice9)
root.order.add_edge(choice1, choice10)
root.order.add_edge(choice1, choice11)
root.order.add_edge(choice1, choice12)
root.order.add_edge(choice1, choice13)
root.order.add_edge(choice1, choice14)
root.order.add_edge(choice1, loop1)
root.order.add_edge(choice1, loop2)

root.order.add_edge(choice2, choice3)
root.order.add_edge(choice2, choice4)
root.order.add_edge(choice2, choice5)
root.order.add_edge(choice2, choice6)
root.order.add_edge(choice2, choice7)
root.order.add_edge(choice2, choice8)
root.order.add_edge(choice2, choice9)
root.order.add_edge(choice2, choice10)
root.order.add_edge(choice2, choice11)
root.order.add_edge(choice2, choice12)
root.order.add_edge(choice2, choice13)
root.order.add_edge(choice2, choice14)
root.order.add_edge(choice2, loop1)
root.order.add_edge(choice2, loop2)

root.order.add_edge(choice3, choice4)
root.order.add_edge(choice3, choice5)
root.order.add_edge(choice3, choice6)
root.order.add_edge(choice3, choice7)
root.order.add_edge(choice3, choice8)
root.order.add_edge(choice3, choice9)
root.order.add_edge(choice3, choice10)
root.order.add_edge(choice3, choice11)
root.order.add_edge(choice3, choice12)
root.order.add_edge(choice3, choice13)
root.order.add_edge(choice3, choice14)
root.order.add_edge(choice3, loop1)
root.order.add_edge(choice3, loop2)

root.order.add_edge(choice4, choice5)
root.order.add_edge(choice4, choice6)
root.order.add_edge(choice4, choice7)
root.order.add_edge(choice4, choice8)
root.order.add_edge(choice4, choice9)
root.order.add_edge(choice4, choice10)
root.order.add_edge(choice4, choice11)
root.order.add_edge(choice4, choice12)
root.order.add_edge(choice4, choice13)
root.order.add_edge(choice4, choice14)
root.order.add_edge(choice4, loop1)
root.order.add_edge(choice4, loop2)

root.order.add_edge(choice5, choice6)
root.order.add_edge(choice5, choice7)
root.order.add_edge(choice5, choice8)
root.order.add_edge(choice5, choice9)
root.order.add_edge(choice5, choice10)
root.order.add_edge(choice5, choice11)
root.order.add_edge(choice5, choice12)
root.order.add_edge(choice5, choice13)
root.order.add_edge(choice5, choice14)
root.order.add_edge(choice5, loop1)
root.order.add_edge(choice5, loop2)

root.order.add_edge(choice6, choice7)
root.order.add_edge(choice6, choice8)
root.order.add_edge(choice6, choice9)
root.order.add_edge(choice6, choice10)
root.order.add_edge(choice6, choice11)
root.order.add_edge(choice6, choice12)
root.order.add_edge(choice6, choice13)
root.order.add_edge(choice6, choice14)
root.order.add_edge(choice6, loop1)
root.order.add_edge(choice6, loop2)

root.order.add_edge(choice7, choice8)
root.order.add_edge(choice7, choice9)
root.order.add_edge(choice7, choice10)
root.order.add_edge(choice7, choice11)
root.order.add_edge(choice7, choice12)
root.order.add_edge(choice7, choice13)
root.order.add_edge(choice7, choice14)
root.order.add_edge(choice7, loop1)
root.order.add_edge(choice7, loop2)

root.order.add_edge(choice8, choice9)
root.order.add_edge(choice8, choice10)
root.order.add_edge(choice8, choice11)
root.order.add_edge(choice8, choice12)
root.order.add_edge(choice8, choice13)
root.order.add_edge(choice8, choice14)
root.order.add_edge(choice8, loop1)
root.order.add_edge(choice8, loop2)

root.order.add_edge(choice9, choice10)
root.order.add_edge(choice9, choice11)
root.order.add_edge(choice9, choice12)
root.order.add_edge(choice9, choice13)
root.order.add_edge(choice9, choice14)
root.order.add_edge(choice9, loop1)
root.order.add_edge(choice9, loop2)

root.order.add_edge(choice10, choice11)
root.order.add_edge(choice10, choice12)
root.order.add_edge(choice10, choice13)
root.order.add_edge(choice10, choice14)
root.order.add_edge(choice10, loop1)
root.order.add_edge(choice10, loop2)

root.order.add_edge(choice11, choice12)
root.order.add_edge(choice11, choice13)
root.order.add_edge(choice11, choice14)
root.order.add_edge(choice11, loop1)
root.order.add_edge(choice11, loop2)

root.order.add_edge(choice12, choice13)
root.order.add_edge(choice12, choice14)
root.order.add_edge(choice12, loop1)
root.order.add_edge(choice12, loop2)

root.order.add_edge(choice13, choice14)
root.order.add_edge(choice13, loop1)
root.order.add_edge(choice13, loop2)

root.order.add_edge(choice14, loop1)
root.order.add_edge(choice14, loop2)

root.order.add_edge(loop1, authentication_cert)
root.order.add_edge(loop2, final_approval)