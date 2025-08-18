from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition

# Define the activities
MilkSourcing = Transition(label='Milk Sourcing')
QualityTesting = Transition(label='Quality Testing')
StarterPrep = Transition(label='Starter Prep')
CurdCutting = Transition(label='Curd Cutting')
WheyDraining = Transition(label='Whey Draining')
MoldingPress = Transition(label='Molding Press')
FermentationControl = Transition(label='Fermentation Control')
AgingSetup = Transition(label='Aging Setup')
HumidityCheck = Transition(label='Humidity Check')
PackagingDesign = Transition(label='Packaging Design')
LabelApproval = Transition(label='Label Approval')
InventoryAudit = Transition(label='Inventory Audit')
OrderScheduling = Transition(label='Order Scheduling')
MarketDelivery = Transition(label='Market Delivery')
FeedbackReview = Transition(label='Feedback Review')
ComplianceCheck = Transition(label='Compliance Check')
MarketingSync = Transition(label='Marketing Sync')

# Define the loop for fermentation control
fermentationControlLoop = OperatorPOWL(operator=Operator.LOOP, children=[FermentationControl])

# Define the exclusive choice for aging setup and humidity check
agingSetupOrHumidityCheck = OperatorPOWL(operator=Operator.XOR, children=[AgingSetup, HumidityCheck])

# Define the exclusive choice for packaging design approval and label approval
packagingDesignOrLabelApproval = OperatorPOWL(operator=Operator.XOR, children=[PackagingDesign, LabelApproval])

# Define the exclusive choice for inventory audit and order scheduling
inventoryAuditOrOrderScheduling = OperatorPOWL(operator=Operator.XOR, children=[InventoryAudit, OrderScheduling])

# Define the exclusive choice for market delivery and feedback review
marketDeliveryOrFeedbackReview = OperatorPOWL(operator=Operator.XOR, children=[MarketDelivery, FeedbackReview])

# Define the exclusive choice for compliance check and marketing sync
complianceCheckOrMarketingSync = OperatorPOWL(operator=Operator.XOR, children=[ComplianceCheck, MarketingSync])

# Define the root POWL model
root = StrictPartialOrder(nodes=[
    MilkSourcing,
    QualityTesting,
    StarterPrep,
    CurdCutting,
    WheyDraining,
    MoldingPress,
    fermentationControlLoop,
    agingSetupOrHumidityCheck,
    packagingDesignOrLabelApproval,
    inventoryAuditOrOrderScheduling,
    marketDeliveryOrFeedbackReview,
    complianceCheckOrMarketingSync
])
root.order.add_edge(fermentationControlLoop, agingSetupOrHumidityCheck)
root.order.add_edge(agingSetupOrHumidityCheck, packagingDesignOrLabelApproval)
root.order.add_edge(packagingDesignOrLabelApproval, inventoryAuditOrOrderScheduling)
root.order.add_edge(inventoryAuditOrOrderScheduling, marketDeliveryOrFeedbackReview)
root.order.add_edge(marketDeliveryOrFeedbackReview, complianceCheckOrMarketingSync)

print(root)