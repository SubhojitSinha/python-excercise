import re
import json

def parse_route_line(line):
    # Patterns for each element
    patterns = {
        'route_url': r"crm_routes\.route\('([^']+)'",
        # 'method_name': r"defaults={'method_name':\s*'([^']+)'}",
        'defaults': r"defaults=({*.*?})",
        'methods': r"methods=\[([^\]]+)\]",
        'strict_slashes': r"strict_slashes=(\w+)",
        'destination': r"\(RequestHandler\.(\w+)\)"

    }
    
    result = {}
    
    for key, pattern in patterns.items():
        match = re.search(pattern, line)
        if match:
            value = match.group(1)
            if key == 'methods':
                value = value.strip("'")
            result[key] = value
    
    return result if result else None

def process_file(file_path):
    result = {}
    with open(file_path, 'r') as file:
        for line in file:
            parsed = parse_route_line(line.strip())
            if parsed:
                destination = parsed['destination']
                if destination not in result:
                    result[destination] = [dict(parsed)]
                else:
                    result[destination].append(parsed)
    return result

# Use the functions
file_path = 'crm_routes.py'  # Replace with your actual file path
parsed_routes = process_file(file_path)

# Save to JSON file
with open('routes.json', 'w') as json_file:
    json.dump(parsed_routes, json_file, indent=4)

print("Parsing complete. Results saved to 'routes.json'")