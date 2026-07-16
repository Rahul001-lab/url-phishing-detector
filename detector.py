from url_features import (
    check_dns_resolution,
    check_domain_age,
    check_encoded_characters,
    check_security_headers,
    check_ssl_certificate,
    validate_url,
    check_https,
    check_url_length,
    check_ip_address,
    check_at_symbol,
    check_dots,
    check_hyphen,
    check_digits,
    check_suspicious_keywords,
    check_url_shortener,
    check_double_slash,
    check_suspicious_tld,
    check_encoded_characters,
    check_redirects,
    check_punycode_domain
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

# Check SSL Certificate Validity

    points, message = check_ssl_certificate(url)

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

# URL Shortener Check

    points, message = check_url_shortener(url)

    score += points
    reasons.append(message)

# Double Slash Check

    points, message = check_double_slash(url)

    score += points
    reasons.append(message)

# Suspicious TLD Check

    points, message = check_suspicious_tld(url)

    score += points
    reasons.append(message)

# Encoded Character Check
    points, message = check_encoded_characters(url)

    score += points
    reasons.append(message)

# Redirects Check

    points, message = check_redirects(url)

    score += points
    reasons.append(message)

# Unicode/Punycode Detection

    points, message= check_punycode_domain(url)

    score +=points
    reasons.append(message)

# Check domain age using whois
   
    points,message = check_domain_age(url)
    
    score += points
    reasons.append(message)

 # DNS Resolution Check

    points,message = check_dns_resolution(url)

    score += points
    reasons.append(message)

# HTTP Security Headers Check

    points, message = check_security_headers(url)

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