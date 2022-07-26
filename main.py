import downloads
from text_extraction import extract_article
from sentiment_analysis import sentiment_analyzer
from code import _paste_output


def _sentiment_analysis():
    """Helper function to initialize sentimental analysis for all the files"""
    variables = list()
    for i in range(1, 171):
        file_name = "files/articles/URL_" + str(i) + ".txt"
        variable = sentiment_analyzer(file_name)
        variables.append(variable)

    return variables



if __name__=="__main__":
    filename = "files/Input.xlsx"
    print("Extracting data from the urls....\n")
    extract_article(filename)
    print("\nPlease wait for some time this would take 15-20 mins:")
    variables = _sentiment_analysis()
    _paste_output(variables)