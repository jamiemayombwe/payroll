class PayRollViewModel(object):
    def __init__(self, id, start_date, end_date, pay_date, status, status_display_name, total_net_pay):
        self.id = id
        self.start_date = start_date
        self.end_date = end_date
        self.pay_date = pay_date
        self.status = status
        self.status_display_name = status_display_name
        self.total_net_pay = total_net_pay
