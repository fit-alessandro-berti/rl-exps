import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define activities
activities = {
    'Provenance Check': Transition(label='Provenance Check'),
    'Image Capture': Transition(label='Image Capture'),
    'Material Scan': Transition(label='Material Scan'),
    'Expert Review': Transition(label='Expert Review'),
    'Historical Cross': Transition(label='Historical Cross'),
    'Legal Verify': Transition(label='Legal Verify'),
    'Registry Search': Transition(label='Registry Search'),
    'Customs Clear': Transition(label='Customs Clear'),
    'Condition Assess': Transition(label='Condition Assess'),
    'Data Log': Transition(label='Data Log'),
    'Chain Custody': Transition(label='Chain Custody'),
    'Report Draft': Transition(label='Report Draft'),
    'Certification': Transition(label='Certification'),
    'Secure Archive': Transition(label='Secure Archive'),
    'Auction Prep': Transition(label='Auction Prep')
}

# Define the POWL model
root = StrictPartialOrder()

# Provenance Check -> Image Capture -> Material Scan -> Expert Review -> Historical Cross
provenance_check = activities['Provenance Check']
image_capture = activities['Image Capture']
material_scan = activities['Material Scan']
expert_review = activities['Expert Review']
historical_cross = activities['Historical Cross']
root.children.append(provenance_check)
provenance_check.children.append(image_capture)
image_capture.children.append(material_scan)
material_scan.children.append(expert_review)
expert_review.children.append(historical_cross)

# Legal Verify -> Registry Search -> Customs Clear
legal_verify = activities['Legal Verify']
registry_search = activities['Registry Search']
customs_clear = activities['Customs Clear']
root.children.append(legal_verify)
legal_verify.children.append(registry_search)
registry_search.children.append(customs_clear)

# Condition Assess -> Data Log -> Chain Custody -> Report Draft
condition_assess = activities['Condition Assess']
data_log = activities['Data Log']
chain_custody = activities['Chain Custody']
report_draft = activities['Report Draft']
root.children.append(condition_assess)
condition_assess.children.append(data_log)
data_log.children.append(chain_custody)
chain_custody.children.append(report_draft)

# Certification -> Secure Archive
certification = activities['Certification']
secure_archive = activities['Secure Archive']
root.children.append(certification)
certification.children.append(secure_archive)

# Auction Prep
auction_prep = activities['Auction Prep']
root.children.append(auction_prep)

# Print the POWL model
print(root)