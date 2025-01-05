# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


from typing import Text, Dict, Any, List
from rasa_sdk import Action, Tracker, FormValidationAction
from rasa_sdk.events import Restarted
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.types import DomainDict
import re
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

class ValidateProductForm(FormValidationAction):
    def name(self) -> Text:
        return "validate_product_form"

    def validate_product_name(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict,
    ) -> Dict[Text, Any]:
        """Validate product name."""

        products = ["FirewoodTypeA", "FirewoodTypeB", "FirewoodTypeC"]
        products_lower = ["firewoodtypea", "firewoodtypeb", "firewoodtypec"]
        # Check if the name is in the list of product names
        slot_value_lower = slot_value.lower()
        if slot_value_lower in products_lower:
            pos = products_lower.index(slot_value_lower)
            return {"product_name": products[pos]}
        else:
            dispatcher.utter_message(text = "Please provide a valid product name.")
            return {"product_name": None}
       
    def validate_product_quantity(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict,
    ) -> Dict[Text, Any]:
        """Validate quantity of product."""

        # Check if the quantity provided is a number and is greater than 0
        try:
            # Try converting the input to a float
            float(slot_value)
            if float(slot_value) > 0:
                return {"product_quantity": slot_value}
            else:
                dispatcher.utter_message(text="Please provide a valid number.")
                return {"product_quantity": None}
        except ValueError:
            dispatcher.utter_message(text="Please provide a valid number.")
            return {"product_quantity": None}
    
    def validate_product_size(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict,
    ) -> Dict[Text, Any]:
        """Validate size of product."""

        sizes = ["40", "33", "25"]
        # Check if the size is in the list of product sizes
        slot_value_num = slot_value[:2]
        if slot_value_num in sizes:
            return {"product_size": slot_value_num}
        else:
            dispatcher.utter_message(text = "Please provide a valid size (40/33/25 cm.")
            return {"product_size": None}
        
class ValidateProductFormTwo(FormValidationAction):
    def name(self) -> Text:
        return "validate_product_form_two"

    def validate_product_name_2(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict,
    ) -> Dict[Text, Any]:
        """Validate product name."""

        products = ["FirewoodTypeA", "FirewoodTypeB", "FirewoodTypeC"]
        products_lower = ["firewoodtypea", "firewoodtypeb", "firewoodtypec"]
        # Check if the name is in the list of product names
        slot_value_lower = slot_value.lower()
        if slot_value_lower in products_lower:
            pos = products_lower.index(slot_value_lower)
            return {"product_name_2": products[pos]}
        else:
            dispatcher.utter_message(text = "Please provide a valid product name.")
            return {"product_name_2": None}
        
    def validate_product_quantity_2(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict,
    ) -> Dict[Text, Any]:
        """Validate quantity of product."""

        # Check if the quantity provided is a number and is greater than 0
        try:
            # Try converting the input to a float
            float(slot_value)
            if float(slot_value) > 0:
                return {"product_quantity_2": slot_value}
            else:
                dispatcher.utter_message(text="Please provide a valid number.")
                return {"product_quantity_2": None}
        except ValueError:
            dispatcher.utter_message(text="Please provide a valid number.")
            return {"product_quantity_2": None}
    
    def validate_product_size_2(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict,
    ) -> Dict[Text, Any]:
        """Validate size of product."""

        sizes = ["40", "33", "25"]
        # Check if the size is in the list of product sizes
        slot_value_num = slot_value[:2]
        if slot_value_num in sizes:
            return {"product_size_2": slot_value_num}
        else:
            dispatcher.utter_message(text = "Please provide a valid size (40/33/25 cm.")
            return {"product_size_2": None}

class ValidateProductFormThree(FormValidationAction):
    def name(self) -> Text:
        return "validate_product_form_three"

    def validate_product_name_3(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict,
    ) -> Dict[Text, Any]:
        """Validate product name."""

        products = ["FirewoodTypeA", "FirewoodTypeB", "FirewoodTypeC"]
        products_lower = ["firewoodtypea", "firewoodtypeb", "firewoodtypec"]
        # Check if the name is in the list of product names
        slot_value_lower = slot_value.lower()
        if slot_value_lower in products_lower:
            pos = products_lower.index(slot_value_lower)
            return {"product_name_3": products[pos]}
        else:
            dispatcher.utter_message(text = "Please provide a valid product name.")
            return {"product_name_3": None}
       
    def validate_product_quantity_3(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict,
    ) -> Dict[Text, Any]:
        """Validate quantity of product."""

        # Check if the quantity provided is a number and is greater than 0
        try:
            # Try converting the input to a float
            float(slot_value)
            if float(slot_value) > 0:
                return {"product_quantity_3": slot_value}
            else:
                dispatcher.utter_message(text="Please provide a valid number.")
                return {"product_quantity_3": None}
        except ValueError:
            dispatcher.utter_message(text="Please provide a valid number.")
            return {"product_quantity_3": None}
    
    def validate_product_size_3(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict,
    ) -> Dict[Text, Any]:
        """Validate size of product."""

        sizes = ["40", "33", "25"]
        # Check if the size is in the list of product sizes
        slot_value_num = slot_value[:2]
        if slot_value_num in sizes:
            return {"product_size_3": slot_value_num}
        else:
            dispatcher.utter_message(text = "Please provide a valid size (40/33/25 cm.")
            return {"product_size_3": None}

class ActionCalculatePrice(Action):
    def name(self) -> Text:
        return "action_calculate_price"

    def run(self,
           dispatcher: CollectingDispatcher,
           tracker: Tracker,
           domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        # Get slots from entities from user's responses depending on the last form filled
        last_action_name = tracker.latest_action_name

        if last_action_name == "product_form":
            product_name = tracker.get_slot('product_name')
            product_quantity = int(tracker.get_slot('product_quantity'))
            product_size = int(tracker.get_slot('product_size'))
            price = self.calculate_price(product_name = product_name, product_quantity = product_quantity, product_size = product_size)
            dispatcher.utter_message(response="utter_price", product_name = product_name, product_quantity = product_quantity, product_size = product_size, price = price)
        elif last_action_name == "product_form_two":
            product_name = tracker.get_slot('product_name_2')
            product_quantity = int(tracker.get_slot('product_quantity_2'))
            product_size = int(tracker.get_slot('product_size_2'))
            price = self.calculate_price(product_name = product_name, product_quantity = product_quantity, product_size = product_size)
            dispatcher.utter_message(response="utter_price", product_name = product_name, product_quantity = product_quantity, product_size = product_size, price = price)
        elif last_action_name == "product_form_three":
            product_name = tracker.get_slot('product_name_3')
            product_quantity = int(tracker.get_slot('product_quantity_3'))
            product_size = int(tracker.get_slot('product_size_3'))
            price = self.calculate_price(product_name = product_name, product_quantity = product_quantity, product_size = product_size)
            dispatcher.utter_message(response="utter_price", product_name = product_name, product_quantity = product_quantity, product_size = product_size, price = price)

    def calculate_price(self,
                       product_name, 
                       product_quantity, 
                       product_size):        
        # Calculate price
        if product_name == "FirewoodTypeA":
            if product_quantity >= 8:
                number_of_trailers = int((product_quantity/8)//1)
                eight_cubic_value = 8 * number_of_trailers
                remaining_value = product_quantity - eight_cubic_value
                if product_size == 40:
                    price = (99 * eight_cubic_value) + (109 * remaining_value)
                elif product_size == 33:
                    price = (104 * eight_cubic_value) + (114 * remaining_value)
                elif product_size == 33:
                    price = (109 * eight_cubic_value) + (119 * remaining_value)
            elif product_quantity < 8:
                if product_size == 40:
                    price = 109 * product_quantity
                elif product_size == 33:
                    price = 114 * product_quantity
                elif product_size == 25:
                    price = 119 * product_quantity
        elif product_name == "FirewoodTypeB":
            price = 0
        elif product_name == "FirewoodTypeC":
            price = 0
    
        return price
   
class ValidateDeliveryForm(FormValidationAction):
    def name(self) -> Text:
        return "validate_delivery_form"

    def validate_customer_name(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict,
    ) -> Dict[Text, Any]:
        """Validate name."""

        # Get the text of the latest message
        slot_value = tracker.latest_message.get('text')

        # Check if the name contains only alphabetic characters and spaces
        if re.fullmatch(r"(?i)^[a-zäöüßéèàç]+([-'\s][a-zäöüßéèàç]+)*$", slot_value):
            # Name is valid
            return {"customer_name": slot_value}
        else:
            # Name is invalid
            dispatcher.utter_message(text = "Please provide a valid name.")
            return {"customer_name": None}
       
    def validate_phone_number(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict,
    ) -> Dict[Text, Any]:
        """Validate phone number."""

        phone_number_regex = "^(\+49|0049|0)?\s*([1-9]\d{1,4})\s*(\d{1,11})(\s*\d{1,11})?$"
        if re.match(phone_number_regex, slot_value.lower()):
            return {"phone_number": slot_value}
        else:
            dispatcher.utter_message(text = "Please provide a valid phone number.")
            return {"phone_number": None}
    
    def validate_address(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict,
    ) -> Dict[Text, Any]:
        """Validate address."""

        # Get the text of the latest message
        slot_value = tracker.latest_message.get('text')

        # Check if the address has a minimum length of 12 characters
        if len(slot_value) >= 12:
            return {"address": slot_value}
        else:
            dispatcher.utter_message(text="Please provide a more detailed address.")
            return {"address": None}
        
    def validate_email_address(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict,
    ) -> Dict[Text, Any]:
        """Validate email address."""

        # Simple email regex
        email_pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
        
        if re.fullmatch(email_pattern, slot_value):
            return {"email_address": slot_value}
        else:
            dispatcher.utter_message(text="Please enter a valid email address.")
            return {"email_address": None}

class ValidateContactInfo(FormValidationAction):
    def name(self) -> Text:
        return "validate_contact_form"

    def validate_customer_name(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict,
    ) -> Dict[Text, Any]:
        """Validate name."""

        # Get the text of the latest message
        slot_value = tracker.latest_message.get('text')
        
        # Check if the name contains only alphabetic characters and spaces
        if re.fullmatch(r"(?i)^[a-zäöüßéèàç]+([-'\s][a-zäöüßéèàç]+)*$", slot_value):
            # Name is valid
            return {"customer_name": slot_value}
        else:
            # Name is invalid
            dispatcher.utter_message(text = "Please provide a valid name.")
            return {"customer_name": None}
       
    def validate_phone_number(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict,
    ) -> Dict[Text, Any]:
        """Validate phone number."""

        phone_number_regex = "^(\+49|0049|0)?\s*([1-9]\d{1,4})\s*(\d{1,11})(\s*\d{1,11})?$"
        if re.match(phone_number_regex, slot_value.lower()):
            return {"phone_number": slot_value}
        else:
            dispatcher.utter_message(text = "Please provide a valid phone number.")
            return {"phone_number": None}
        
    def validate_email_address(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict,
    ) -> Dict[Text, Any]:
        """Validate email address."""

        # Simple email regex
        email_pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
        
        if re.fullmatch(email_pattern, slot_value):
            return {"email_address": slot_value}
        else:
            dispatcher.utter_message(text="Please enter a valid email address.")
            return {"email_address": None}

class ActionSayDeliveryInfo(Action):
    def name(self) -> Text:
        return "action_say_delivery_info"

    def run(self,
           dispatcher: CollectingDispatcher,
           tracker: Tracker,
           domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        customer_name = tracker.get_slot('customer_name')
        phone_number = tracker.get_slot('phone_number')
        address = tracker.get_slot('address')
        email_address = tracker.get_slot('email_address')

        # Create a message using the variables
        message = f"These are the delivery details you have provided:\nName: {customer_name}\nPhone Number: {phone_number}\nAddress: {address}\nEmail Address: {email_address}.\n"
        
        # Utter the message
        dispatcher.utter_message(text=message)
        
        return []

class ActionSendOrderEmail(Action):

    def name(self) -> str:
        return "action_send_order_email"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: DomainDict) -> list:

        # Retrieve data from slots
        product_name = tracker.get_slot("product_name")
        product_quantity = tracker.get_slot("product_quantity")
        product_size = tracker.get_slot("product_size")
        product_name_2 = tracker.get_slot("product_name_2")
        product_quantity_2 = tracker.get_slot("product_quantity_2")
        product_size_2 = tracker.get_slot("product_size_2")
        product_name_3 = tracker.get_slot("product_name_3")
        product_quantity_3 = tracker.get_slot("product_quantity_3")
        product_size_3 = tracker.get_slot("product_size_3")
        customer_name = tracker.get_slot("customer_name")
        phone_number = tracker.get_slot("phone_number")
        address = tracker.get_slot("address")
        email_address = tracker.get_slot("email_address")

        # Email sending logic
        sender_email = "baidoo394@gmail.com"
        sender_password = "yldy dzup mena goyl"
        recipient_email = "baidoo394@gmail.com"
        # Create the email message
        message = MIMEMultipart()
        message['From'] = sender_email
        message['To'] = recipient_email
        message['Subject'] = f'''Order {product_name}'''
        if product_name_2 == None:
            email_body = f'''Hello,\n\nI just ordered {product_quantity} cubic meters of {product_size} cm {product_name}. Please find below my delivery details.\n\nOrder:\nProduct: {product_name}\nQuantity: {product_quantity} cubic meters\nSize: {product_size}cm\n\nDelivery Details:\nName: {customer_name}\nPhone number: {phone_number}\nEmail address: {email_address}\nDelivery address: {address}\n\nBest Regards\n{customer_name}'''
        elif (product_name_2 != None) & (product_name_3 == None):
            email_body = f'''Hello,\n\nI just made some orders. Please find below my delivery details.\n\nFirst Order:\nProduct: {product_name}\nQuantity: {product_quantity} cubic meters\nSize: {product_size}cm\n\nSecond Order:\nProduct: {product_name_2}\nQuantity: {product_quantity_2} cubic meters\nSize: {product_size_2}cm\n\nDelivery Details:\nName: {customer_name}\nPhone number: {phone_number}\nEmail address: {email_address}\nDelivery address: {address}\n\nBest Regards\n{customer_name}'''
        elif (product_name_2 != None) & (product_name_3 != None):
            email_body = f'''Hello,\n\nI just made some orders. Please find below my delivery details.\n\nFirst Order:\nProduct: {product_name}\nQuantity: {product_quantity} cubic meters\nSize: {product_size}cm\n\nSecond Order:\nProduct: {product_name_2}\nQuantity: {product_quantity_2} cubic meters\nSize: {product_size_2}cm\n\nThird Order:\nProduct: {product_name_3}\nQuantity: {product_quantity_3} cubic meters\nSize: {product_size_3}cm\n\nDelivery Details:\nName: {customer_name}\nPhone number: {phone_number}\nEmail address: {email_address}\nDelivery address: {address}\n\nBest Regards\n{customer_name}'''
        # Attach the body of the email
        message.attach(MIMEText(email_body, 'plain'))
        try:
            # Connect to the SMTP server
            server = smtplib.SMTP('smtp.gmail.com', 587)
            server.starttls()  # Upgrade the connection to a secure encrypted SSL/TLS connection
            server.login(sender_email, sender_password)

            # Send the email
            server.sendmail(sender_email, recipient_email, message.as_string())
            server.close()
        except Exception as e:
            print(f"Failed to send email: {str(e)}")

        return []
    
class ActionSendContactEmail(Action):

    def name(self) -> str:
        return "action_send_contact_email"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: DomainDict) -> list:

        # Retrieve data from slots
        customer_name = tracker.get_slot("customer_name")
        phone_number = tracker.get_slot("phone_number")
        email_address = tracker.get_slot("email_address")

        # Email sending logic
        sender_email = "baidoo394@gmail.com"
        sender_password = "yldy dzup mena goyl"
        recipient_email = "baidoo394@gmail.com"

        # Create the email message
        message = MIMEMultipart()
        message['From'] = sender_email
        message['To'] = recipient_email
        message['Subject'] = "Talk to Staff"
        email_body = f'''Hello,\n\nI would like to talk to a staff directly. Please find below my contact information.\n\nName: {customer_name}\nPhone number: {phone_number}\nEmail address: {email_address}\n\nBest Regards\n{customer_name}'''

        # Attach the body of the email
        message.attach(MIMEText(email_body, 'plain'))

        try:
            # Connect to the SMTP server
            server = smtplib.SMTP('smtp.gmail.com', 587)
            server.starttls()  # Upgrade the connection to a secure encrypted SSL/TLS connection
            server.login(sender_email, sender_password)

            # Send the email
            server.sendmail(sender_email, recipient_email, message.as_string())
            server.close()
        except Exception as e:
            print("Failed to send the email: {str(e)}")

        return []
    
class ActionRestartConversation(Action):

    def name(self) -> str:
        return "action_restart_conversation"

    def run(self, dispatcher, tracker, domain):
        # Return the Restarted event to reset the conversation
        return [Restarted()]