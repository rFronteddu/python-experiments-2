import pandas


def nato_exercise():
    """
    This exercise accepts a sentence and produces nato phonetic alphabet translation for each word provided.
    """
    nato_data_frame = pandas.read_csv("nato_phonetic_alphabet.csv")
    nato_data_frame = {row.letter.casefold(): row.code for (index, row) in nato_data_frame.iterrows()}
    words = input("Enter one or more words:\n")
    for word in words.split():
        print("Spelling for word " + word + " is:")
        spelling = [nato_data_frame[letter.casefold()] for letter in word if letter.isalpha()]
        print(spelling)


# student_dict = {
#     "student": ["Angela", "James", "Lily"],
#     "score": [56, 76, 98]
# }

# #Looping through dictionaries:
# for (key, value) in student_dict.items():
#     #Access key and value
#     pass
#
# import pandas
# student_data_frame = pandas.DataFrame(student_dict)
#
# #Loop through rows of a data frame
# for (index, row) in student_data_frame.iterrows():
#     #Access index and row
#     #Access row.student or row.score
#     pass
#
# # Keyword Method with iterrows()
# # {new_key:new_value for (index, row) in df.iterrows()}
#

#

#
