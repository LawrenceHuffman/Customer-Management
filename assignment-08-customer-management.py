# Module 8 Assignment: Data Lookup with Dictionaries & Basic Aggregation
# GlobalTech Solutions Customer Management System

# Welcome message
print("=" * 60)
print("GLOBALTECH SOLUTIONS - CUSTOMER MANAGEMENT SYSTEM")
print("=" * 60)

# TODO 1: Create a dictionary of service categories and hourly rates
services = {
    "Web Development": 150,
    "Data Analysis": 175,
    "Cybersecurity": 220,
    "Cloud Consulting": 200,
    "IT Support": 95
}

# TODO 2: Create customer dictionaries
customer1 = {
    "company_name": "Alpha Innovations",
    "contact_person": "James Carter",
    "email": "james@alphainnovations.com",
    "phone": "813-555-1001"
}

customer2 = {
    "company_name": "BrightPath Logistics",
    "contact_person": "Maria Lopez",
    "email": "maria@brightpathlogistics.com",
    "phone": "813-555-1002"
}

customer3 = {
    "company_name": "Summit Retail Group",
    "contact_person": "David Kim",
    "email": "david@summitretail.com",
    "phone": "813-555-1003"
}

customer4 = {
    "company_name": "Nexa Health Systems",
    "contact_person": "Olivia Brown",
    "email": "olivia@nexahealth.com",
    "phone": "813-555-1004"
}

# TODO 3: Create a master customers dictionary
customers = {
    "C001": customer1,
    "C002": customer2,
    "C003": customer3,
    "C004": customer4
}

# TODO 4: Display all customers
print("\nAll Customers:")
print("-" * 60)
for customer_id, info in customers.items():
    print(f"{customer_id}:")
    for key, value in info.items():
        print(f"  {key}: {value}")
    print()

# TODO 5: Look up specific customers
c002_info = customers["C002"]
c003_contact = customers["C003"]["contact_person"]
c999_info = customers.get("C999", "Customer not found")

print("\n\nCustomer Lookups:")
print("-" * 60)
print("C002 Information:", c002_info)
print("C003 Contact Person:", c003_contact)
print("C999 Lookup:", c999_info)

# TODO 6: Update customer information
customers["C001"]["phone"] = "813-555-1111"
customers["C002"]["industry"] = "Logistics"

print("\n\nUpdating Customer Information:")
print("-" * 60)
print("Updated C001:", customers["C001"])
print("Updated C002:", customers["C002"])

# TODO 7: Create project dictionaries for each customer
project1 = {
    "name": "Corporate Website Redesign",
    "service": "Web Development",
    "hours": 120,
    "budget": 18000
}

project2 = {
    "name": "Sales Dashboard",
    "service": "Data Analysis",
    "hours": 80,
    "budget": 14000
}

project3 = {
    "name": "Security Audit",
    "service": "Cybersecurity",
    "hours": 60,
    "budget": 15000
}

project4 = {
    "name": "Cloud Migration",
    "service": "Cloud Consulting",
    "hours": 100,
    "budget": 22000
}

project5 = {
    "name": "Help Desk Setup",
    "service": "IT Support",
    "hours": 50,
    "budget": 5000
}

project6 = {
    "name": "Inventory Analytics",
    "service": "Data Analysis",
    "hours": 70,
    "budget": 12500
}

projects = {
    "C001": [project1, project2],
    "C002": [project3],
    "C003": [project4, project5],
    "C004": [project6]
}

print("\n\nProject Information:")
print("-" * 60)
for customer_id, project_list in projects.items():
    print(f"{customer_id}:")
    for project in project_list:
        print(f"  {project}")
    print()

# TODO 8: Calculate project costs
print("\n\nProject Cost Calculations:")
print("-" * 60)
for customer_id, project_list in projects.items():
    for project in project_list:
        hourly_rate = services[project["service"]]
        cost = hourly_rate * project["hours"]
        print(
            f"{customer_id} - {project['name']} | "
            f"Service: {project['service']} | "
            f"Hours: {project['hours']} | "
            f"Calculated Cost: ${cost:,.2f}"
        )

# TODO 9: Customer statistics using dictionary methods
print("\n\nCustomer Statistics:")
print("-" * 60)
print("Customer IDs:", list(customers.keys()))
print("Customer Companies:", [customer["company_name"] for customer in customers.values()])
print("Total Customers:", len(customers))

# TODO 10: Service usage analysis
service_counts = {}
for project_list in projects.values():
    for project in project_list:
        service_name = project["service"]
        service_counts[service_name] = service_counts.get(service_name, 0) + 1

print("\n\nService Usage Analysis:")
print("-" * 60)
for service, count in service_counts.items():
    print(f"{service}: {count}")

# TODO 11: Financial aggregations
all_projects = []
for project_list in projects.values():
    all_projects.extend(project_list)

total_hours = sum(project["hours"] for project in all_projects)
total_budget = sum(project["budget"] for project in all_projects)
avg_budget = total_budget / len(all_projects) if all_projects else 0
max_budget = max(project["budget"] for project in all_projects) if all_projects else 0
min_budget = min(project["budget"] for project in all_projects) if all_projects else 0

most_expensive_project = max(all_projects, key=lambda p: p["budget"]) if all_projects else None
least_expensive_project = min(all_projects, key=lambda p: p["budget"]) if all_projects else None

print("\n\nFinancial Summary:")
print("-" * 60)
print(f"Total Hours: {total_hours}")
print(f"Total Budget: ${total_budget:,.2f}")
print(f"Average Project Budget: ${avg_budget:,.2f}")
print(f"Highest Budget Amount: ${max_budget:,.2f}")
print(f"Lowest Budget Amount: ${min_budget:,.2f}")
print(f"Most Expensive Project: {most_expensive_project['name']} (${most_expensive_project['budget']:,.2f})")
print(f"Least Expensive Project: {least_expensive_project['name']} (${least_expensive_project['budget']:,.2f})")

# TODO 12: Customer summary report
print("\n\nCustomer Summary Report:")
print("-" * 60)
for customer_id, customer_info in customers.items():
    customer_projects = projects.get(customer_id, [])
    customer_total_hours = sum(project["hours"] for project in customer_projects)
    customer_total_budget = sum(project["budget"] for project in customer_projects)

    print(f"{customer_id} - {customer_info['company_name']}")
    print(f"  Contact: {customer_info['contact_person']}")
    print(f"  Email: {customer_info['email']}")
    print(f"  Phone: {customer_info['phone']}")
    print(f"  Number of Projects: {len(customer_projects)}")
    print(f"  Total Hours: {customer_total_hours}")
    print(f"  Total Budget: ${customer_total_budget:,.2f}")
    print()

# TODO 13: Create rate adjustments using dictionary comprehension
adjusted_rates = {service: rate * 1.1 for service, rate in services.items()}

print("\n\nAdjusted Service Rates (10% increase):")
print("-" * 60)
for service, rate in adjusted_rates.items():
    print(f"{service}: ${rate:,.2f}")

# TODO 14: Filter customers using dictionary comprehension
active_customers = {customer_id: info for customer_id, info in customers.items() if customer_id in projects and len(projects[customer_id]) > 0}

print("\n\nActive Customers (with projects):")
print("-" * 60)
for customer_id, info in active_customers.items():
    print(f"{customer_id}: {info['company_name']}")

# TODO 15: Create project summaries using dictionary comprehension
customer_budgets = {customer_id: sum(project["budget"] for project in project_list) for customer_id, project_list in projects.items()}

print("\n\nCustomer Budget Totals:")
print("-" * 60)
for customer_id, total in customer_budgets.items():
    print(f"{customer_id}: ${total:,.2f}")

# TODO 16: Service pricing tiers using dictionary comprehension
service_tiers = {
    service: "Premium" if rate >= 200 else "Standard" if rate >= 100 else "Basic"
    for service, rate in services.items()
}

print("\n\nService Pricing Tiers:")
print("-" * 60)
for service, tier in service_tiers.items():
    print(f"{service}: {tier}")

# TODO 17: Customer validation function
def validate_customer(customer_dict):
    required_fields = ["company_name", "contact_person", "email", "phone"]
    for field in required_fields:
        if field not in customer_dict or customer_dict[field] == "":
            return False
    return True

print("\n\nCustomer Validation:")
print("-" * 60)
for customer_id, customer_info in customers.items():
    print(f"{customer_id}: {validate_customer(customer_info)}")

# TODO 18: Project status tracking with loops and conditionals
status_list = ["active", "completed", "pending"]
status_counts = {"active": 0, "completed": 0, "pending": 0}

status_index = 0
for project_list in projects.values():
    for project in project_list:
        project["status"] = status_list[status_index % len(status_list)]
        status_counts[project["status"]] += 1
        status_index += 1

print("\n\nProject Status Summary:")
print("-" * 60)
for status, count in status_counts.items():
    print(f"{status.capitalize()}: {count}")

# TODO 19: Budget analysis function with aggregation
def analyze_customer_budgets(projects_dict):
    budget_analysis = {}

    for customer_id, project_list in projects_dict.items():
        total = 0
        count = 0

        for project in project_list:
            total += project["budget"]
            count += 1

        average = total / count if count > 0 else 0

        budget_analysis[customer_id] = {
            "total": total,
            "average": average,
            "count": count
        }

    return budget_analysis

budget_analysis_results = analyze_customer_budgets(projects)

print("\n\nDetailed Budget Analysis:")
print("-" * 60)
for customer_id, stats in budget_analysis_results.items():
    print(f"{customer_id}: Total=${stats['total']:,.2f}, Average=${stats['average']:,.2f}, Count={stats['count']}")

# TODO 20: Service recommendation system
def recommend_services(customer_id, customers, projects, services):
    if customer_id not in customers:
        return ["Customer not found"]

    customer_projects = projects.get(customer_id, [])
    used_services = []

    for project in customer_projects:
        used_services.append(project["service"])

    average_budget = 0
    if len(customer_projects) > 0:
        total_budget = sum(project["budget"] for project in customer_projects)
        average_budget = total_budget / len(customer_projects)

    recommendations = []
    for service, rate in services.items():
        if service not in used_services:
            estimated_cost = rate * 50  # assumes a moderate 50-hour project
            if average_budget == 0 or estimated_cost <= average_budget * 1.2:
                recommendations.append(service)

    return recommendations

print("\n\nService Recommendations:")
print("-" * 60)
for customer_id in customers.keys():
    recommendations = recommend_services(customer_id, customers, projects, services)
    print(f"{customer_id}: {recommendations}")