# SkyTeam Lounges Database
A crowdsourced JSON database of SkyTeam airline lounges.

## How to Contribute
1. **Add a Lounge**: Create a new JSON file in `data/lounges/` (e.g., `LAX-TBIT-SKYTEAM.json`).
2. **Validate**: Ensure your file matches the [schema](schema.json).
3. **Submit**: Open a Pull Request!

### Example Lounge Entry
```json
{
  "id": "LAX-TBIT-SKYTEAM",
  "name": "SkyTeam Lounge",
  "airport": "LAX",
  "terminal": "TBIT",
  "access": [
    { "rule": "BusinessClass" },
    { "rule": "PaidEntry", "fee": 50 }
  ],
  "hours": [
    { "days": "Mon-Fri", "open": "05:00", "close": "23:00" }
  ],
  "amenities": ["Showers", "PremiumFood"]
}
