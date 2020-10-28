# API_payment_process

# request format: http://gateway:port/bank account/name/date/security code/amount 
# OK test: http://127.0.0.1:5000/5295910192068929/Popescu George/2020-10-25/123/30.00 
# NOK test (date in future): http://127.0.0.1:5000/5295910192068929/Popescu George/2020-10-31/123/30.00  
# if one of the test fails, error "400 bad request" is returned 
# all tests mentioned in the code have been tested
# if all tests are good, request is made using same format to specific gateway, "200 OK" is returned
