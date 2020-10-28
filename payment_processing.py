# API_payment_process

# request format: http://address:port/bank account/name/expiring date/security code/amount
# OK test: http://address:port/5295910192068929/Popescu George/2020-10-31/123/30.00
# NOK test (date in past): http://address:port/5295910192068929/Popescu George/2020-10-25/123/30.00
# NOK test (missing decimal separator): http://address:port/5295910192068929/Popescu George/2020-10-25/123/3000
# if one of the test fails, error "400 bad request" is returned
# all tests mentioned in the code have been tested and working
# if all tests are good, request is made using same format to specific gateway, "200 OK" is returned

from flask import Flask
from datetime import datetime
import re
import requests


app = Flask(__name__);


@app.route('/<string:card_numb>/<string:name>/<string:exp_date>/<string:sec_code>/<float:amount>', methods=['GET'])
def ProcessPayment(card_numb, name, exp_date, sec_code, amount):

##TESTS

    # list contains all test results
    t_all_res = [];

    # CARD NUMBER

    # test if number is missing
    if card_numb == "":
        t_all_res.append("NOK");

    # test if number contains characters
    if re.search('[a-zA-Z]', card_numb) is not None:
        t_all_res.append("NOK");

    # test for card number length
    if len(card_numb) != 16:
        t_all_res.append("NOK");

##NAME

    #test if name is missing
    if name == "":
        t_all_res.append("NOK");

    #test is using minimum one space
    if re.search('[ ]', name) is None:
        t_all_res.append("NOK");

    #test if name contains digits
    if re.search('[0-9]', name) is not None:
        t_all_res.append("NOK");

##DATE

    #test if date is missing
    if exp_date == "":
        t_all_res.append("NOK");

    #test date format
    try:
        datetime.strptime(exp_date, '%Y-%m-%d');

        #test date is in the past
        if datetime.strptime(exp_date, '%Y-%m-%d') < datetime.now():
            t_all_res.append("NOK");
    except ValueError:
        t_all_res.append("NOK");

##SEC_CODE

    # test code length
    if len(sec_code) != 3:
        t_all_res.append("NOK");

    # code contains letters
    if re.search('[a-zA-Z]', sec_code) is not None:
        t_all_res.append("NOK");

##AMOUNT

    # test if amount is missing
    if amount == "":
        t_all_res.append("NOK");

    #test if amount contains decimal separator
    if re.search('[.]', str(amount)) is None:
        t_all_res.append("NOK");

    #test if amount contains characters
    if re.search('[a-zA-Z]', str(amount)) is not None:
        t_all_res.append("NOK");

    #test if amount is positive
    if amount < 0:
        t_all_res.append("NOK");

    ##PROCESS PAYMENT CHECK & REQUEST TO RIGHT GATEWAY
    if "NOK" in t_all_res:
        return "400 bad request";
    if amount < 20:
            requests.get('https://cheappaymentgateway.com/%s/%s/%s/%s/%f'%(card_numb,name,exp_date,sec_code,amount));
    if amount  in range(21,500):
            requests.get('https://expensivepaymentgateway.com/%s/%s/%s/%s/%f'%(card_numb,name,exp_date,sec_code,amount));
    if amount > 500:
            requests.get('https://premiumpaymentgateway.com/%s/%s/%s/%s/%f'%(card_numb,name,exp_date,sec_code,amount));
    return "200 OK";


@app.errorhandler(404)
def page_not_found(e):
    return "400 bad request";


if __name__ == '__main__':
    app.run();
