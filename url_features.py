import validators
import ipaddress
from urllib.parse import urlparse

# Validate URL

def validate_url(url):

    if validators.url(url):
        return True

    return False


# Check HTTPS

def check_https(url):

    if url.startswith("https://"):
        return 0, "Uses HTTPS connection."

    return 20, "Does not use HTTPS."


# Check URL Length

def check_url_length(url):

    length = len(url)

    if length < 50:
        return 0, f"URL length is normal ({length} characters)."

    elif length < 75:
        return 10, f"URL is a little long ({length} characters)."

    else:
        return 20, f"URL is very long ({length} characters)."
    
    # Check IP Address

def check_ip_address(url):

    try:

        hostname = urlparse(url).hostname

        ipaddress.ip_address(hostname)

        return 25, "URL contains an IP address."

    except:

        return 0, "URL uses a domain name."
    
    # Check @ Symbol

def check_at_symbol(url):

    if "@" in url:
        return 20, "URL contains '@' symbol."

    return 0, "No '@' symbol found."

# Check Number of Dots

def check_dots(url):

    dot_count = url.count(".")

    if dot_count <= 2:
        return 0, f"Normal number of dots ({dot_count})."

    elif dot_count <= 4:
        return 10, f"URL contains multiple dots ({dot_count})."

    else:
        return 20, f"URL contains too many dots ({dot_count})."
    
    # Check Hyphens

def check_hyphen(url):

    hostname = urlparse(url).hostname

    if hostname is None:
        return 0, "Unable to check domain."

    hyphen_count = hostname.count("-")

    if hyphen_count == 0:
        return 0, "No hyphens found in domain."

    elif hyphen_count <= 2:
        return 10, f"Domain contains {hyphen_count} hyphen(s)."

    else:
        return 20, f"Domain contains many hyphens ({hyphen_count})."