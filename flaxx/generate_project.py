import os

app_name = "app"
files = ["app.py", "models.py", "schemas.py", "enums.py", "database.py"]
folders = ["android", "ios"]


def generate_project_structure(name: str = app_name):
    os.makedirs(f"{name}")

    for file in files:
        with open(f"{name}/{file}", 'w'):
            pass

    for folder in folders:
        os.makedirs(f"{name}/{folder}")


if __name__ == "__main__":
    generate_project_structure()
