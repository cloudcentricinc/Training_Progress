def banner_text(text):
    screen_width = 80
    if len(text) > screen_width - 4:
        print("EEK!!")
        print("THE TEXT IS TOO LONG TO FIT IN THE SPECIFIED WIDTH")

    if text == "*":
        print("*" * screen_width)
    else:
        centred_text = text.center(screen_width - 4)
        output_string = "**{0}**".format(centred_text)
        print(output_string)


banner_text("*")
banner_text("I am")
banner_text("seeing")
banner_text("the world")
banner_text("dimensionally")
banner_text(" ")
banner_text(" with good and bad ")
banner_text("hate and love ")
banner_text(" trust and betrayal ")
banner_text("**                     ..                                                 **")
banner_text("birth and death all are same")
banner_text("circle of life")
banner_text("*")

result = banner_text("well you did not write anything")
print(result)

numbers = [4,5,6,7,8,9,1]
print(numbers.sort())