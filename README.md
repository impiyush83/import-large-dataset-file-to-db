# Fulfil.io coding challenge

***Create a sku import system for ACME INC for large csv files.*** 

**-----------------------------------------------------------------------------------------**

**1. LOGIC**

**-----------------------------------------------------------------------------------------**

1. Used **RabbitMq + Celery for async background jobs**.

2. Created paginated API for searching.  

**-----------------------------------------------------------------------------------------**

**2. SETUP**


**-----------------------------------------------------------------------------------------**


1. Ensure the python runtime is greater than or equal to python3.5 

2. Run **pip install -r requirements.txt**

3. Create postgres user and table 

    3.1 Open postgres shell by: **psql**
    
    3.2 **CREATE USER fulfilio WITH PASSWORD 'fulfilio';**

4. Run database migration file: **python manage.py db upgrade**

5. Create flask server: **python manage.py server** 

6. Start the celery worker to accept jobs by command : **./worker_start.sh**

**-----------------------------------------------------------------------------------------**

**3. API DOCS**


**-----------------------------------------------------------------------------------------**


1. Search API

        """

        .. http:get::  /products

        This api will be used to filter and return products

        **Example request**:

        .. sourcecode:: http

           GET  /products?page="1"&name="name"&sku="sku"&description="desc"&status="active/inactive"  HTTP/1.1
           page is mandatory

        **Example response**:

            {
                "page": "1",
                "items": [
                    {
                        "name" : "Product name",
                        "sku" : "Sku name",
                        "status": "active/inactive",
                        "description": "product description"
                    },
                     {
                        "name" : "Product name",
                        "sku" : "Sku name 2",
                        "status": "active/inactive",
                        "description": "product description"
                    }
                    
                ]
            }

        .. sourcecode:: http

           HTTP/1.1 200 OK
           Vary: Accept


        :statuscode 200: success
        :statuscode 400: bad request error

        """