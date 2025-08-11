import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

MilkSelection = Transition(label='Milk Selection')
QualityTesting = Transition(label='Quality Testing')
MilkPasteurize = Transition(label='Milk Pasteurize')
CheeseCrafting = Transition(label='Cheese Crafting')
ControlledAging = Transition(label='Controlled Aging')
SensoryReview = Transition(label='Sensory Review')
CustomPackaging = Transition(label='Custom Packaging')
LabelPrinting = Transition(label='Label Printing')
ExportLicensing = Transition(label='Export Licensing')
DocumentationPrep = Transition(label='Documentation Prep')
CustomsClearance = Transition(label='Customs Clearance')
ColdShipping = Transition(label='Cold Shipping')
DeliveryTracking = Transition(label='Delivery Tracking')
FeedbackReview = Transition(label='Feedback Review')
MarketAnalysis = Transition(label='Market Analysis')

skip = SilentTransition()

# Milk Processing Steps
MilkSelectionXQualityTesting = OperatorPOWL(operator=Operator.XOR, children=[MilkSelection, QualityTesting])
MilkSelectionXQualityTestingXPasteurize = OperatorPOWL(operator=Operator.XOR, children=[MilkSelectionXQualityTesting, MilkPasteurize])
MilkSelectionXQualityTestingXPasteurizeXCrafting = OperatorPOWL(operator=Operator.XOR, children=[MilkSelectionXQualityTestingXPasteurize, CheeseCrafting])

# Aging and Packaging
CraftingXAgeing = OperatorPOWL(operator=Operator.XOR, children=[CheeseCrafting, ControlledAging])
CraftingXAgeingXReview = OperatorPOWL(operator=Operator.XOR, children=[CraftingXAgeing, SensoryReview])
CraftingXAgeingXReviewXCustomPackaging = OperatorPOWL(operator=Operator.XOR, children=[CraftingXAgeingXReview, CustomPackaging])

# Packaging and Labeling
CustomPackagingXLabelPrinting = OperatorPOWL(operator=Operator.XOR, children=[CustomPackaging, LabelPrinting])

# Export Licensing and Documentation
LabelPrintingXExportLicensing = OperatorPOWL(operator=Operator.XOR, children=[LabelPrinting, ExportLicensing])
LabelPrintingXExportLicensingXDocumentation = OperatorPOWL(operator=Operator.XOR, children=[LabelPrintingXExportLicensing, DocumentationPrep])

# Customs Clearance and Shipping
DocumentationPrepXCustomsClearance = OperatorPOWL(operator=Operator.XOR, children=[DocumentationPrep, CustomsClearance])
DocumentationPrepXCustomsClearanceXShipping = OperatorPOWL(operator=Operator.XOR, children=[DocumentationPrepXCustomsClearance, ColdShipping])

# Shipping and Tracking
ShippingXDeliveryTracking = OperatorPOWL(operator=Operator.XOR, children=[ColdShipping, DeliveryTracking])

# Feedback Review and Market Analysis
DeliveryTrackingXFeedbackReview = OperatorPOWL(operator=Operator.XOR, children=[DeliveryTracking, FeedbackReview])
DeliveryTrackingXFeedbackReviewXMarketAnalysis = OperatorPOWL(operator=Operator.XOR, children=[DeliveryTrackingXFeedbackReview, MarketAnalysis])

root = StrictPartialOrder(nodes=[MilkSelectionXQualityTestingXPasteurizeXCrafting, CraftingXAgeingXReviewXCustomPackaging, CustomPackagingXLabelPrinting, LabelPrintingXExportLicensingXDocumentation, DocumentationPrepXCustomsClearanceXShipping, ShippingXDeliveryTracking, DeliveryTrackingXFeedbackReviewXMarketAnalysis])
root.order.add_edge(MilkSelectionXQualityTestingXPasteurizeXCrafting, CraftingXAgeingXReviewXCustomPackaging)
root.order.add_edge(CraftingXAgeingXReviewXCustomPackaging, CustomPackagingXLabelPrinting)
root.order.add_edge(CustomPackagingXLabelPrinting, LabelPrintingXExportLicensingXDocumentation)
root.order.add_edge(LabelPrintingXExportLicensingXDocumentation, DocumentationPrepXCustomsClearanceXShipping)
root.order.add_edge(DocumentationPrepXCustomsClearanceXShipping, ShippingXDeliveryTracking)
root.order.add_edge(ShippingXDeliveryTracking, DeliveryTrackingXFeedbackReviewXMarketAnalysis)