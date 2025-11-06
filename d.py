
sales_team = {
    "S001": {
        "name": "Ahmed",
        "region": "Cairo",
        "monthly_sales": 12000,
        "target": 10000
    },
    "S002": {
        "name": "Sara",
        "region": "Alexandria",
        "monthly_sales": 8500,
        "target": 9000
    },
    "S003": {
        "name": "Omar",
        "region": "Giza",
        "monthly_sales": 10000,
        "target": 10000
    }
}


for rep_id, info in sales_team.items():
    name = info["name"]
    region = info["region"]
    sales = info["monthly_sales"]
    target = info["target"]

    print(f"\nSales Representative: {name}")
    print(f"Region: {region}")
    print(f"Monthly Sales: {sales}")
    print(f"Target: {target}")

    if sales >= target:
        print("They exceeded the target!")
        bonus = sales * 0.10
        print(f" Bonus awarded: {bonus} EGP")
    else:
        print(" They did not meet the target.")
