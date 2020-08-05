import json
from difflib import get_close_matches

data = json.load(open("data.json"))
word = input("Enter the word you want to search : ").lower()


def transalte(w):
    # ******************FIRST -CASE**********************************
    # when user will enter the correct word

    if w in data:
        #  w is the input value which will already be in string format
        #  so we don't need to use data["w"]
        # instead just data[w] will do
        return data[w]

    # ******************SECOND -CASE**********************************
    # Currently, when the user inputs a proper noun, such as Delhi or Paris,
    # the program will (1) convert that string into lowercase  and (2) it will look for the lowercase version (i.e. delhi or paris )
    # in the dataset. However, the dataset doesn't have delhi or paris. It only has Delhi and Paris.
    # Therefore, no definition is currently returned for proper nouns such as Delhi or Paris.
    # so we use title(),The title() method returns a string where the first character in every word is upper case

    elif w.title() in data:
        # if user entered "texas" this will check for "Texas" as well.
        return data[w.title()]

    # ******************THIRD -CASE***********************************
    # The program cannot return the definition of acronyms such as USA or NATO;
    # therefore, add another conditional to make the program return the definition of such words.
    # The upper() methods returns the uppercased string from the given string. It converts all lowercase characters to uppercase.

    elif w.upper() in data:
        # in case user enters words like USA or NATO
        return data[w.upper()]

    # *******************FOURTH -CASE**********************************
    # what is user mistakenly enters the wrong spelling
    # so if spelling is only little incorrect than we will display the option to user
    # where he can select if that was the word he wished to enter
    # like entering "rainn" instead of "rain"
    # but this section of elif will not work if word is completely incorrect, like "raeeen"
    # see video for this one 91,92,93,94(first two should be enough though)
    # get_close_matches(w, data.keys(), n=1, cutoff=0.8) will return list with maximum of a single value, because we set n=1

    elif len(get_close_matches(w, data.keys(), n=1, cutoff=0.8)) > 0:
        choice = input(
            f"Did you mean {get_close_matches(w, data.keys(), n=1, cutoff=0.8)} if yes then press 'Y' , if not then press any character ").upper()
        if choice == "Y":
            # get_close_matches(w, data.keys(), n=1, cutoff=0.8)[0] = it will give the first and only string from the list
            return data[get_close_matches(w, data.keys(), n=1, cutoff=0.8)[0]]
        else:
            return f"Word:'{w}' not found in the dictionary, please check spelling"

    # one more way of writing elif loop, basically here you will remove argument n=1 from get_close_matches
    # so without n=1, the list will by default have n=3 and store maximum 3 value
    # so everytime we will only take the first value from the list as it will be the closest value to out input string
    # elif len(get_close_matches(w, data.keys(), cutoff=0.8)) > 0:

    #     choice = input(
    #         f"Did you mean {get_close_matches(w, data.keys(), cutoff=0.8)[0]} if yes then press 'Y' , if not then press any character ").upper()
    #     if choice == "Y":
    #         # get_close_matches(w, data.keys(), n=1, cutoff=0.8)[0] = it will give the first and only string from the list
    #         return data[get_close_matches(w, data.keys(), cutoff=0.8)[0]]
    #     else:
    #         return f"Word {w} not found, please check spelling"

    # *******************FIFTH -CASE****************************
    # final case, When user enters completely wrong word
    else:
        return f"Word:'{w}' not found in the dictionary, please check spelling"

# this will give all definition all together in a list
# print(transalte(word))


# the below way will produce a nice looking output
better_output = transalte(word)
counter = 1
if type(better_output) == list:
    for items in better_output:
        print(f'{counter} : {items}')
        counter = counter + 1

    # or we can use enumerate function in forloop and avoid declaring counter

    # for i, items in enumerate(better_output):
    #     print(f'{i+1} : {items}') # i+1, bcoz by default indexing starts at zero

else:
    print(better_output)
