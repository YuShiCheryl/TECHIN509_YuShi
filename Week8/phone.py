class iPhone:
    def __init__(self, name, phone_number):
        self.name = name
        self.phone_number = phone_number
        self.messages = []  # Stores all messages

    def set_name(self, new_name): # Change name
        self.name = new_name

    def send_message(self, recipient_number, message):
        #Send message to a phone number
        for phone in all_phones:
            if phone.phone_number == recipient_number:
                phone.receive_message(self.name, message)
                return
        print(f"No phone found with the number {recipient_number}")

    def receive_message(self, sender_name, message): 
        self.messages.append(f"From {sender_name}: {message}")
        # Receive message and put in inbox

    def check_messages(self):
        print(f"Messages for {self.name} ({self.phone_number}):")
        if not self.messages:
            print("No messages") # if no message 
        else:
            for msg in self.messages:
                print(msg) # Print all received messages


# create iPhones
phone1 = iPhone("Yanzu's iPhone", "123-456-7890")
phone2 = iPhone("Chaowei's iPhone", "987-654-3210")
phone3 = iPhone("Yu's iPhone", "814-777-8866")

all_phones = [phone1, phone2, phone3]

# Change names
phone1.set_name("Yanzu's iPhone 14 Pro")
phone2.set_name("Chaowei's iPhone 15 Pro Max")
phone3.set_name("Yu's iPhone 4")

# Send message
phone1.send_message("814-777-8866", "Hi Yu! I'm Wu Yanzu.")
phone2.send_message("814-777-8866", "Hi Yu! I'm Liang Chaowei.")

phone3.check_messages()