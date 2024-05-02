# Fatmug-Assignment


---

# Vendor Management System with Performance Metrics

This is a Vendor Management System developed using Django and Django REST Framework. It allows users to manage vendor profiles, track purchase orders, and calculate vendor performance metrics.

## Features

- **Vendor Profile Management**
  - Create, retrieve, update, and delete vendor profiles.
- **Purchase Order Tracking**
  - Create, retrieve, update, and delete purchase orders.
- **Vendor Performance Evaluation**
  - Calculate various performance metrics including on-time delivery rate, quality rating average, response time, and fulfillment rate.
- **Update Acknowledgment Endpoint**
  - Endpoint to acknowledge purchase orders, updating acknowledgment date and triggering the recalculation of average response time.

## Installation

1. Clone the repository:

    ```bash
    git clone <repository_url>
    ```

2. Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```

3. Apply migrations:

    ```bash
    python manage.py migrate
    ```

4. Run the development server:

    ```bash
    python manage.py runserver
    ```

## Usage

### API Endpoints

- **Vendor Management**
  - `GET /api/vendors/`: List all vendors.
  - `POST /api/vendors/`: Create a new vendor.
  - `GET /api/vendors/{vendor_id}/`: Retrieve a specific vendor.
  - `PUT /api/vendors/{vendor_id}/`: Update a specific vendor.
  - `DELETE /api/vendors/{vendor_id}/`: Delete a specific vendor.

- **Purchase Order Management**
  - `GET /api/purchase_orders/`: List all purchase orders.
  - `POST /api/purchase_orders/`: Create a new purchase order.
  - `GET /api/purchase_orders/{po_id}/`: Retrieve a specific purchase order.
  - `PUT /api/purchase_orders/{po_id}/`: Update a specific purchase order.
  - `DELETE /api/purchase_orders/{po_id}/`: Delete a specific purchase order.
  - `POST /api/purchase_orders/{po_id}/acknowledge`: Acknowledge a purchase order.

- **Vendor Performance Metrics**
  - `GET /api/vendors/{vendor_id}/performance/`: Retrieve performance metrics for a specific vendor.

### Sample Data

#### Create a Vendor

```bash
curl -X POST http://localhost:8000/api/vendors/ -H "Content-Type: application/json" -d '{
    "name": "Vendor A",
    "contact_details": "vendor_a@example.com",
    "address": "123 Main Street, Cityville",
    "vendor_code": "VENDOR-A"
}'
```

#### Create a Purchase Order

```bash
curl -X POST http://localhost:8000/api/purchase_orders/ -H "Content-Type: application/json" -d '{
    "po_number": "PO-001",
    "vendor": 1,  # vendor_id
    "delivery_date": "2024-05-10T12:00:00Z",
    "items": [{"name": "Item 1", "quantity": 10}],
    "quantity": 10
}'
```

#### Acknowledge a Purchase Order

```bash
curl -X POST http://localhost:8000/api/purchase_orders/{po_id}/acknowledge -H "Content-Type: application/json"
```

Replace `{po_id}` with the actual ID of the purchase order.

## Testing

- To test the API endpoints, use tools like cURL, Postman, or send HTTP requests programmatically.
- Test different scenarios such as creating vendors and purchase orders, acknowledging purchase orders, and retrieving performance metrics.
- Verify data integrity and correct calculation of performance metrics.

## Contributors

- [Anjan Prasad](https://github.com/anjanprasad112)

