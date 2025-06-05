def word_count(text):
    """
    Counts the number of words in a given text.
    
    Args:
        text (str): The text to count words in.
        
    Returns:
        int: The number of words in the text.
    """
    return len(text.split())

def char_count(text):
    """
    Counts the number of characters in a given text.
    
    Args:
        text (str): The text to count characters in.
        
    Returns:
        dictionary: total count of each character in a given text.
    """
    char_dict = {}

    for char in text:
        if not char.isalpha():
            continue
        char = char.lower()  # Normalize to lowercase for case-insensitive counting
        char_dict[char] = char_dict.get(char, 0) + 1

    return char_dict

def sort_char_dict(char_dict):
    """
    Sorts a character dictionary by count (numerical value) in descending order.
    
    Args:
        char_dict (dict): The dictionary to sort.
        
    Returns:
        list: A sorted list of tuples (character, count), sorted by count descending.
    """
    return sorted(char_dict.items(), key=lambda item: item[1], reverse=True)