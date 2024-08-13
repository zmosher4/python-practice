subscribers = set()
unsubscribers = set()

def add_email(email, set_name): 
    set_name.add(email)
    print(f'{email} added')

def remove_email(email, set_name):
    if email in set_name:
        set_name.remove(email)
        print(f"{email} was removed")
    else:
        print('Email not found')

def display_emails(set_name):

    for email in set_name:
        print(email)

def find_active_subscribers():
    unique_subs = subscribers.difference(unsubscribers)
    for sub in unique_subs:
        print(sub)
   
        
# Adding emails to subscribers (notice that some people subscribe more than once)
add_email("user1@example.com", subscribers)
add_email("user3@example.com", subscribers)
add_email("user4@example.com", subscribers)
add_email("user11@example.com", subscribers)
add_email("user5@example.com", subscribers)
add_email("user6@example.com", subscribers)
add_email("user2@example.com", subscribers)
add_email("user5@example.com", subscribers)
add_email("user2@example.com", subscribers)
add_email("user7@example.com", subscribers)
add_email("user8@example.com", subscribers)
add_email("user9@example.com", subscribers)
add_email("user2@example.com", subscribers)
add_email("user11@example.com", subscribers)
add_email("user7@example.com", subscribers)
add_email("user10@example.com", subscribers)
add_email("user12@example.com", subscribers)

# Adding emails to unsubscribers
add_email("user6@example.com", unsubscribers)
add_email("user8@example.com", unsubscribers)
add_email("user1@example.com", unsubscribers)
add_email("user10@example.com", unsubscribers)

# Displaying subscribers and unsubscribers
print("All Subscribers:")
display_emails(subscribers)

print("All Unsubscribers:")
display_emails(unsubscribers)

# Finding active subscribers
print("Active Subscribers:")
find_active_subscribers()