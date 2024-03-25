print("Register to vote, your vote is your power to make a change")

party_list = []

def register_party(party_name, reg_number, member_count):
    if member_count >= 1000:
        party_list.append({
            "party_name": party_name,
            "reg_number": reg_number,
            "member_count": member_count

        })
        print("Registered!")

    else:
        print("not eligible to Register!")

register_party("nkata", 123, 500)

        


