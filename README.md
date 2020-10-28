# API_payment_process

# request format: http://gateway:port/bank account/name/date/security code/amount 
# OK test: http://127.0.0.1:5000/5295910192068929/Popescu George/2020-10-25/123/30.00 
# NOK test (date in future): http://127.0.0.1:5000/5295910192068929/Popescu George/2020-10-31/123/30.00 
# all tests mentioned in the code have been tested # if one of the test fails, error "400 bad request" is returned 
# if all tests are good,make request with same format to specific gateway, "200 OK" is returned
