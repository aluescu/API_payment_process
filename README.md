# API_payment_process

# request format: http://address:port/bank account/name/expiring date/security code/amount
# OK test: http://address:port/5295910192068929/Popescu George/2020-10-31/123/30.00
# NOK test (date in past): http://address:port/5295910192068929/Popescu George/2020-10-25/123/30.00
# NOK test (missing decimal separator): http://address:port/5295910192068929/Popescu George/2020-10-25/123/3000
# if one of the test fails, error "400 bad request" is returned
# all tests mentioned in the code have been tested and working
# if all tests are good, request is made using same format to specific gateway, "200 OK" is returned
