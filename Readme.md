# This repository consists of code for a Vendor Management System, written in Django.

## Setting-up the Project

### Cloning the Repository
```sh
git clone https://github.com/kirmola/vms-fatmug.git
cd vms-fatmug
```

### Installing Poetry
First, install Poetry using its official installer. Follow the instructions at [https://python-poetry.org/docs/#installing-with-the-official-installer](https://python-poetry.org/docs/#installing-with-the-official-installer).

### Installing Dependencies
```sh
poetry install
```

### Running the Project Locally
```sh
poetry run python manage.py runserver
```

After running these commands, your Django project should be running locally at [http://localhost:8000/](http://localhost:8000/).

### Admin Credentials
username: root
password: root

### Run model tests
```sh
python manage.py test 
```

## API Documentation

1. Following are the API endpoints to interact with vendor model:

- API Endpoints:
  - `GET` `/api/vendors/`: List all vendors.
  - `GET` `/api/vendors/{vendor_id}/`: Retrieve a specific vendor's details.
  - `PUT` `/api/vendors/{vendor_id}/`: Update a vendor's details.
  - `POST` `/api/vendors/`: Create a new vendor.
  - `DELETE` `/api/vendors/{vendor_id}/`: Delete a vendor.

2. Following are the routes to interact with Purchase Orders:

- API Endpoints:
  - `GET` `/api/purchase_orders/`: List all purchase orders with an option to filter by vendor.
  - `GET` `/api/purchase_orders/{purchase_order_id}/`: Retrieve details of a specific purchase order.
  - `POST` `/api/purchase_orders/`: Create a purchase order.
  - `PUT` `/api/purchase_orders/{purchase_order_id}/`: Update a purchase order.
  - `DELETE` `/api/purchase_orders/{purchase_order_id}/`: Delete a purchase order.

3. Following are the routes to evaluate a vendor's performance and acknowledging a purchase order, which further triggers recalculation of average response time:

- API Endpoints:
  - `GET` `/api/vendors/{vendor_id}/performance/`: Retrieve a vendor's performance metrics.
  - `POST` `/api/purchase_orders/{po_id}/acknowledge/`: 