from url_features import (
    validate_url,
    check_https,
    check_url_length,
    check_ip_address,
    check_at_symbol,
    check_dots,
    check_hyphen,
    check_digits,
    check_suspicious_keywords
)

def scan_url(url):

    score = 0
    reasons = []

 # Validate URL

    if not validate_url(url):

        return {
            "status": "Invalid URL",
            "score": 100,
            "reasons": [
                "The entered URL is not valid."
            ]
        }

 # HTTPS Check

    points, message = check_https(url)

    score += points
    reasons.append(message)

# URL Length Check

    points, message = check_url_length(url)

    score += points
    reasons.append(message)

 # IP Address Check

    points, message = check_ip_address(url)

    score += points
    reasons.append(message)

 # @ Symbol Check

    points, message = check_at_symbol(url)

    score += points
    reasons.append(message)

 # Dot Check

    points, message = check_dots(url)

    score += points
    reasons.append(message)

# Hyphen Check

    points, message = check_hyphen(url)

    score += points
    reasons.append(message)

# Digits Check

    points, message = check_digits(url)

    score += points
    reasons.append(message)

# Suspicious Keywords Check

    points, message = check_suspicious_keywords(url)

    score += points
    reasons.append(message)


    # Final Status

    if score == 0:
        status = "Safe"

    elif score <= 40:
        status = "Suspicious"

    else:
        status = "High Risk"

    return {
        "status": status,
        "score": score,
        "reasons": reasons
    }