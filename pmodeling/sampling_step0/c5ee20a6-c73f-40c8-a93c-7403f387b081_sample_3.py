import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator
from enum import Enum

class Label(Enum):
    INITIAL_ASSESS = 'Initial Assess'
    CONDITION_SCAN = 'Condition Scan'
    MATERIAL_TEST = 'Material Test'
    HISTORICAL_CHECK = 'Historical Check'
    PROVENANCE_VERIFY = 'Provenance Verify'
    PARTS_SOURCING = 'Parts Sourcing'
    GENTLE_CLEAN = 'Gentle Clean'
    STABILIZE_ITEM = 'Stabilize Item'
    STRUCTURAL_REPAIR = 'Structural Repair'
    SURFACE_FINISH = 'Surface Finish'
    EXPERT_CONSULT = 'Expert Consult'
    ARCHIVAL_REVIEW = 'Archival Review'
    ETHICS_AUDIT = 'Ethics Audit'
    QUALITY_INSPECT = 'Quality Inspect'
    PHOTO_DOCUMENT = 'Photo Document'
    PACKAGING_PREP = 'Packaging Prep'
    REPORT_GENERATE = 'Report Generate'
    CERTIFY_PROVENANCE = 'Certify Provenance'

initial_assess = Transition(label=Label.INITIAL_ASSESS)
condition_scan = Transition(label=Label.CONDITION_SCAN)
material_test = Transition(label=Label.MATERIAL_TEST)
historical_check = Transition(label=Label.HISTORICAL_CHECK)
provenance_verify = Transition(label=Label.PROVENANCE_VERIFY)
parts_sourcing = Transition(label=Label.PARTS_SOURCING)
gentle_clean = Transition(label=Label.GENTLE_CLEAN)
stabilize_item = Transition(label=Label.STABILIZE_ITEM)
structural_repair = Transition(label=Label.STRUCTURAL_REPAIR)
surface_finish = Transition(label=Label.SURFACE_FINISH)
expert_consult = Transition(label=Label.EXPERT_CONSULT)
archival_review = Transition(label=Label.ARCHIVAL_REVIEW)
ethics_audit = Transition(label=Label.ETHICS_AUDIT)
quality_inspect = Transition(label=Label.QUALITY_INSPECT)
photo_document = Transition(label=Label.PHOTO_DOCUMENT)
packaging_prep = Transition(label=Label.PACKAGING_PREP)
report_generate = Transition(label=Label.REPORT_GENERATE)
certify_provenance = Transition(label=Label.CERTIFY_PROVENANCE)

skip = SilentTransition()

# Define the POWL model
xor = OperatorPOWL(operator=Operator.XOR, children=[provenance_verify, skip])
xor2 = OperatorPOWL(operator=Operator.XOR, children=[quality_inspect, skip])
xor3 = OperatorPOWL(operator=Operator.XOR, children=[archival_review, skip])
xor4 = OperatorPOWL(operator=Operator.XOR, children=[expert_consult, skip])
xor5 = OperatorPOWL(operator=Operator.XOR, children=[ethics_audit, skip])
xor6 = OperatorPOWL(operator=Operator.XOR, children=[report_generate, skip])
xor7 = OperatorPOWL(operator=Operator.XOR, children=[certify_provenance, skip])

loop = OperatorPOWL(operator=Operator.LOOP, children=[initial_assess, condition_scan, material_test, historical_check, xor])
loop2 = OperatorPOWL(operator=Operator.LOOP, children=[parts_sourcing, gentle_clean, stabilize_item, structural_repair, surface_finish, xor2])
loop3 = OperatorPOWL(operator=Operator.LOOP, children=[xor3, xor4, xor5, xor6, xor7])

root = StrictPartialOrder(nodes=[loop, loop2, loop3])
root.order.add_edge(loop, loop2)
root.order.add_edge(loop, loop3)
root.order.add_edge(loop2, loop3)