import hashlib
import json
from datetime import datetime

print("--- PortNetX Blockchain eDocs System ---")

# 1. Create a digital document (e.g., a Bill of Lading for a shipment)
digital_document = {
    "Vessel_ID": "VESSEL_042",
    "Cargo_Type": "Electronics",
    "Weight_Tons": 12500,
    "Receiver": "TechCorp Logistics",
    "Timestamp": str(datetime.now())
}

# 2. Convert the dictionary into a standardized text string
document_string = json.dumps(digital_document, sort_keys=True)

# 3. Create the Digital Fingerprint (Hash) using SHA-256 (the same math Bitcoin uses!)
# We encode the string to bytes, hash it, and get the readable hexadecimal version
digital_fingerprint = hashlib.sha256(document_string.encode()).hexdigest()

print("\nOriginal Document:")
print(json.dumps(digital_document, indent=4))
print(f"\nLocked Digital Fingerprint (Hash):\n{digital_fingerprint}")

# 4. Demonstrate Tampering
print("\n--- Simulating a Hacker Tampering with the Document ---")
# A hacker tries to change the weight of the cargo
digital_document["Weight_Tons"] = 9000 
tampered_string = json.dumps(digital_document, sort_keys=True)
tampered_fingerprint = hashlib.sha256(tampered_string.encode()).hexdigest()

print(f"Tampered Fingerprint:\n{tampered_fingerprint}")

if digital_fingerprint == tampered_fingerprint:
    print("\nResult: Document is valid.")
else:
    print("\nResult: ALERT! The document has been altered. Hashes do not match!")