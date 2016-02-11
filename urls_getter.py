'''
The main issue:
    This solution doesn't support hexadecimal characters


https://tools.ietf.org/html/rfc1738.html
1. In general, URLs are written as follows:

       <scheme>:<scheme-specific-part>

   A URL contains the name of the scheme being used (<scheme>) followed
   by a colon and then a string (the <scheme-specific-part>) whose
   interpretation depends on the scheme.

   Scheme names consist of a sequence of characters. The lower case
   letters "a"--"z", digits, and the characters plus ("+"), period
   ("."), and hyphen ("-") are allowed. For resiliency, programs
   interpreting URLs should treat upper case letters as equivalent to
   lower case in scheme names (e.g., allow "HTTP" as well as "http").
Result: "a-z","0-9","+",".","-" are allowed, case insensetive
Example: "http:", "ftp:", etc.
2. URL can consist of hexadecimal characters (% and two hexadecimal
    characters "0-9a-f", e.g. 00, 0a, a2)
    2.1 URLs are written only with the graphic printable characters of the
   US-ASCII coded character set. The octets 80-FF hexadecimal are not
   used in US-ASCII, and the octets 00-1F and 7F hexadecimal represent
   control characters; these must be encoded.
3. Unsafe
    Unsafe:

   Characters can be unsafe for a number of reasons.  The space
   character is unsafe because significant spaces may disappear and
   insignificant spaces may be introduced when URLs are transcribed or
   typeset or subjected to the treatment of word-processing programs.
   The characters "<" and ">" are unsafe because they are used as the
   delimiters around URLs in free text; the quote mark (""") is used to
   delimit URLs in some systems.  The character "#" is unsafe and should
   always be encoded because it is used in World Wide Web and in other
   systems to delimit a URL from a fragment/anchor identifier that might
   follow it.  The character "%" is unsafe because it is used for
   encodings of other characters.  Other characters are unsafe because
   gateways and other transport agents are known to sometimes modify
   such characters. These characters are "{", "}", "|", "\", "^", "~",
   "[", "]", and "`".
Result: space_cahcrters (\s, or	[ \f\n\r\t\v]), <, >, ", #, %, {, }, | , /, ^, ~, [, ], ` are unsafe and must be encoded
4. Many URL schemes reserve certain characters for a special meaning:
   their appearance in the scheme-specific part of the URL has a
   designated semantics. If the character corresponding to an octet is
   reserved in a scheme, the octet must be encoded. The characters ";",
   "/", "?", ":", "@", "=" and "&" are the characters which may be
   reserved for special meaning within a scheme. No other characters may
   be reserved within a scheme.
5. Common Internet Scheme Syntax
    //<user>:<password>@<host>:<port>/<url-path>

   While the syntax for the rest of the URL may vary depending on the
   particular scheme selected, URL schemes that involve the direct use
   of an IP-based protocol to a specified host on the Internet use a
   common syntax for the scheme-specific data:

        //<user>:<password>@<host>:<port>/<url-path>

   Some or all of the parts "<user>:<password>@", ":<password>",
   ":<port>", and "/<url-path>" may be excluded.  The scheme specific
   data start with a double slash "//" to indicate that it complies with
   the common Internet scheme syntax. The different components obey the
   following rules:

    user
        An optional user name. Some schemes (e.g., ftp) allow the
        specification of a user name.

    password
        An optional password. If present, it follows the user
        name separated from it by a colon.

   The user name (and password), if present, are followed by a
   commercial at-sign "@". Within the user and password field, any ":",
   "@", or "/" must be encoded.

    Note that an empty user name or password is different than no user
   name or password; there is no way to specify a password without
   specifying a user name. E.g., <URL:ftp://@host.com/> has an empty
   user name and no password, <URL:ftp://host.com/> has no user name,
   while <URL:ftp://foo:@host.com/> has a user name of "foo" and an
   empty password.

    host
        The fully qualified domain name of a network host, or its IP
        address as a set of four decimal digit groups separated by
        ".". Fully qualified domain names take the form as described
        in Section 3.5 of RFC 1034 [13] and Section 2.1 of RFC 1123
        [5]: a sequence of domain labels separated by ".", each domain
        label starting and ending with an alphanumerical character and
        possibly also containing "-" characters. The rightmost domain
        label will never start with a digit, though, which
        syntactically distinguishes all domain names from the IP
        addresses.

    port
        The port number to connect to. Most schemes designate
        protocols that have a default port number. Another port number
        may optionally be supplied, in decimal, separated from the
        host by a colon. If the port is omitted, the colon is as well.

    url-path
        The rest of the locator consists of data specific to the
        scheme, and is known as the "url-path". It supplies the
        details of how the specified resource can be accessed. Note
        that the "/" between the host (or port) and the url-path is
        NOT part of the url-path.

   The url-path syntax depends on the scheme being used, as does the
   manner in which it is interpreted.

Possible urls:
{scheme}:{scheme-specific-part}
http://user:password@google.com
{scheme-specific-part}
//google.com
{domain-name}
google.com
'''

import requests
import re
# import bs4


# GETURL = re.compile(r'(?i)\b((?:https?://|www\d{0,3}[.]|[a-z0-9.\-]+[.][a-z]{2,4}/)(?:[^\s()<>]+|\(([^\s()<>]+|(\([^\s()<>]+\)))*\))+(?:\(([^\s()<>]+|(\([^\s()<>]+\)))*\)|[^\s`!()\[\]{};:\'".,<>?\xab\xbb\u201c\u201d\u2018\u2019]))')
# FINDURL = re.compile(r'(?:(?:https?|ftp)://)(?:\S+(?::\S*)?@)?(?:(?!10(?:\.\d{1,3}){3})(?!127(?:\.\d{1,3}){3})(?!169\.254(?:\.\d{1,3}){2})(?!192\.168(?:\.\d{1,3}){2})(?!172\.(?:1[6-9]|2\d|3[0-1])(?:\.\d{1,3}){2})(?:[1-9]\d?|1\d\d|2[01]\d|22[0-3])(?:\.(?:1?\d{1,2}|2[0-4]\d|25[0-5])){2}(?:\.(?:[1-9]\d?|1\d\d|2[0-4]\d|25[0-4]))|(?:(?:[a-z\x{00a1}-\x{ffff}0-9]+-?)*[a-z\x{00a1}-\x{ffff}0-9]+)(?:\.(?:[a-z\x{00a1}-\x{ffff}0-9]+-?)*[a-z\x{00a1}-\x{ffff}0-9]+)*(?:\.(?:[a-z\x{00a1}-\x{ffff}]{2,})))(?::\d{2,5})?(?:/[^\s]*)?')

class UrlsGetter:
    _urls = None

    def print_urls_str(self):
        """
        Print data to console out in shiny way:
        only "console_len" symbols at line
        """
        # n = console_len = 80
        # n = console_len
        # data = str(self._urls)
        # while n < data.__len__():
        #    print(data[(n-console_len):n])
        #     n += console_len
        # print(data[n-console_len:data.__len__()])
        links = [''.join(part) for part in self._urls]
        for link in links:
            print(str(link))

    def print_urls_tuples(self):
        """
        Print data to console out in shiny way:
        only "console_len" symbols at line
        """
        # n = console_len = 80
        # n = console_len
        # data = str(data)
        # while n < data.__len__():
        #    print(data[(n-console_len):n])
        #    n += console_len
        # print(data[n-console_len:data.__len__()])
        for link in self._urls:
            print(str(link))

    def _get_urls(self, _content):
        # scheme_pat = re.compile('[[a-z][0-9]\+\.\-]+:')
        # {scheme} = ([a-z0-9\+\.\-]+:)
        # start of {scheme_specific_part} = (//)
        # username = non-unsafe characters:
        # space_characters (\s, or	[ \f\n\r\t\v]), <, >, ", #, %, {, }, | , /, ^, ~, [, ], `
        # % can encode other characters
        # password = non-unsafe characters:
        # user_pass_pat = '([^ \s\<\>\"\#\{\}\|\/\^\~\[\]\`]?:?([^ \s\<\>\"\#\{\}\|\/\^\~\[\]\`]?(@)?'
        # host_pat
        # [a-z0-9\-\.] - has the "." because domain name can include of "."
        # last [a-z0-9\-] must not have "."
        scheme_pat = '([a-z0-9\+\.\-]+\:)?'
        specific_pat = '(//)?'
        safe_char_pat = '[^ \s\<\>\"\#\{\}\|\/\^\~\[\]\`\:\@]*'
        user_pass_pat = '('+safe_char_pat+':?'+safe_char_pat+'\@)?'
        host_pat = '([a-z0-9\-\.]+\.[a-z0-9\-]+)'
        url_pat = scheme_pat+specific_pat+user_pass_pat+host_pat
        _content = str(_content)
        _content = _content.lower()
        self._urls = re.findall(url_pat, _content)
        # return scheme

    def __init__(self, _site="https://tools.ietf.org/html/rfc1738.html"):
        r = requests.get(_site)
        self._get_urls(str(r.content))

# site = "https://tools.ietf.org/html/rfc1738.html"
# site = "http://bash.im"
# site = "https://ru.wikipedia.org/wiki/HTTPS"
site = "http://formvalidation.io/validators/uri/"
urls = UrlsGetter(site)
# urls.print_urls_tuples()
urls.print_urls_str()
