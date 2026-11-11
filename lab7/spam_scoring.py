def sender_domain(email):
    """Return the lower-case domain from a basic email address, or an empty string."""
    if not isinstance(email, str):
        return ""
    local, separator, domain = email.strip().partition("@")
    if not separator or not local or not domain or "@" in domain:
        return ""
    if any(character.isspace() for character in domain):
        return ""
    return domain.lower()


def first_link(text):
    """Return the first whitespace-delimited HTTP(S) URL, or an empty string."""
    if not isinstance(text, str):
        return ""
    for token in text.split():
        start = token.find("http://")
        if start == -1:
            start = token.find("https://")
        if start != -1:
            link = token[start:].rstrip(".,!?;:)]}\"'")
            if link:
                return link
    return ""


def shout_ratio(text):
    """Return the fraction of alphabetic characters that are uppercase."""
    if not isinstance(text, str):
        return 0.0
    letters = [character for character in text if character.isalpha()]
    if not letters:
        return 0.0
    return sum(character.isupper() for character in letters) / len(letters)

def main():
    print("==== Running sender_domain ====")
    user_input = input("Enter a sender email (e.g. offers@Deals.com): ")
    result = sender_domain(user_input)
    print("Sender Domain:", result)

    print("\n==== Running first_link ====")
    user_input = input("Enter a message containing a link: ")
    result = first_link(user_input)
    print("First Link:", result)

    print("\n==== Running shout_ratio ====")
    user_input = input("Enter a message (e.g. FREE prize NOW): ")
    result = shout_ratio(user_input)
    print("Uppercase Ratio:", result)

if __name__ == "__main__":
    main()
