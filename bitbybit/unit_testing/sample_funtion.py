
def get_data(name, last, email, ph=None, add=None, bg=None):
    if ph and add and bg:
        return "pankaj","gosavi","pankajgosavi1029@gmail.com", "solapur", "o+", "9766588937"
    if ph and bg:
        return "pankaj", "gosavi", "pankajgosavi1029@gmail.com", "o+", "9766588937"
    if ph and add:
        return "pankaj", "gosavi", "pankajgosavi1029@gmail.com", "solapur", "9766588937"
    if add and bg:
        return "pankaj", "gosavi", "pankajgosavi1029@gmail.com", "solapur", "o+"
    if ph:
        return "pankaj","gosavi","pankajgosavi1029@gmail.com","9766588937"
    if bg:
        return "pankaj", "gosavi", "pankajgosavi1029@gmail.com", "o+"
    if add:
        return "pankaj","gosavi","pankajgosavi1029@gmail.com","solapur"

    return "pankaj","gosavi","pankajgosavi1029@gmail.com"