# BookBackend
## Introduce
* This is the backend repo for micro service of book management.
* Developing Language: Python3
* Developing Framework: Django

### Restful APIs
* Create a book : http://xxx/bookmanage/book/create
* Read a book   : http://xxx/bookmanage/book/read/id http://xxx/bookmanage/book/read/name
* Delete books  : http://xxx/bookmanager/book/delete
* Search books  : http://xxx/bookmanager/book/search

### Set up and Run
1. Clone the repo into your local Linux environment.       
    ```$ git clone https://github.com/millerblack/BookBackend.git```
2. Use manage.py to run Book Manager website.
    ```
    $ cd BookBackend/BookManagement/
    $ python3 manage.py runserver 0:8000
    ```
3. Access the Book Manager website by browser(eg: Chrome)          
    For local:  http://0.0.0.0:8000/book/      
    For remote: http://<ip_BookManager_server>:8000/book/        
