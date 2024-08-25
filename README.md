
# eCommerce Project

![eCommerce](https://img.shields.io/badge/eCommerce-Django%20REST%20Framework-blue.svg)

This is a comprehensive eCommerce platform built with Django and Django REST Framework. The platform includes essential features for managing products, orders, users, and more. 

## Table of Contents

- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [API Documentation](#api-documentation)
- [Models Overview](#models-overview)
- [Project Structure](#project-structure)
- [Data Generation](#data-generation)
- [Contributing](#contributing)
- [License](#license)

## Features

- User Authentication (JWT)
- Product Management
- Order Management
- Cart Functionality
- Product Reviews
- Admin Panel for Managing Data
- Swagger API Documentation
- Comprehensive Querysets and Business Logic Layers
- OTP Service for Authentication
- payment(compatible with all PSP in Iran)

## Installation

1. **Clone the repository:**

```bash
git clone https://github.com/sajadfallahdoost/eCommerce.git
cd eCommerce
```

2. **Install dependencies:**

   - Using Poetry (Recommended):

     ```bash
     poetry install
     ```

   - Using pip:

     ```bash
     pip install -r requirements.txt
     ```

3. **Apply migrations:**

```bash
python manage.py migrate
```

4. **Create a superuser:**

```bash
python manage.py createsuperuser
```

5. **Run the development server:**

```bash
python manage.py runserver
```

## Usage

- Access the admin panel at `http://127.0.0.1:8000/admin/`
- Access the API documentation at `http://127.0.0.1:8000/swagger/`

## API Documentation

This project uses Swagger for API documentation. Visit the `/swagger/` endpoint to explore and test the available API endpoints.

## Models Overview

### Warehouse

- **Product**: Represents a product in the store.
- **ProductGallery**: Manages product images.
- **Pack**: Represents a product pack.
- **Tag**: Tags for products.
- **Brand**: Brand information.
- **Category**: Product categories.
- **AttributeValue**: Values for product attributes.

### Customer

- **User**: User authentication and management.
- **PersonalProfile**: Personal profile for users.
- **CorporateProfile**: Corporate profile for companies.
- **Address**: User addresses.

### Basket

- **Cart**: Shopping cart management.
- **CartItem**: Items within a shopping cart.
- **OrderAddresses**: Addresses associated with orders.
- **Orders**: Order management.

## Project Structure

```bash
eCommerce/
├── account/
│   ├── api/
│   │   └── views.py
│   ├── models/
│   │   └── user_profile.py
│   └── serializers
├── basket/
│   ├── api/
│   │   └── views.py
│   ├── models/
│   │   └── cart.py
│   └── serializers
├── services/
│   ├── otp/
│   │   ├── api/
│   │   │   └── views.py
│   │   ├── logic.py
│   │   └── serializers
│   ├── payment/
│   │   ├── api/
│   │   ├── payment_idpay/
│   │   ├── payment_sep/
│   │   ├── payment_zarinpal/
│   │   └── serializers
├── shop/
│   ├── models/
│   │   └── order.py
│   ├── api/
│   │   └── views.py
│   └── serializers
├── warehouse/
│   ├── api/
│   │   └── views.py
│   ├── models/
│   │   └── product.py
│   ├── repository/
│   │   ├── manager/
│   │   │   └── warehouse.py
│   │   └── queryset/
│   │       └── warehouse.py
│   └── serializers
├── eCommerce/
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
└── manage.py

```

## Data Generation

To generate sample data for the database, run the following command:

```bash
python manage.py generate_all_data
```

This command will fill the database with sample data for testing and development purposes.

## Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository.
2. Create a new branch: `git checkout -b feature-branch-name`.
3. Make your changes and commit them: `git commit -m 'Add some feature'`.
4. Push to the branch: `git push origin feature-branch-name`.
5. Create a pull request.

## License

This project is open source and available under the sjd-developer License.
