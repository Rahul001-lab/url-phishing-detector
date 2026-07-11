import validators
import ipaddress
from urllib.parse import urlparse
import re
import requests
from urllib.parse import urlparse
from datetime import datetime
import whois

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
    
    # Check Digits in Domain

def check_digits(url):

    hostname = urlparse(url).hostname

    if hostname is None:
        return 0, "Unable to check domain."

    digits = re.findall(r'\d', hostname)

    if len(digits) == 0:
        return 0, "No digits found in domain."

    elif len(digits) <= 2:
        return 10, f"Domain contains {len(digits)} digit(s)."

    else:
        return 20, f"Domain contains many digits ({len(digits)})."

        # Check Suspicious Keywords

def check_suspicious_keywords(url):

    suspicious_words = [
        "login",
        "verify",
        "secure",
        "update",
        "account",
        "banking",
        "password",
        "signin",
        "confirm",
        "wallet",
        "payment"
    ]

    url = url.lower()

    found_words = []

    for word in suspicious_words:

        if word in url:
            found_words.append(word)

    if len(found_words) == 0:
        return 0, "No suspicious keywords found."

    elif len(found_words) <= 2:
        return 15, f"Suspicious keywords found: {', '.join(found_words)}."

    else:
        return 30, f"Multiple suspicious keywords found: {', '.join(found_words)}."
    
    # Check URL Shortener

def check_url_shortener(url):

    shorteners = [
        "bit.ly",
        "tinyurl.com",
        "goo.gl",
        "t.co",
        "is.gd",
        "ow.ly",
        "buff.ly",
        "rebrand.ly",
        "cutt.ly",
        "shorturl.at"
    ]

    hostname = urlparse(url).hostname

    if hostname is None:
        return 0, "Unable to check URL shortener."

    hostname = hostname.lower()

    for shortener in shorteners:

        if shortener == hostname:
            return 25, f"URL uses a shortening service ({shortener})."

    return 0, "No URL shortening service detected."

    # Check Double Slash

def check_double_slash(url):

    position = url.rfind("//")

    if position > 7:
        return 15, "Extra double slash found in URL."

    return 0, "No extra double slash found."

# Check Suspicious TLD

def check_suspicious_tld(url):

    suspicious_tlds = [
        ".xyz",
        ".top",
        ".click",
        ".gq",
        ".cf",
        ".ml",
        ".tk",
        ".work",
        ".zip"
    ]

    hostname = urlparse(url).hostname

    if hostname is None:
        return 0, "Unable to check TLD."

    for tld in suspicious_tlds:

        if hostname.endswith(tld):
            return 20, f"Suspicious TLD detected ({tld})."

    return 0, "No suspicious TLD detected."

# Encoded Character Detection

#def check_encoded_characters(url):
    encoded_pattern = re.compile(r'%[0-9A-Fa-f]{2}')

 #   if encoded_pattern.findall(url):
    #    return 15, "URL contains encoded characters."

    #return 0, "No encoded characters found."

# Encoded Character Detection

def check_encoded_characters(url):

    encoded_pattern = re.compile(r'%[0-9A-Fa-f]{2}')

    matches = encoded_pattern.findall(url)

    count = len(matches)

    if count == 0:
        return 0, "No encoded characters found."

    elif count <= 2:
        return 10, f"URL contains {count} encoded character(s)."

    else:
        return 20, f"URL contains multiple encoded characters ({count})."

# Redirect Detection

#def check_redirects(url):
    parsed_url = urlparse(url)

 #   if parsed_url.fragment:
  #      return 15, "URL contains a fragment (possible redirect)."

   # if parsed_url.query:
    #    return 10, "URL contains query parameters (possible redirect)."

    #return 0, "No redirects detected."

def check_redirects(url):

    try:

        response = requests.get(url, timeout=5)

        redirect_history = response.history

        redirect_count = len(redirect_history)

        if redirect_count == 0:
            return 0, "No redirects detected."

        original_host = urlparse(url).hostname
        final_host = urlparse(response.url).hostname

    # Normal HTTP → HTTPS redirect on the same domain

        if original_host == final_host:
            return 0, "Redirected to HTTPS on the same domain."

    # Redirect to another domain

        return 20, f"URL redirected {redirect_count} time(s) to another domain."

    except requests.exceptions.RequestException:

        return 10, "Unable to check redirects."

#unicode/Punycode Detection   

def check_punycode_domain(url):

    hostname = urlparse(url).hostname

    if hostname is None:
        return 0, "Unable to check domain."

    if "xn--" in hostname:
        return 20, "Punycode domain detected."

    return 0, "No Punycode domain detected."

# Check domain age using whois(pip intall python-whois)

def check_domain_age(url):

    hostname = urlparse(url).hostname

    if hostname is None:
        return 0, "Unable to check domain age."

    try:

        domain_info = whois.whois(hostname)

        creation_date = domain_info.creation_date

        if creation_date is None:
            return 0, "Unable to determine domain age."

        if isinstance(creation_date, list):
            creation_date = creation_date[0]

        current_date = datetime.now()

        domain_age_days = (current_date - creation_date).days

        if domain_age_days < 180:
            return 20, f"Domain age is less than 6 months ({domain_age_days} days)."

        return 0, f"Domain age is {domain_age_days} days (appears established)."

    except Exception:
        return 0, "Unable to check domain age."