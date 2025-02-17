def mock_hubspot_api_call(field_name, field_type):
    print(f"Mock call to HubSpot: Adding field {field_name} of type {field_type}")
    return True

def mock_upso_api_call(cadence_name, timing, template):
    print(f"Mock call to Upso: Updating cadence {cadence_name} to timing {timing} with template: {template}")
    return True
