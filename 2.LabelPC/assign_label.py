import pickle
from collections import Counter
from dict_labels import asset_labels


def main():
    # open P_dict
    P_dict = open('../OUTPUT/TEMP/P_dict.p', 'rb')
    P_dict = pickle.load(P_dict)


    for P in P_dict:
        # Get RGB list for each point
        RGB_list = []
        for Im in P.ImageData_list:
            RGB = tuple(Im.RGB)
            RGB_list.append(RGB)
        # get label and assign
        RGB_voted = vote(RGB_list)
        P.asset_type = get_label(RGB_voted)

    pickle.dump(P_dict, open('../OUTPUT/TEMP/P_dict_labelled.p', "wb"))
    print('Added labels')


def get_label(RGB_voted):
    key = str(RGB_voted)
    label = asset_labels[key]
    return label


def vote(RGB_list):
    counter = Counter(RGB_list)
    voted = counter.most_common(1)[0][0]
    return voted


main()
