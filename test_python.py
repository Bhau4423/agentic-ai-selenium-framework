from models.finding import Finding
from models.severity import Severity

f = Finding(
    finding_id="MAP-001",
    severity=Severity.HIGH,
    source="SemanticReviewer",
    title="Invalid Mapping",
    description="Incorrect page mapping detected",
    recommendation="Review mapping"
)

print(f.to_dict())