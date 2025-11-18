# orbital_utils/telemetry_parser.py
# Author: Jax Coder
# Date: 2038-03-01
# Description: Basic parser for raw satellite telemetry data.

import json

class TelemetryParser:
    def __init__(self, data_format="json"):
        self.data_format = data_format

    def parse_data(self, raw_data):
        if self.data_format == "json":
            try:
                return json.loads(raw_data)
            except json.JSONDecodeError:
                print("Error: Invalid JSON format.")
                return None
        elif self.data_format == "csv":
            # Very simplified CSV parser
            return [line.split(',') for line in raw_data.strip().split('\n')]
        else:
            print("Unsupported data format.")
            return None

    def get_altitude(self, parsed_telemetry):
        if self.data_format == "json" and parsed_telemetry:
            return parsed_telemetry.get("altitude_km")
        return None

if __name__ == "__main__":
    sample_json = '{"satellite_id": "SAT-001", "timestamp": "2038-03-01T10:30:00Z", "altitude_km": 550.2, "velocity_mps": 7600}'
    sample_csv = "SAT-002,2038-03-01T10:31:00Z,551.0,7605"

    parser = TelemetryParser("json")
    parsed_json = parser.parse_data(sample_json)
    if parsed_json:
        print(f"Satellite ID: {parsed_json.get('satellite_id')}, Altitude: {parser.get_altitude(parsed_json)} km")

    parser_csv = TelemetryParser("csv")
    parsed_csv = parser_csv.parse_data(sample_csv)
    if parsed_csv:
        print(f"CSV Data: {parsed_csv}")
