from paypalrestsdk import BillingPlan, ResourceNotFound, BillingAgreement


class PaypalAPI:
    """
    Please config paypalrestsdk first. Example:


        ```
        paypalrestsdk.configure({
            "mode": "sandbox",  # sandbox or live
            "client_id": "5b91f4c1-dd3r-4a8a-acef-e3e3efg32",
            "client_secret": "5b91f4c1-dd3r-4a8a-acef-e3e3efg32"
        })
        ```
    """

    def __init__(self):
        pass

    def get_billing_plans(self, status="ACTIVE"):
        """
        status: CREATED, ACTIVE, INACTIVE, ALL

        :param status:
        :return:
        """
        plans = BillingPlan.all({"status": status})
        if 'plans' in plans:
            return plans["plans"]
        return []

    def create_billing_plan(self, name, description, cancel_url, return_url, amount, frequency, payment_name):
        billing_plan = BillingPlan({
            "name": name,
            "description": description,
            "merchant_preferences": {
                "auto_bill_amount": "yes",
                "cancel_url": cancel_url,
                "return_url": return_url,
                # "notify_url": "http://webhook.moonz.info/5b91f4c1-dd3r-4a8a-acef-e3e3efg32",
                "initial_fail_amount_action": "continue",
                "max_fail_attempts": "1",
                "setup_fee": {
                    "currency": "USD",
                    "value": "0"
                }
            },
            "payment_definitions": [
                {
                    "amount": {
                        "currency": "USD",
                        "value": amount
                    },
                    "cycles": "0",
                    "frequency": frequency,
                    "frequency_interval": "1",
                    "name": payment_name,
                    "type": "REGULAR"
                }
            ],
            "type": "INFINITE"
        })

        if billing_plan.create():
            return True, billing_plan
        print(billing_plan.error)
        return False, billing_plan.error['message']

    def active_plan(self, plan_id):
        try:
            billing_plan = BillingPlan.find(plan_id)

            if billing_plan.activate():
                return billing_plan.state
            else:
                raise Exception(billing_plan.error['message'])

        except ResourceNotFound as error:
            raise Exception("Billing Plan Not Found")

    def get_plan(self, plan_id):
        try:
            billing_plan = BillingPlan.find(plan_id)
            return billing_plan
        except ResourceNotFound as error:
            print("Billing Plan Not Found")


paypal = PaypalAPI()
