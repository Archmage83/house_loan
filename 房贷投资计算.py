import requests
import json

# 商业贷款数额
com_amount = 240
# 公积金贷款数额
fund_amount = 0
# 贷款年数
years = 20
# same_all等额本息 same_base等额本金
pay_method = "same_base"
# 商业贷款利率
commercial_loan = 5.90
# 公积金贷款利率
housing_loan = 4.00

url = "http://fangd.sinaapp.com/home/calc?com_amount={}&fund_amount={}&year={}&com_rate_percent={}&fund_rate_percent={}&pay_method={}"

response = requests.get(url.format(com_amount, fund_amount, years, commercial_loan, housing_loan, pay_method))
res = json.loads(response.text)
print("贷款{}万，商业贷款{}万元，公积金贷款{}万元".format(com_amount + fund_amount, com_amount, fund_amount))
print("总支付利息=%.1f万元" % ((float(res["sum_com_interest"]) + float(res["sum_fund_interest"])) / 10000))

# 还款几年
return_year = 5

return_interest = 0
return_principal = 0
all_return = res["detail"]

for i in range(return_year * 12):
    obj = all_return[i]
    return_interest += float(obj["per_interest"])
    return_principal += float(obj["per_base"])

print("%d年后共还利息%.1f万元，本金%.1f万元，剩余本金%.1f万元" % (
return_year, return_interest / 10000, return_principal / 10000, (com_amount + fund_amount - return_principal / 10000)))
