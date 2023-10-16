# -*- coding: utf-8 -*-
"""
Created on Tue Sep 26 12:34:16 2023

@author: 97154
"""
"""
Ex 5 Change Guest List
"""
Question Chapter 3 Exercise 5.
#You just heard that one of your guests can’t make the dinner, so you need to send out a new set of invitations. You’ll have to think of someone else to invite.
#•Start with your program from Exercise 3-4. Add a print() call at the end of your program stating the name of the guest who can’t make it.
#•Modify your list, replacing the name of the guest who can’t make it with the name of the new person you are inviting.
#•Print a second set of invitation messages, one for each person who is still in your list.

Explanation:
#A message stating that a guest can't make it. Then, we replace the name of the guest who can't make it with a new person, in this case, 
#"Isaac Newton." Finally, we send out new dinner invitations to the updated list of guests.
"""
#Code:
"""
# List of people to invite to dinner
guests = ["Albert Einstein", "Marie Curie", "Leonardo da Vinci"]

# Print a message for the guest who can't make it
guest_cant_make_it = "Marie Curie"
print(f"Unfortunately, {guest_cant_make_it} can't make it to the dinner.")

# Replace the name of the guest who can't make it with a new person
new_guest = "Isaac Newton"
guests[guests.index(guest_cant_make_it)] = new_guest

# Send dinner invitations to the updated list of guests
for guest in guests:
    invitation = f"Dear {guest}, you are cordially invited to dinner. Please join us for a delightful evening."
    print(invitation)

