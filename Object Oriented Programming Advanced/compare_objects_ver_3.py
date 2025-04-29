# There might arise the need to compare objects in Python , but there is not such method, and it must be created

class Message:
    """
    This is the model of a Message
    """
    def __init__(self, message, date_of_transmission, sender):
        self.message = message
        self.data_of_transmission = date_of_transmission
        self.sender = sender

    def compare(self,other_object):
        if isinstance(other_object, Message):
            return self.message == other_object.message and self.sender== other_object.sender
        else:
            return False

messages_list = [
    Message("Hello", "2025-05-01 14:35", "George"),
    Message("How are you", "2025-04-01 17:35", "Mara"),
    Message("Thanks", "2025-12-14 10:35", "Sorina"),
]

# there appears a new message. one needs to compare it with existing ones to see whether to add it to the list or not

new_message = Message("Hello", "2024-12-31 23:45", "George")

is_found = any([message.compare(new_message) for message in messages_list])

if not is_found:
    print("The message was not found and will be added to the list")
    messages_list.append(new_message)

print(messages_list)

for message in messages_list:
    print(vars(message))